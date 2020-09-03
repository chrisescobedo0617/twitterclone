from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required

from tweet.forms import AddTweetForm
from tweet.models import Tweet
from twitteruser.models import MyUser
from notification.models import Notification

import re
# Create your views here.


@login_required
def add_tweet(request):
    user = MyUser.objects.filter(username=request.user.username).first()
    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(
                author=user,
                text=data.get("text"),
            )
            mentions = re.findall(r'@[a-zA-Z0-9]+', new_tweet.text)
            print(mentions)
            for mention in mentions:
                print(mention[1:])
                mentioned_user = MyUser.objects.filter(
                    username=mention[1:]).first()
                if mentioned_user:
                    notification = Notification.objects.create(
                        user=MyUser.objects.filter(
                            username=mention[1:]).first(),
                        tweet=new_tweet
                    )
            return HttpResponseRedirect(reverse("homepage"))

    form = AddTweetForm()
    return render(request, "generic_form.html", {"form": form})


def tweet_view(request, tweet_id):
    user_tweets = 0
    my_tweet = Tweet.objects.filter(id=tweet_id).first()
    following_count = len(MyUser.objects.filter(
        id=my_tweet.author.id).first().following.all())
    if my_tweet:
        user_tweets = len(Tweet.objects.filter(author=my_tweet.author.id))
    return render(request, 'tweet_detail.html', {'tweet': my_tweet, 'tweet_num': user_tweets, 'following_count': following_count})
