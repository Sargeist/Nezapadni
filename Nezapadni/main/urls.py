from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('story/', views.story, name='story'),
    path('vision/', views.vision, name='vision'),
]
