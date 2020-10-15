# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from django.contrib.auth import views
from .views import registrarUsuarioView
urlpatterns = [
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/register', registrarUsuarioView.as_view(), name='register'),
    path('accounts/logout', views.LogoutView.as_view(), name='logout')
]
