from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def call(request):
    return render(request, 'call.html')
