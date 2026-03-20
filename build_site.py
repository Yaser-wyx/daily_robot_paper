import shutil
from pathlib import Path

from site_renderer import REPORTS_DIR, STATIC_DIR, load_reports, render_archive_page, render_detail_page

OUTPUT_DIR = Path("dist")


def reset_output_dir(output_dir):
    """Create a clean output directory for the static build."""
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)


def copy_static_assets(output_dir):
    """Copy the static asset directory into the build output."""
    shutil.copytree(STATIC_DIR, output_dir / "static")


def write_text(path, content):
    """Write a UTF-8 text file, creating parent directories as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_site(report_dir=REPORTS_DIR, output_dir=OUTPUT_DIR):
    """Build the complete static site into dist/."""
    print(f"[build] Loading reports from {report_dir}")
    reports = load_reports(report_dir)
    reset_output_dir(output_dir)
    copy_static_assets(output_dir)

    write_text(output_dir / ".nojekyll", "")
    print(f"[build] Rendering archive page for {len(reports)} reports")
    write_text(output_dir / "index.html", render_archive_page(reports, page_depth=0))

    for report in reports:
        detail_path = output_dir / "reports" / report.report_id / "index.html"
        print(f"[build] Rendering {report.filename}")
        try:
            detail_html = render_detail_page(report, page_depth=2)
        except Exception as exc:
            raise RuntimeError(f"Failed to render report {report.markdown_path}: {exc}") from exc
        write_text(detail_path, detail_html)

    print(f"[build] Static site written to {output_dir}")


def main():
    """Entry point for GitHub Pages static builds."""
    build_site()


if __name__ == "__main__":
    main()
