from django.shortcuts import render, HttpResponseRedirect, reverse

from notification.models import Notification
from twitteruser.models import MyUser
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def notification_view(request):
    all_notifications = []
    notifications = Notification.objects.filter(user__id=request.user.id)
    user_tweets = len(Tweet.objects.filter(author__id=request.user.id))
    following_count = len(MyUser.objects.filter(
        id=request.user.id).first().following.all())
    for notification in notifications:
        if not notification.seen:
            all_notifications.append(notification)
        notification.seen = True
        notification.save()

    return render(request, 'notification.html', {"notifications": all_notifications, 'user_tweets': user_tweets, 'following_count': following_count, 'notification_count': len(all_notifications)})
