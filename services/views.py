from django.shortcuts import render

def copywriting(request):
    return render(request, "copywriting.html", {'current_path': '/services/'})

def video_editing(request):
    return render(request, "video_editing.html", {'current_path': '/services/'})

def fixed_price_services(request):
    return render(request, "fixed_price_services.html", {'current_path': '/services/'})

def web_development(request):
    return render(request, "web_development.html", {'current_path': '/services/'})

def business_website_development(request):
    return render(request, "web_development.html", {'current_path': '/services/'})

def ecom_website_development(request):
    return render(request, "web_development.html", {'current_path': '/services/'})

def web_application_development(request):
    return render(request, "web_development.html", {'current_path': '/services/'})

def shopify_website_development(request):
    return render(request, "web_development.html", {'current_path': '/services/'})

def custom_requests(request):
    return render(request, "web_development.html", {'current_path': '/services/'})