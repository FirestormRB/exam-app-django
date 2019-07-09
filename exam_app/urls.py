from django.contrib import admin
from django.urls import path
from .views import LoginView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(), name = "login"),
    path('index', views.index, name = "index"),
]
