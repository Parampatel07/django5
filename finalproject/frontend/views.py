from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . import models
# Create your views here.
def home(request):
     print("this is home page ")
     return render(request,"index.html")

def template(request):
     return render(request,"template.html")

def category(request):
     categoryData = models.category.objects.all().values()
     print(categoryData)
     return render(request,"category.html",{'data':categoryData})

def register(request):
     return render(request,'register.html')

def add_user(request):
     print('this is add_user')
     if request.method == "POST":
          print(request.POST)
          user_model = models.user.objects
          form = user_model.create(name=request.POST['name'],phone=request.POST['phone'],age=request.POST['age'],email=request.POST['email'],password=request.POST['password'])
          form.save()
     return redirect("/shop/login")

def login(request):
     return render(request,"login.html")

def check_login(request):
     if request.method == "POST":
          print(request.POST)
          data = models.user.objects.filter(email=request.POST['email'],password=request.POST['password']).values()
          if(len(data)==0):
               print("invalid login attempt ")
               return redirect("/shop/login?message=0")
          else:
               print("login successfully ")
               return redirect(f"/shop/home?id={data[0]['id']}")
     return HttpResponse('success')

def change_password(request):
     return render(request,"change_password.html")

def update_password(request):
     if request.method == "POST":
          print(request.POST)
     return HttpResponse("success")

def view_product(request,id):
     category_data = models.category.objects.filter(id=id).values()
     data = models.product.objects.filter(categoryid=id).values()
     print(data)
     return render(request,'product.html',{'data':data , 'category_name' : category_data[0]['name']})

def single_product(request,id):
     product_data = models.product.objects.filter(id=id).values()
     category_data = models.product.objects.filter(categoryid=product_data[0]['categoryid']).values()
     print(product_data)
     return render(request,'single_product.html',{'product_data':product_data , 'category_data':category_data})