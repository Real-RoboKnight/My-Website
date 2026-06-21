""" Code to have a rich text editor on a form. """

from django import forms
from bs4 import BeautifulSoup


class RichTextWidget(forms.Widget):
    """A widget that provides a rich text editor."""
    template_name = 'form_widgets/rich_text_widget.html'


class RichTextField(forms.CharField):
    """A form field that provides a rich text editor."""
    widget = RichTextWidget

    def __init__(self, *args, **kwargs):
        label = kwargs.pop('label', '')
        super().__init__(*args,
                         label=label,  # type: ignore
                         template_name=kwargs.pop('template_name',  # type: ignore
                                                  'form_widgets/bootstrap_form_groups.html'),
                         **kwargs,)

    def validate(self, value):
        # Ensure that there is no malicious HTML. Allowed tags are <p>, <strong>, <em>, <u>, <blockquote>, <div>, <span>, <a>, <ol>, <li>, <h1>, <h2>, <h3>, <sub>, <sup>
        allowed_tags = ['p', 'strong', 'em', 'u', 'blockquote', 'div', 'span', 'a', 'ol', 'li', 'h1', 'h2', 'h3', 'sub', 'sup']
        soup = BeautifulSoup(value, 'html.parser')
        for tag in soup.find_all():
            if tag.name not in allowed_tags:
                raise forms.ValidationError(f"Tag <{tag.name}> is not allowed.")
            if tag.name == 'a' and not tag.has_attr('href'):
                raise forms.ValidationError("Anchor tags must have an href attribute.")
        super().validate(value)

    def to_python(self, value) -> str:
        """Converts the input value to a string."""
        return str(super().to_python(value))  # pyright: ignore[reportAttributeAccessIssue]
