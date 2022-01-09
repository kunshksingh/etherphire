from django.urls import path
from . import views
from .models import *


urlpatterns = [
    path('', views.mainPage, name = 'mainPage'),
    path('poetry/', views.poetry, name = 'poetry'),
    path('poetry/preface/', views.preface, name = 'preface'),
    path('poetry/<str:poemname>/', views.poem, name='poem'),
    path('blog/', views.blog, name = 'blog'),
    path('automation/', views.automation, name = 'automation'),
   
    
]

