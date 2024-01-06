from django import forms

from subscription.models import Subscription


class SubscriptionForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    card_number = forms.ImageField(label='Card number', widget=forms.TextInput(attrs={'class': 'form-input'}))
    exp_month = forms.IntegerField(label='Expire month', widget=forms.TextInput(attrs={'class': 'form-input'}))
    exp_year = forms.IntegerField(label='Expire year', widget=forms.TextInput(attrs={'class': 'form-input'}))
    cvc = forms.IntegerField(label='CVC', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Subscription
        fields = ['name', 'email', 'card_number', 'exp_month', 'exp_year', 'cvc']
        labels = {
            'name': 'Name',
            'email': 'Email',
            'card_number': 'Card Number',
            'exp_month': 'Expiration Month',
            'exp_year': 'Expiration Year',
            'cvc': 'CVC',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'card_number': forms.TextInput(attrs={'class': 'form-input'}),
            'exp_month': forms.NumberInput(attrs={'class': 'form-input'}),
            'exp_year': forms.NumberInput(attrs={'class': 'form-input'}),
            'cvc': forms.TextInput(attrs={'class': 'form-input'}),
        }
