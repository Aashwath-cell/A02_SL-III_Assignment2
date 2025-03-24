from django.shortcuts import render

def home(request):
    return render(request, 'app1/home.html')

def sample(request):
    return render(request, 'app1/sample.html')