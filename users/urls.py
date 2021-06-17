"""Users URL patterns"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Include default authorization urls.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register'),
]