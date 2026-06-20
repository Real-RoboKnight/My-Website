import * as bootstrap from "bootstrap";
import { loadScriptFromUrl } from "./load_remote_script";

type TurnstileRenderOptions = {
    sitekey: string;
    theme?: "light" | "dark" | "auto";
    size?: "normal" | "compact" | "flexible";
    execution?: "render" | "execute";
    'response-field-name'?: string
    callback?: (token: string) => void;
    'error-callback'?: (errorCode: string) => void;
    'expired-callback'?: () => void;
    'timeout-callback'?: () => void;
};

type TurnstileApi = {
    render: (container: string | HTMLElement, options: TurnstileRenderOptions) => any;
};

declare global {
    interface Window {
        turnstile: TurnstileApi;
    }
}

/**
 * Used to authenticate on a form that should not be bot spammed
 * @param id the turnstile elem: <div id="turnstile-container"></div>
 * @param form The form with which to include the user's human token
 */
export function turnstile_form(id: HTMLDivElement, form: HTMLFormElement, error_div: HTMLDivElement) {
    loadScriptFromUrl(
        "https://challenges.cloudflare.com/turnstile/v0/api.js",
        {
            async: true,
            defer: true
        }
    ).then(() => {
        const widgetId = window.turnstile.render(id, {
            sitekey: "0x4AAAAAADn448-Kh06GWZ7e",
            theme: "dark",
            size: "flexible",
            'response-field-name': 'turnstile_token',
            callback: function (token: string) {
                console.log("Success:", token);
                const submitElements = form.querySelectorAll<HTMLButtonElement | HTMLInputElement>(
                    'button[type="submit"], input[type="submit"]'
                );

                submitElements.forEach((element) => {
                    element.disabled = false;
                    element.removeAttribute("aria-disabled");
                });
            },

            'expired-callback': function () {
                console.log("Turnstile Expired");
                const submitElements = form.querySelectorAll<HTMLButtonElement | HTMLInputElement>(
                    'button[type="submit"], input[type="submit"]'
                );

                submitElements.forEach((element) => {
                    element.disabled = true;
                    element.setAttribute("aria-disabled", "true");
                });
                // window.turnstile.reset();
            },

            'error-callback': function (error) {
                error_div.innerHTML = `
    <div class="alert alert-danger" role="alert">
        Unfortunately, we ran into an error verifying that you are human :(  Error code: ` + error + `
    </div>
`;
                const bsCollapse = new bootstrap.Collapse(error_div, {
                    toggle: false // Prevents it from automatically toggling upon initialization
                });
                const submitElements = form.querySelectorAll<HTMLButtonElement | HTMLInputElement>(
                    'button[type="submit"], input[type="submit"]'
                );

                submitElements.forEach((element) => {
                    element.disabled = true;
                    element.setAttribute("aria-disabled", "true");
                });
                bsCollapse.show();
            }
        });
    });
}

