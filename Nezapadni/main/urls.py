from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('story/', views.story, name='story'),
    path('contact/', views.contact, name='contact'),
    path('vision/', views.vision, name='vision'),
    path('courses/', views.courses, name='courses'),
    path('signup/', views.sign_up, name='sign_up'),  
    path('login/', views.login, name='login'),  
]
