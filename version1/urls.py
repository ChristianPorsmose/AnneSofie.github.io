"""Defines URL patterns for version1."""
from django.urls import path
from . import views

app_name = 'version1'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    #page that show all topics
    path('topics/', views.topics, name='topics'),
    #page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    #page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    
    
]
