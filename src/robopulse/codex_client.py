import glob
import json
import os
import shutil
import subprocess
import tempfile
import time

from robopulse.config import CHATGPT_WEB_URL, CODEX_MODEL
from robopulse.utils import clean_json_string, extract_codex_output_from_jsonl, print

CODEX_BIN = None


def resolve_cli_binary(binary_name):
    """Find a CLI from PATH or a typical nvm installation."""
    binary_path = shutil.which(binary_name)
    if binary_path:
        return binary_path

    candidates = sorted(
        glob.glob(os.path.expanduser(f"~/.nvm/versions/node/*/bin/{binary_name}")),
        reverse=True,
    )
    for candidate in candidates:
        if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
            return candidate

    return None


def ensure_runtime_requirements():
    """Fail fast when local prerequisites are unavailable."""
    global CODEX_BIN
    CODEX_BIN = resolve_cli_binary("codex")
    if not CODEX_BIN:
        print("❌ [Error] Codex CLI not found. Run `codex login` and ensure `codex` is in PATH.")
        return False

    if not CHATGPT_WEB_URL:
        print("❌ [Error] CHATGPT_WEB_URL is empty. Set it or use the default https://chatgpt.com/.")
        return False

    return True

def run_codex_structured(prompt, schema, task_label, max_retries=2, retry_delay=3):
    """Invoke codex exec and force the final message through a JSON schema."""
    codex_bin = CODEX_BIN or resolve_cli_binary("codex")
    if not codex_bin:
        print("❌ [Error] Codex CLI not found. Run `codex login` and ensure `codex` is in PATH.")
        return None

    for attempt in range(max_retries):
        schema_path = None
        output_path = None
        try:
            with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as schema_file:
                json.dump(schema, schema_file, ensure_ascii=False)
                schema_path = schema_file.name

            with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as output_file:
                output_path = output_file.name

            command = [
                codex_bin,
                "exec",
                "--color",
                "never",
                "--json",
                "--ephemeral",
                "--output-schema",
                schema_path,
                "--output-last-message",
                output_path,
                "-",
            ]
            if CODEX_MODEL:
                command[2:2] = ["-m", CODEX_MODEL]

            print(f"  🚀 [Codex] Request submitted. {task_label}...", flush=True)
            process = subprocess.Popen(
                command,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
            )

            start_time = time.time()
            stdout = ""
            stderr = ""
            pending_input = prompt
            while True:
                try:
                    stdout, stderr = process.communicate(input=pending_input, timeout=15)
                    break
                except subprocess.TimeoutExpired:
                    pending_input = None
                    elapsed = int(time.time() - start_time)
                    print(f"  ⏳ [Codex] Still working... {elapsed}s elapsed.", flush=True)

            with open(output_path, "r", encoding="utf-8") as output_file:
                structured_output = output_file.read().strip()

            elapsed = int(time.time() - start_time)
            jsonl_output = extract_codex_output_from_jsonl(stdout)
            fallback_output = structured_output or jsonl_output or clean_json_string(stdout)

            if fallback_output:
                if process.returncode != 0:
                    print(
                        f"  ⚠️ [Codex] CLI exited with code {process.returncode}, but a structured response was recovered from stdout.",
                        flush=True,
                    )
                print(f"  ✅ [Codex] Structured response received in {elapsed}s.", flush=True)
                return fallback_output

            if process.returncode != 0:
                error_lines = [line.strip() for line in (stderr or "").splitlines() if line.strip()]
                if not error_lines:
                    error_lines = [line.strip() for line in (stdout or "").splitlines() if line.strip()]
                error_msg = error_lines[-1] if error_lines else "Unknown Codex error"
                print(f"  ⚠️ [Retry {attempt + 1}/{max_retries}] Codex CLI failed: {error_msg}")
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                    continue
                return None

            print(
                f"  ⚠️ [Retry {attempt + 1}/{max_retries}] Codex finished after {elapsed}s but returned empty output."
            )
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                continue
            return None
        except Exception as exc:
            print(f"  ❌ [Retry {attempt + 1}/{max_retries}] Exception calling Codex CLI: {exc}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                continue
            return None
        finally:
            for temp_path in (schema_path, output_path):
                if temp_path and os.path.exists(temp_path):
                    os.remove(temp_path)

    return None
