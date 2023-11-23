from django.http import JsonResponse
from django.shortcuts import render
import json
from django.contrib import messages

from .models import NewsletterSubscriber

def home(request):
    return render(request, "home.html", {'current_path': request.path})

def about(request):
    return render(request, "about.html", {'current_path': request.path})

def contact(request):
    return render(request, "contact.html", {'current_path': request.path})

def portfolio(request):
    return render(request, "portfolio.html", {'current_path': request.path})

def blog(request):
    return render(request, "blog.html", {'current_path': request.path})

def processSubscription(request):

    data = json.loads(request.body)

    name = data['name']
    email = data['email']

    try: # we try to get the user email from the database, if it exists we don't create it
        subscriber = NewsletterSubscriber.objects.get(email=email)
        messages.success(request, (f"{email} is already a subscriber!"))

        return JsonResponse('Email already subscribed!', safe=False)

    except :
        subscriber = NewsletterSubscriber.objects.create(name=name, email=email)
        subscriber.save()
        
        messages.success(request, (f"{email} subscribed successfully!"))
        return JsonResponse('Subscription success!', safe=False)