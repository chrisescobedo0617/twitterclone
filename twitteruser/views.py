from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from twitteruser.models import MyUser
from tweet.models import Tweet
from notification.models import Notification

# Create your views here.


@login_required
def index(request):
    following_list = request.user.following.all()
    all_tweets = Tweet.objects.all().order_by('-id')
    user_tweets = len(Tweet.objects.filter(author__id=request.user.id))
    notifications = Notification.objects.filter(
        user__id=request.user.id, seen=False)
    following_count = len(MyUser.objects.filter(
        id=request.user.id).first().following.all())
    return render(request, 'home.html', {'tweets': all_tweets, 'user_tweets': user_tweets, 'following_count': following_count, 'notification_count': len(notifications), 'following_list': following_list})


def user_detail(request, username):
    author_tweets = Tweet.objects.filter(
        author__username=username).order_by('-id')
    user_tweets = len(author_tweets)
    name = MyUser.objects.filter(username=username).first()
    if not name:
        return render(request, '404.html')
    following_count = len(name.following.all())
    following_status = False
    if request.user.is_authenticated:
        for user in request.user.following.all():
            if username == user.username:
                following_status = True
    return render(request, "user_detail.html", {"author_tweets": author_tweets, 'user_tweets': user_tweets, 'name': name, 'following_status': following_status, 'following_count': following_count})


def follow(request, username):
    user_to_follow = MyUser.objects.filter(username=username).first()
    following_user = MyUser.objects.get(username=request.user.username)

    following_user.following.add(user_to_follow)
    following_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unfollow(request, username):
    user_to_unfollow = MyUser.objects.filter(username=username).first()
    unfollowing_user = MyUser.objects.get(username=request.user.username)

    unfollowing_user.following.remove(user_to_unfollow)
    unfollowing_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
