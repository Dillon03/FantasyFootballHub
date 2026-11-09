from django.shortcuts import render

def home(request):
    return render(request, 'rosters/home.html')