from django.shortcuts import render
from django.contrib.auth import views
from django.contrib.auth import forms
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


class PasswordChangeView(views.PasswordChangeView):
    template_name = "account/password_change_form.html"
    success_url = reverse_lazy("account:password_change_done")

    def get_form_class(self):
        if self.request.user.has_usable_password():
            return forms.PasswordChangeForm
        else:
            return forms.SetPasswordForm   # if user password is not set


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = "account/password_change_done.html"
