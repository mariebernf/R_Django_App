from django.shortcuts import render, HttpResponse
from . import models

recipes = [
    {
        'author': 'Dom',
        'title': 'meatball sub',
        'directions': 'combine all ingredients',
        'date_posted': 'May 19, 2022',
    },
    {
        'author': 'Dom',
        'title': 'turkey sub',
        'directions': 'combine all ingredients',
        'date_posted': 'May 10, 2022',
    },
    {
        'author': 'Dom',
        'title': 'ham & cheese sub',
        'directions': 'combine all ingredients',
        'date_posted': 'May 07, 2022',
    },
]

# Create your views here.
def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/home.html", context)

def about(request):
    return render(request, "recipes/about.html", {'title':'about us page'})
