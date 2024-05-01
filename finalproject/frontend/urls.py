from django.urls import path 
from . import views
urlpatterns = [

     path("home",views.home,name="home"),
     path("template",views.template,name="template"),
     path("category",views.category,name="category"),
     path("register",views.register,name="register"),
     path("add_user",views.add_user,name="add_user"),
     path("login",views.login,name="login"),
     path("logout",views.logout,name="logout"),
     path("profile",views.profile,name="profile"),
     path("check_login",views.check_login,name="check_login"),
     path("change_password",views.change_password,name="change_password"),
     path("update_password",views.update_password,name="update_password"),
     path("product/<int:id>",views.view_product,name="product"),
     path("single_product/<int:id>",views.single_product,name="single_product"),
     path("add_to_cart",views.add_to_cart,name="add_to_cart"),
     path("view_wishlist",views.view_wishlist,name="view_wishlist"),
     path("add_product_to_cart/<int:id>/<int:price>",views.add_product_to_cart,name="add_product_to_cart"),
     path("plus_quantity/<int:productid>",views.plus_quantity,name="plus_quantity"),
     path("minus_quantity/<int:productid>",views.minus_quantity,name="minus_quantity"),
     path("remove_from_cart/<int:id>",views.remove_from_cart,name="remove_from_cart"),
     path("remove_from_wishlist/<int:id>",views.remove_from_wishlist,name="remove_from_wishlist"),
     path("checkout/<int:amount>",views.checkout,name="checkout"),
     path("add_to_wishlist/<int:productid>",views.add_to_wishlist,name="add_to_wishlist"),
]