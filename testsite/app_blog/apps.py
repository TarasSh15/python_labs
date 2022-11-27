#app_blog/urls.py
from django.apps import AppConfig
from django.urls import path
from django.shortcuts import render
from django.contrib import admin


class AppBlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_blog'
