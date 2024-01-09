from django import forms
from .models import Content, Collection

CATEGORY_CHOICES = [
        ("Art", "Art"),
        ("Poems", "Poems"),
        ("Education", "Education"),
        ("Entertainment", "Entertainment"),
        ("Not_selected", "Not selected"),
    ]

class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class ContentForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-input'}))
    preview = forms.ImageField(label='Preview', widget=forms.FileInput(attrs={'class': 'form-input'}), required=False)
    is_free = forms.ChoiceField(label='To make public?', choices=((True, "Yes"), (False, "No")))
    category = forms.ChoiceField(label='Category', choices=CATEGORY_CHOICES)
    collection = forms.ModelChoiceField(label='Collection', queryset=Collection.objects.all(), required=False)

    class Meta:
        model = Content
        fields = ("name", "description", "preview", "is_free", 'category', 'collection')
        labels = {
            'name': 'Name',
            'preview': 'Preview',
            'description': 'Description',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'preview': forms.FileInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input'}),
            "is_free": forms.Select(choices=((True, "Yes"), (False, "No"))),
            'category': forms.Select(choices=CATEGORY_CHOICES),
            'collection': forms.Select(attrs={'class': 'form-input'}),
        }


class CollectionForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-input'}))
    preview = forms.ImageField(label='Preview', widget=forms.FileInput(attrs={'class': 'form-input'}), required=False)

    class Meta:
        model = Collection
        fields = ("name", "description", "preview")
        labels = {
            'name': 'Name',
            'preview': 'Preview',
            'description': 'Description',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'preview': forms.FileInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input'}),
        }
