from django.shortcuts import render, HttpResponse

def hui(request):
    return HttpResponse("hello world")

def copywriting(request):
    return render(request, "copywriting.html")