import { make_div_editor_form } from './rich_text_form';
import { turnstile_form } from './turnstile_form'
console.log("Main entry point loaded.");




declare global {
    interface Window {
        make_div_editor_form: typeof make_div_editor_form;
        turnstile_form: typeof turnstile_form
    }
}

window.make_div_editor_form = make_div_editor_form;
window.turnstile_form = turnstile_form