from django.urls import path
from contact_us.views import ContactUs, ThankYou
app_name = "contact_us"
urlpatterns = [
    path('', ContactUs.as_view(), name="contact"),
    path('thank_you/', ThankYou.as_view(), name='thank_you'),
]
