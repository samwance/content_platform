from django import forms
from .models import Content, Collection

CATEGORY_CHOICES = [
    ("Not_selected", "Not selected"),
    ("Art", "Art"),
    ("Poems", "Poems"),
    ("Education", "Education"),
    ("Entertainment", "Entertainment"),
]


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class ContentForm(StyleMixin, forms.ModelForm):
    collection = forms.ModelChoiceField(queryset=Collection.objects.none(), required=True)

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
            'category': forms.Select(choices=CATEGORY_CHOICES, ),
            'collection': forms.Select(attrs={'class': 'form-input'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['collection'].queryset = Collection.objects.filter(user=user)



class CollectionForm(StyleMixin, forms.ModelForm):
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
