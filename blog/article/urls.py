from django.contrib import admin
from django.urls import path, include
from .views import index, about

app_name="article"

urlpatterns = [
    path('create/', index, name="index"),

]