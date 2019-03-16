from django.contrib import admin
from django.urls import path

from twitter.views import MainPageView


app_name = 'twitter'
urlpatterns = [
    path('', MainPageView.as_view(), name='index'),
]

