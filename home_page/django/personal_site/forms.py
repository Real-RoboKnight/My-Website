from django import forms


class Contact_Me(forms.Form):
    """A form for the contact me page."""
    name = forms.CharField(label="Name", max_length=100)
    response_email = forms.EmailField(label="Email", max_length=100)
    subject = forms.CharField(label="Subject", max_length=100, min_length=5)
    content = forms.CharField(label="Content")
    turnstile_token = forms.CharField(label="turnstile_token",
                                            widget=forms.HiddenInput(), required=True)
