from django.contrib import admin  # Import admin here
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Add the path for the admin interface
    path('', include('testapp.urls')),  # Include your app URLs
]
