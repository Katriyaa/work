from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('', view=views.index),  # 默认主页
    path('login/', view=views.login),
    path('home/', view=views.home),


]
