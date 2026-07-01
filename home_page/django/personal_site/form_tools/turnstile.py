"""Code to put a cloudflare turnstile on a form."""

from django.conf import settings
from django import forms
import requests


class TurnstileWidget(forms.Widget):
    """A widget that uses the cloudflare turnstile for bot protection."""

    template_name = "form_widgets/turnstile_widget.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):

        context = super().get_context(name, value, attrs)
        context["turnstile_public_key"] = settings.TURNSTILE_PUBLIC_KEY
        return context


class TurnstileField(forms.Field):
    """A form field that uses the cloudflare turnstile for bot protection."""

    template_name = "form_widgets/bootstrap_form_groups.html"
    widget = TurnstileWidget

    def __init__(self, *args, **kwargs):
        label = kwargs.pop("label", "")
        super().__init__(
            *args,
            label=label,
            template_name=kwargs.pop(
                "template_name",  # type: ignore
                "form_widgets/bootstrap_form_groups.html",
            ),
            **kwargs,
        )

    def validate(self, value):
        errors = {
            "missing-input-secret": "Secret parameter not provided",
            "invalid-input-secret": "Secret key is invalid or expired",
            "missing-input-response": "Response parameter was not provided",
            "invalid-input-response": "Token is invalid, malformed, or expired",
            "bad-request": "Request is malformed",
            "timeout-or-duplicate": "Token has already been validated",
            "internal-error": "Internal error occurred",
        }
        super().validate(value)
        response = requests.post(
            url="https://challenges.cloudflare.com/turnstile/v0/siteverify",
            data={
                "secret": settings.TURNSTILE_SECRET_KEY,
                "response": value,
            },
            timeout=10,
        )
        result = response.json()
        if result.get("success"):
            return

        raise forms.ValidationError(
            [
                "Bot Verification Failed: " + errors.get(code, "Unknown error")
                for code in result.get("error-codes", [])
                if code != "timeout-or-duplicate"
                # For some reason, django checks this twice, so the token is always duplicated.
                # I don't know why, but it is. So, I will just ignore this error.
            ]
        )

    def to_python(self, value) -> str:
        """Gets the token that the turnstile widget generates and returns it."""
        return str(super().to_python(value))

    def bound_data(self, data, initial):
        """Regenerate the token every time that the form is bound."""
        return None
