from django import forms

class SubscriptionForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    card_number = forms.CharField(max_length=16)
    exp_month = forms.IntegerField()
    exp_year = forms.IntegerField()
    cvc = forms.CharField(max_length=4)
