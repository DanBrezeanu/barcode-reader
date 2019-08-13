from django import forms

class BarcodeForm(forms.Form):
    photo = forms.ImageField()
