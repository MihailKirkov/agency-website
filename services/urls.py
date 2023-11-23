from django.urls import path
from . import views

urlpatterns = [
    path('copywriting/', views.copywriting, name='copywriting')
]
