from django import forms

class Django_form(forms.Form):
    name = forms.CharField(label="User Name")
    email = forms.CharField(label="Email")