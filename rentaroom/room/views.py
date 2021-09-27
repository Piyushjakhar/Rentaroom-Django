from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("You are at room's index!!")
    
def details(request, property_id):
    return HttpResponse("you are looking at the details page of property %s" %property_id)    