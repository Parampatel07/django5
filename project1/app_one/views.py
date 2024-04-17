from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
     print("this is home page ")
     return HttpResponse("This is home page ")