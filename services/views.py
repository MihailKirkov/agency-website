from django.shortcuts import render

def copywriting(request):
    return render(request, "copywriting.html", {'current_path': '/services/'})

def video_editing(request):
    return render(request, "video_editing.html", {'current_path': '/services/'})

def fixed_price_websites(request):
    return render(request, "fixed_price_websites.html", {'current_path': '/services/'})

def web_development(request):
    return render(request, "web_development.html", {'current_path': '/services/'})