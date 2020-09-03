from django import forms
from twitteruser.models import MyUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ["username", "password", ]
        widgets = {'password': forms.PasswordInput()}
