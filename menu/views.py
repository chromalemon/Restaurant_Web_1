from django.shortcuts import render
from .models import foodItem
from django.shortcuts import get_object_or_404

# Create your views here.

def main(request):
    return render(request, "menu.html",{
        "food": get_object_or_404(foodItem, food_name="Honey pancakes")
    })
                  