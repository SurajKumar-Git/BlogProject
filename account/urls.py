from django.urls import path, include
from account.views import LoginView, RegisterView, PasswordChangeView, PasswordChangeDoneView
from account.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from account.views import Profile, PublicProfileView, UpdateProfile


app_name = "account"
urlpatterns = [
    path("login/", LoginView.as_view(), name='login'),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", Profile.as_view(), name="user_profile"),
    path("profile/", Profile.as_view(), name="user_profile"),
    path("profile/<slug:slug>/view", PublicProfileView.as_view(),
         name="user_public_profile"),
    path("profile/<slug:slug>/update",
         UpdateProfile.as_view(), name="update_user_profile"),
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
