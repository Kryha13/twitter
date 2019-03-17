from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from twitter.views import MainPageView, RegisterView, AddTweetView, ProfileView, TweetDetailsView


app_name = 'twitter'
urlpatterns = [
    path('', MainPageView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('add_tweet/', AddTweetView.as_view(), name='add_tweet'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('tweet/<tweet_id>', TweetDetailsView.as_view(), name='tweet'),
]

