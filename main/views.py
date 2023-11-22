from django.http import JsonResponse
from django.shortcuts import render
import json
from django.contrib import messages

from .models import NewsletterSubscriber

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def portfolio(request):
    return render(request, "portfolio.html")

def blog(request):
    return render(request, "blog.html")

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