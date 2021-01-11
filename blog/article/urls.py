from django.contrib import admin
from django.urls import path, include
from .views import dashboard,addArticle,detail

app_name="article"

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('addarticle/', addArticle, name="addarticle"),
    path('article/<int:id>', detail, name="detail"),

]