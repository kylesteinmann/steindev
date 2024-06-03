from django.urls import path
from .views import (HomeView, ResumeView, ContactView, ServicesView)

app_name = 'base'

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('resume', ResumeView.as_view(), name='resume'),
  path('contact', ContactView.as_view(), name='contact'),
  path('services', ServicesView.as_view(), name='services')
]