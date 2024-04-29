from django.urls import path 
from . import views
urlpatterns = [

     path("home",views.home,name="home"),
     path("template",views.template,name="template"),
     path("category",views.category,name="category"),
     path("register",views.register,name="register"),
     path("add_user",views.add_user,name="add_user"),
     path("login",views.login,name="login"),
     path("check_login",views.check_login,name="check_login"),
     path("change_password",views.change_password,name="change_password"),
     path("update_password",views.update_password,name="update_password"),
     path("product/<int:id>",views.view_product,name="product"),
     path("single_product/<int:id>",views.single_product,name="single_product"),
]