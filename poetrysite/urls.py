from django.urls import path
from . import views
from .models import *


urlpatterns = [
    path('', views.mainPage, name = 'mainPage'),
    path('poetry/', views.poetry, name = 'poetry'),
    path('poetry/preface/', views.preface, name = 'preface'),
    path('poetry/<str:poemname>/', views.poem, name='poem'),
    path('blog/', views.blog, name = 'blog'),
    path('blog/<int:month>/<int:day>/<int:year>', views.article, name = 'article'),
    path('automation/', views.automation, name = 'automation'),
   
    
]

