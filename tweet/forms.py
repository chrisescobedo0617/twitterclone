from django import forms

from twitteruser.models import MyUser
from tweet.models import Tweet


class AddTweetForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, max_length=140)
