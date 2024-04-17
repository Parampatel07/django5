from django import forms

class loginForm(forms.Form):
     email = forms.CharField(label="Enter your Email ",widget=forms.EmailInput(attrs={'class': "form-control"}))
     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))