"""The base widgets, but themed with bootstrap

These are based on home_page/venv/lib/python3.12/site-packages/django/forms/widgets.py
"""


from django import forms


def setFieldTemplate(template_name: str):
    """For some reason, the template_name attribute of the field is not being used. 
    This is a decorator that sets the template name for the field.
    """
    def decorator(field_class):
        def inner(*args, **kwargs):
            field_class(*args,
                        template_name=kwargs.pop('template_name',  # type: ignore
                                                 'form_widgets/bootstrap_char_form_groups.html'),
                        **kwargs,)
        return inner
    return decorator


class BootstrapCharFieldWidget(forms.TextInput):
    template_name = 'form_widgets/text_input.html'


class BootstrapCharField(forms.CharField):
    widget = BootstrapCharFieldWidget

    @setFieldTemplate('form_widgets/bootstrap_char_form_groups.html')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class BootstrapEmailField(forms.EmailField):
    widget = BootstrapCharFieldWidget

    @setFieldTemplate('form_widgets/bootstrap_char_form_groups.html')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
