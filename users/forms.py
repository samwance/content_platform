from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm

from django import forms
from content.forms import StyleMixin
from users.models import User


class LoginUserForm(StyleMixin, AuthenticationForm):
    password = forms.CharField(label="Password",
                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['password']


class RegisterUserForm(StyleMixin, UserCreationForm):
    phone = forms.CharField(label="Phone", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Password repeat", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['name', 'phone', 'password1', 'password2']
        labels = {
            'phone': 'Phone Number',
            'name': "Name",
        }
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError("This phone already exists")
        return phone



class ProfileUserForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    phone = forms.CharField(label='Phone', widget=forms.TextInput(attrs={'class': 'form-input'}))
    photo = forms.ImageField(label='Photo', widget=forms.FileInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['phone', 'name', 'photo']
        labels = {
            'phone': 'Phone',
            'name': 'Name',
            'photo': 'Photo',
        }
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'photo': forms.FileInput(attrs={'class': 'form-input'}),
        }

