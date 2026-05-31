from django.shortcuts import render, redirect, HttpResponse
from .models import *

current_model = None

def index(request):
    featured_cars = Car.objects.all()
    global current_model

    if request.method == "POST":
        current_model = request.POST.get("model")
        return redirect("current_model")
    return render(request, "home.html", {"featured_cars":featured_cars})

def configure_model(request, model_name, image, base_price):
    colors = Color.objects.all()
    engines = Engine.objects.all()
    if request.method == "POST":
        color = request.POST.get("color")
        if color == "Grey":
            image = f"{model_name} Grey.png"
        elif color=="Blue":
            image = f"{model_name} Blue.jpg"
        elif color == "Yellow":
            image = f"{model_name} Yellow.png"
        return render(request, 
                  "current_model.html", 
                  {"model":model_name, 
                   "image":image, 
                   "price":base_price, 
                   "colors":colors,
                   "engines":engines})
    return render(request, 
                  "current_model.html", 
                  {"model":model_name, 
                   "image":image, 
                   "price":base_price, 
                   "colors":colors,
                   "engines":engines})

def about(request):
    return render(request, "about.html", {"model":current_model})

def base(request):
    return render(request, "base.html")

def contact(request):
    return render(request, "contact.html")

def models_cars(request):
    featured_cars = Car.objects.all()
    return render(request, "models.html", {"cars":featured_cars})
