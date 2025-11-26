# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),          # главная, имя 'home'
    path('story/', views.story, name='story'),   # /story/
    path('vision/', views.vision, name='vision'),# /vision/
    path('contact/', views.contact, name='contact'),  # /contact/
    path('parents/', views.parents, name='parents'),  # если нужно
]
