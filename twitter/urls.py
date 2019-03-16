from django.contrib import admin
from django.urls import path

from twitter.views import MainPageView, RegisterView, AddTweetView


app_name = 'twitter'
urlpatterns = [
    path('', MainPageView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('add_tweet/', AddTweetView.as_view(), name='add_tweet'),
]

