from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def index(request):
    now = datetime.now()

    return render(
        request,
        "Pizzerias/index.html", 
        {
            'title': "The Pizzeria",
            'message': "WELCOME TO THE PIZZERIA!",
            'content': "Nice to see you! It's " + now.strftime("%A, %d %B, %Y at %X")
        }
    )


def about(request):
    return render(
        request,
        "Pizzerias/about.html",
        {
            'title' : "About The Pizzeria",
            'content' : "Example app page for Django."
        }
    )