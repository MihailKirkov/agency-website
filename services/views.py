from django.shortcuts import render

def copywriting(request):
    return render(request, "copywriting.html", {'current_path': '/services/'})