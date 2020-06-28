from django.shortcuts import render
from django.contrib.auth import views
from django.views import generic
from django.urls import reverse, reverse_lazy
from account.forms import LoginForm
# Create your views here.


class LoginView(views.LoginView):
    template_name = "account/login.html"
    form_class = LoginForm
    redirect_authenticated_user = True  # redirecting authenticated user,


class RegisterView(generic.CreateView):
    pass


class PasswordResetView(views.PasswordResetView):
    template_name = "account/password_reset_form.html"
    email_template_name = "account/password_reset_email.html"
    success_url = reverse_lazy("account:password_reset_done")


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = "account/password_reset_done.html"


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    template_name = "account/password_reset_confirm.html"
    success_url = reverse_lazy("account:password_reset_complete")


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = "account/password_reset_complete.html"
