from django import forms

from .form_tools import (
    RichTextField,
    TurnstileField,
    BootstrapCharField,
    BootstrapEmailField,
)
from .form_tools.rich_text import RichTextWidget


class Contact_Me(forms.Form):
    """A form for the contact me page."""

    # template_name = "form_widgets/bootstrap_form_groups.html"
    # field_template_name = "form_widgets/bootstrap_form_groups.html"

    name = BootstrapCharField(
        label="Name",
        max_length=100,
        widget=BootstrapCharField.widget(attrs={"autocomplete": "name"}),  # pyright: ignore[reportCallIssue]
    )
    response_email = BootstrapEmailField(
        label="Response Email",
        max_length=100,
        widget=BootstrapEmailField.widget(
            attrs={"autocomplete": "email", "inputmode": "email"}
        ),  # pyright: ignore[reportCallIssue]
    )
    subject = BootstrapCharField(label="Subject", max_length=50, min_length=5)
    content = RichTextField(
        widget=RichTextWidget(attrs={"editor_height": "75vh"}),
        initial='<p><span class="ql-font-Hermit">Dear Dylan,</span></p><p><br></p><p class="ql-indent-1"><span class="ql-font-Hermit">Hello!</span></p><p><br></p><p><span class="ql-font-Hermit">Thanks,</span></p><p class="ql-indent-1"><span style="color: rgb(230, 0, 0);" class="ql-font-Hermit">[Name]</span></p>',
        min_length=10,
        max_length=100000,
    )
    turnstile_token = TurnstileField()
