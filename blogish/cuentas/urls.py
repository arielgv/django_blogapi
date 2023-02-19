from django.contrib import admin
from django.urls import path 

from views import registerview

urlpatterns = [
    path('register/', registerview.as_view())
]
