from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to my Recipes App!</h1>")

def about(request):
    return HttpResponse("<h1>This is a recipes app to keep track of your recipes</h1>")
