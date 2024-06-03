from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'base/home.html'

class ResumeView(TemplateView):
    template_name = 'base/resume.html'

class ContactView(TemplateView):
    template_name = 'base/contact.html'

class ServicesView(TemplateView):
    template_name = 'base/services.html'

