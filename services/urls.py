from django.urls import path
from . import views

urlpatterns = [
    path('copywriting/', views.copywriting, name='copywriting'),
    path('video_editing/', views.video_editing, name="video_editing"),
    path('fixed_price_websites', views.fixed_price_websites, name="fixed_price_websites"),
    path('web_development', views.web_development, name="web_development"),
    
]
