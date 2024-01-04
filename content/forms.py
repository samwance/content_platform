from django import forms
from .models import Content


class StyleMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class ContentForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Content
        fields = ('name', 'description', 'preview', 'is_free')
        widgets = {"is_free": forms.Select(choices=((True, "Yes"), (False, "No")))}
