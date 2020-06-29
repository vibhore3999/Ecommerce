from django.shortcuts import render



# Create your views here.
from django.http import HttpResponse
def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return render(request, 'shop/about.html')

def  contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return HttpResponse("we are at tracker")

def search(request):
    return HttpResponse("we are at search")

def productview(request):
    return HttpResponse("we are at product view")

def checkout(request):
    return HttpResponse("we are at checkout")



