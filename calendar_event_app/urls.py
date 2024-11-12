# calendar_event_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page view
    path('send-interview-notification/', views.send_interview_notification, name='send_interview_notification'),
]
