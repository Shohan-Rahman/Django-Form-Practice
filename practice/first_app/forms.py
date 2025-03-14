from django import forms

class DjangoForm(forms.Form):
    name = forms.CharField(label='User Name')
    email = forms.EmailField(label='Email')