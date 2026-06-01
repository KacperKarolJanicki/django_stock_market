from django.shortcuts import render, redirect, HttpResponse
from .models import *

def index(request):
    featured_cars = Car.objects.all()
    global current_model

    if request.method == "POST":
        return redirect("current_model")
    return render(request, "home.html", {"featured_cars":featured_cars})

def configure_model(request, model_name, image, base_price):
    colors = Color.objects.all()
    engines = Engine.objects.all()
    equipment = Equipment.objects.all()

    if request.method == "POST":
        color = request.POST.get("color")
        engine = request.POST.get("engine")
        current_equipment = request.POST.get("equipment")
        chosen_opitons = [base_price]

        # Cars colors changing. Remember that the name of image file
        # must be the same like a model name value!

        if color == "Grey":
            image = f"{model_name} {color}.png"
        elif color=="Blue":
            image = f"{model_name} {color}.png"
        elif color == "Yellow":
            image = f"{model_name} {color}.png"

        if current_equipment == "Premium +":
            chosen_opitons.append(10000)
        elif current_equipment == "S-line":
            chosen_opitons.append(50000)
        
        if engine == "2.0":
            chosen_opitons.append(5000)
        elif engine == "2.5":
            chosen_opitons.append(7500)
        elif engine == "3.0":
            chosen_opitons.append(10000)
        
        final_price = sum(chosen_opitons)

        return render(request, 
                  "current_model.html", 
                  {"model":model_name, 
                   "image":image, 
                   "price":final_price, 
                    "equipment": equipment, 
                   "colors":colors,
                   "engines":engines,
                   "current_engine":engine,
                   "current_color": color,
                   "current_equipment": current_equipment
                   })
    
    return render(request, 
                  "current_model.html", 
                  {"model":model_name, 
                   "image":image, 
                   "price":base_price,
                   "equipment": equipment, 
                   "colors":colors,
                   "engines":engines})

def about(request):
    return render(request, "about.html")

def base(request):
    return render(request, "base.html")

def contact(request):
    return render(request, "contact.html")

def models_cars(request):
    featured_cars = Car.objects.all()
    return render(request, "models.html", {"cars":featured_cars})
