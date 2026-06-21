import * as bootstrap from 'bootstrap';
import { rich_text_form } from './rich_text_form';
import { turnstile_form } from './turnstile_form'
import { notify_form_submission } from './notify_form_submission'
console.log("Main entry point loaded.");




declare global {
    interface Window {
        bootstrap: typeof bootstrap;
        rich_text_form: typeof rich_text_form;
        turnstile_form: typeof turnstile_form
        notify_form_submission: typeof notify_form_submission
    }
}

window.bootstrap = bootstrap;
window.rich_text_form = rich_text_form;
window.turnstile_form = turnstile_form
window.notify_form_submission = notify_form_submission