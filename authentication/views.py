from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from authentication.forms import SignupForm, LoginForm
from twitteruser.models import MyUser

# Create your views here.


class LoginView(TemplateView):

    def get(self, request):
        form = LoginForm
        return render(request, "login_form.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                "username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))


class SignupView(TemplateView):

    def get(self, request):
        form = SignupForm()
        return render(request, "generic_form.html", {"form": form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(
                username=data.get("username"), password=data.get("password"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))


class LogoutView(TemplateView):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("homepage"))
