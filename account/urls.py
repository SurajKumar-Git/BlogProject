from django.urls import path, include
from account.views import LoginView, RegisterView, PasswordChangeView, PasswordChangeDoneView
from account.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


app_name = "account"
urlpatterns = [
    path("login/", LoginView.as_view(), name='login'),
    path("register/", RegisterView.as_view(), name="register"),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path("", include("django.contrib.auth.urls")),
]
