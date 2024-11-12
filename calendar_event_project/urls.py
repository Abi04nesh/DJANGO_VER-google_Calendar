# calendar_event_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('calendar-event/', include('calendar_event_app.urls')),  # Only include the app URLs here
]
