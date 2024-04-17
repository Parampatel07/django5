from django.shortcuts import render
from django.shortcuts import HttpResponse
from . import models
# Create your views here.
def home(request):
     return HttpResponse("Hello world ")

def calc(request):
     return render(request,'calc.html')


def result(request):
     print("------------------")
     num1 = int(request.GET['num1'])
     num2 = int(request.GET['num2'])
     answer = num1 + num2 
     print(answer)
     return render(request,'result.html',{'result' : answer})

def calc2(request):
     print("----------------------")
     return render(request,'calc2.html')

def result_post(request):
     print("------------------")
     num1 = int(request.POST['num1'])
     num2 = int(request.POST['num2'])
     option = request.POST['option']
     print("the value of num1 is " , num1 , "num2 is ",num2 , "option is ", option)
     if option == 'Addition':
          answer = num1 + num2
     elif option == 'Subtraction':
          answer = num1 - num2
     elif option == 'Multiplication':
          answer = num1 * num2
     elif option == 'Division':
          answer = num1 / num2 
     return render(request,'result.html',{'result':answer})

def add_category(request):
     if request.method == "POST":
          print("")
          name = request.POST['name']
          total = request.POST['total']
          description = request.POST['desc']
          image = request.FILES
          print(request.POST)
          print(request.FILES)
          form = models.category(name=name,total=total,photo=image['image'],description=description)
          form.save()
     
     data = models.category.objects.all().values()
     print(data)
     return render(request,'add_category.html',{'data':data})