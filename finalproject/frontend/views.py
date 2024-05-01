from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . import models
# Create your views here.
def home(request):
     print("this is home page ")
     categoryData = models.category.objects.all().values()
     print(categoryData)
     productData = models.product.objects.all().values()
     productData = productData[0:4]
     return render(request,"index.html",{'data':categoryData , 'productData' : productData})

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
               request.session['userid'] = data[0]['id']
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

def add_to_cart(request):
     if(request.session['userid'] == 0):
          return redirect('/shop/login')
     else:
          product_data = []
          merged_data = []
          cart_data = models.cart.objects.filter(userid=request.session['userid'],orderid=0).values()
          print(cart_data)
          for i in cart_data:
               product_data.append(models.product.objects.filter(id=i['productid']).values())
          print(product_data)
          # for i in product_data:
          #      print("---------------------------------------")
          #      print(i[0]['name'])
          #      print(i[0]['image'])
          index=  0
          for i in cart_data:
               i['product_name']= product_data[index][0]['name']
               i['product_image']= product_data[index][0]['image']
               i['product_id']= product_data[index][0]['id']
               index+=1
               # print(index)
               # print(i)
               merged_data.append(i)
          print("++++++++++++++++++++++++++++++++++++++++++++++++++")
          print(merged_data)
          total = 0 
          for  i in merged_data:
               total = total  + (i['price'] * i['quantity'])
     return render(request,"cart.html",{'cart_data':merged_data , 'total' : total})

def add_product_to_cart(request,id,price):
     print(request.session['userid'])
     userid = request.session['userid']
     print(id)
     print(price)
     cart_data = models.cart.objects.filter(userid=userid,productid=id).values()
     if(len(cart_data) >=1 ):
          print()
          cart_form = models.cart.objects.filter(userid=userid,productid=id).update(quantity=cart_data[0]['quantity'] + 1 )
     else:
          cart_form = models.cart.objects
          data = cart_form.create(userid=userid,productid=id,price=price,quantity=1,orderid=0)
          data.save()
     return redirect("/shop/add_to_cart")

def plus_quantity(request,productid):
     cart_data = models.cart.objects.filter(productid=productid,userid=request.session['userid']).values()
     cart_form = models.cart.objects.filter(productid=productid,userid=request.session['userid']).update(quantity=cart_data[0]['quantity'] + 1)
     return HttpResponse('0')

def minus_quantity(request,productid):
     cart_data = models.cart.objects.filter(productid=productid,userid=request.session['userid']).values()
     cart_form = models.cart.objects.filter(productid=productid,userid=request.session['userid']).update(quantity=cart_data[0]['quantity'] - 1)
     return HttpResponse('0')

def remove_from_cart(request,id):
     print("this is id " , id )
     models.cart.objects.filter(id=id).delete()
     return HttpResponse('0')

def checkout(request,amount):
     if request.method == "POST":
          checkout_form = models.orders.objects
          data = checkout_form.create(userid=request.session['userid'],amount=amount,address=request.POST['address'],state=request.POST['state'],city=request.POST['city'],description=request.POST['description'],mode_of_payment=request.POST['mode_of_payment'])
          data.save()
          orderid  =  models.orders.objects.latest('id')
          print("----------------------------------------------")
          orderid = orderid.id
          print(orderid)
          models.cart.objects.filter(orderid=0,userid=request.session['userid']).update(orderid=orderid)
          return redirect("/shop/home")
     return render(request,"checkout.html",{'total':amount})

def add_to_wishlist(request,productid):
     cart_form = models.wishlist.objects
     data = cart_form.create(userid=request.session['userid'],productid=productid)
     data.save()
     return redirect("shop/view_wishlist")


def view_wishlist(request):
     if(request.session['userid'] == 0):
          return redirect('/shop/login')
     else:
          product_data = []
          merged_data = []
          cart_data = models.wishlist.objects.filter(userid=request.session['userid']).values()
          print(cart_data)
          for i in cart_data:
               product_data.append(models.product.objects.filter(id=i['productid']).values())
          print(product_data)
          # for i in product_data:
          #      print("---------------------------------------")
          #      print(i[0]['name'])
          #      print(i[0]['image'])
          index=  0
          for i in cart_data:
               i['product_name']= product_data[index][0]['name']
               i['product_image']= product_data[index][0]['image']
               i['price']= product_data[index][0]['price']
               i['product_id']= product_data[index][0]['id']
               index+=1
               # print(index)
               # print(i)
               merged_data.append(i)
          print("++++++++++++++++++++++++++++++++++++++++++++++++++")
          print(merged_data)
     return render(request,'wishlist.html',{'merge_data':merged_data})

def remove_from_wishlist(request,id):
     print("this is id " , id )
     models.wishlist.objects.filter(id=id).delete()
     return HttpResponse('0')

def logout(request):
     request.session['userid'] = 0
     return redirect("/shop/login")

def profile(request):
     if(request.session['userid'] == 0):
          return redirect('/shop/login')
     else:
          data = models.user.objects.filter(id=request.session['userid']).values()
          order_data = models.orders.objects.filter(userid=request.session['userid']).values()
     return render(request,"profile.html",{'data':data , 'order_data':order_data})