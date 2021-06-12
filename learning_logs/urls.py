"""Learning logs URLs"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topics page
    path('topics/', views.topics, name='topics'),
    # Detail page for single topic
    path('topics/<int:topic_id>/', views.topic, name='topic')
]