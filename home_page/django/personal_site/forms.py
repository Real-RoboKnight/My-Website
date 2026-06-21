from django import forms

from .form_tools.rich_text import RichTextField
from .form_tools.turnstile import TurnstileField


class Contact_Me(forms.Form):
    """A form for the contact me page."""
    template_name = "form_widgets/bootstrap_form_groups.html"
    field_template_name = "form_widgets/bootstrap_form_groups.html"

    name = forms.CharField(label="Name", max_length=100)
    response_email = forms.EmailField(label="Response Email", max_length=100)
    subject = forms.CharField(label="Subject", max_length=50, min_length=5)
    content = RichTextField(
        initial='<p><span class="ql-font-Hermit">Dear Dylan,</span></p><p><br></p><p class="ql-indent-1"><span class="ql-font-Hermit">Hello!</span></p><p><br></p><p><span class="ql-font-Hermit">Thanks,</span></p><p class="ql-indent-1"><span style="color: rgb(230, 0, 0);" class="ql-font-Hermit">[Name]</span></p>',
        label="Content", min_length=10, max_length=10000)
    turnstile_token = TurnstileField()
