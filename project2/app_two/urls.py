from django.urls import path
from . import views 
from project2 import settings
from django.conf.urls.static import static

urlpatterns = [
     path("login",views.login,name="login"),
     path('home',views.home,name='home'),
     path('aboutus',views.aboutus,name='aboutus'),
     path("contactus",views.contactus,name="contactus"),
     path("home2",views.home2,name="home2"),
     path("teams",views.teams,name="teams"),
     path("profile/<str:name>",views.profile,name="profile"),
     path("calc/<int:number1>/<int:number2>",views.calc,name="calc"),
     path("students",views.students,name='students'),
     path("login2",views.login2,name='login2')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)