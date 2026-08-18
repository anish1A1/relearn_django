from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    
    data = {"Data" : "Data"}
    render(request, 'home.html', {'data': data})
    