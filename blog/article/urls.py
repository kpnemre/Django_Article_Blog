from django.contrib import admin
from django.urls import path, include
from .views import dashboard,addArticle,detail,update,delete,articles,comment

app_name="article"

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('addarticle/', addArticle, name="addarticle"),
    path('article/<int:id>', detail, name="detail"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('', articles, name="articles"),
    path('comment/<int:id>', comment, name="comment"),
    

]