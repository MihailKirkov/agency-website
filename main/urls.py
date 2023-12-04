from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),
    path('process_subscription/', views.processSubscription, name='process_subscription'),
    path('terms-conditions/', views.about, name='terms-conditions'),
    path('privacy-policy/', views.about, name='privacy-policy'),
]
