from django.contrib import admin
from django.urls import path

from twitter.views import MainPageView, RegisterView


app_name = 'twitter'
urlpatterns = [
    path('', MainPageView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
]

