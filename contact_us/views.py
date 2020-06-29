from django.shortcuts import render
from contact_us.forms import ContactUsForm
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
# Create your views here.


class ContactUs(FormView):
    form_class = ContactUsForm
    success_url = reverse_lazy('contact_us:thank_you')
    template_name = "contact_us/contact_us.html"


class ThankYou(TemplateView):
    template_name = "contact_us/thank_you.html"
