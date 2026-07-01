from django import template
from django.utils.safestring import SafeText, mark_safe

register = template.Library()


@register.filter("quill_to_email")
def convert_quill_to_email_html(text: str) -> SafeText:
    """Converts some of the classes that Quill uses to HTML that can be used in an email.
    This is a very basic implementation and only handles a few classes, but it should be enough for the contact me form."""
    out = str(text)
    out = out.replace(
        '<pre data-language="plain">',
        '<pre data-language="plain" style="background-color: #23241f; color: #f8f8f2;}">',
    )
    out = out.replace(
        "<blockquote>",
        '<blockquote style="border-left:1px solid rgb(204,204,204);padding-left:1ex">',
    )
    out = out.replace('class="ql-align-center"', 'style="text-align: center;"')
    out = out.replace('class="ql-align-right"', 'style="text-align: right;"')
    out = out.replace('class="ql-align-justify"', 'style="text-align: justify;"')
    out = out.replace('class="ql-align-left"', 'style="text-align: left;"')
    out = out.replace('class="ql-size-huge"', 'style="font-size: 2.5em;"')
    out = out.replace('class="ql-size-large"', 'style="font-size: 1.5em;"')
    out = out.replace('class="ql-size-small"', 'style="font-size: 0.75em;"')
    for i in range(1, 10):
        out = out.replace(
            f'class="ql-indent-{i}"',
            f'style="margin-left: {i * 3}em;"',
        )
    return mark_safe(out)
