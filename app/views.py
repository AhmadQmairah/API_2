from django.shortcuts import render
import requests
from django.http import JsonResponse
# Create your views here.

def home(request):
    print("hello")
    url="https://api.github.com/events"
    response=requests.get(url).json()
    context={"response":response}
    
    return render(request, 'home.html', context)
    