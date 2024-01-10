from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
    PasswordChangeForm,
)

from django import forms
from content.forms import StyleMixin
from users.models import User


class LoginUserForm(StyleMixin, AuthenticationForm):
    class Meta:
        model = User
        fields = ["password"]



class RegisterUserForm(StyleMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ["name", "phone", "password1", "password2"]
        labels = {
            "phone": "Phone Number",
            "name": "Name",
        }
        widgets = {
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError("This phone already exists")
        return phone


class ProfileUserForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ["phone", "name", "photo"]
        labels = {
            "phone": "Phone",
            "name": "Name",
            "photo": "Photo",
        }
        widgets = {
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "photo": forms.FileInput(attrs={"class": "form-select-image"}),
        }
