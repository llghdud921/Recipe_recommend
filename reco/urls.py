from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "reco"

urlpatterns = [

    path('', views.mainpage, name='mainpage'),
    path('result/', views.result, name='result'),
    path("detail/<int:recipe_id>", views.detail, name = "detail"),

]