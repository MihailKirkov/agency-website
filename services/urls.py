from django.urls import path
from . import views

urlpatterns = [
    path('copywriting/', views.copywriting, name='copywriting'),
    path('video_editing/', views.video_editing, name="video_editing"),
    path('fixed_price_websites/', views.fixed_price_services, name="fixed_price_services"),
    path('web_development/', views.web_development, name="web_development"),
    path('business_website_development/', views.business_website_development, name="business_website_development"),
    path('ecom_website_development/', views.ecom_website_development, name="ecom_website_development"),
    path('web_application_development/', views.web_application_development, name="web_application_development"),
    path('shopify_website_development/', views.shopify_website_development, name="shopify_website_development"),
    path('custom_requests/', views.custom_requests, name="custom_requests"),
]
