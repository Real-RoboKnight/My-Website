import * as bootstrap from "bootstrap";

async function send_data(to: URL, data: FormData) {
    try {
        const response = await fetch(to, { body: data, method: "POST" });
        return response;
    } catch (e) {
        console.error(e);
    }
}

/**
 * Used to notify the user of that the form is being processed.
 * @param form The html form
 * @param modal The modal to show to the user
 * @param redirect? Optional - A URL to take them too; If not present will refresh the page
 */
export function notify_form_submission(form: HTMLFormElement, modal: bootstrap.Modal, redirect: string | undefined | null) {
    form.addEventListener('submit', async function handler(event) {
        // Stop the page from immediately redirecting
        event.preventDefault();
        const formData = new FormData(form);
        const response = await send_data(new URL(form.action), formData)

        if (response?.status == 400) {
            form.removeEventListener('submit', handler)
            form.requestSubmit();
            return;
        }
        if (response?.ok) {
            if (!redirect)
                redirect = window.location.href;

            modal._element.addEventListener('hidden.bs.modal', function () {
                window.location.href = redirect
            });
            // Artificial wait to show 'progress'
            form.querySelectorAll('button[type="submit"]').forEach((button) => {
                button.innerHTML = '<div class="spinner-border" role="status"></div>'
            });
            setTimeout(() => { modal.show(); }, 750);
        }

        return;
    }
    );
}