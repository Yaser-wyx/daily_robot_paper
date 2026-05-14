document.querySelectorAll('.copy-button').forEach((button) => {
    button.addEventListener('click', async () => {
        const code = button.closest('.code-block')?.querySelector('pre code');
        if (!code) {
            return;
        }

        try {
            await navigator.clipboard.writeText(code.innerText);
            const original = button.textContent;
            button.textContent = 'Copied';
            button.classList.add('is-copied');
            window.setTimeout(() => {
                button.textContent = original;
                button.classList.remove('is-copied');
            }, 1400);
        } catch (error) {
            button.textContent = 'Copy failed';
            window.setTimeout(() => {
                button.textContent = 'Copy Prompt';
            }, 1400);
        }
    });
});
