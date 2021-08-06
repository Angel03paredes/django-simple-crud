from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='name', max_length=100,required=True)
    email = forms.CharField(label='email', max_length=100,required=True)
    password = forms.CharField(label='password', max_length=100,required=True)
