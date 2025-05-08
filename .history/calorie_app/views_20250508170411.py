from django.shortcuts import render, redirect
from .models import Food
from datetime import date

def home(request):
    foods = Food.objects.filter(added_at__date=date.today())
    total = sum(f.calories for f in foods)
    return render(request, 'calorie_tracker/home.html', {'foods': foods, 'total': total})

def add_food(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        calories = request.POST.get('calories')
        if name and calories:
            Food.objects.create(name=name, calories=int(calories))
    return redirect('home')

def delete_food(request, food_id):
    Food.objects.filter(id=food_id).delete()
    return redirect('home')

def reset_day(request):
    Food.objects.filter(added_at__date=date.today()).delete()
    return redirect('home')
