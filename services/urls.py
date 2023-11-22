from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('hui', views.hui, name='hui'),
    path('copywriting/', views.copywriting, name='copywriting')
]
