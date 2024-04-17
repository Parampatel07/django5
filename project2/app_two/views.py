from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .forms import loginForm
# Create your views here.
def login(request):
     print("This is login page ")
     # print(request.value())
     return HttpResponse("Welcome to login page ")

def home(request):
     print("this is home page ")
     return HttpResponse("<h1>Home Page</h1><a href='aboutus'>Go to About us </a>")

def aboutus(request):
     print("This is about us ")
     return HttpResponse("<h1>About us </h1> <a href='home'>Go to Home page</a>")

def contactus(request):
     print("this is contact us ")
     return render(request,'contactus.html',{'phone':'9874563210' , 'email':'admin@gmail.com' , 'address' : 'ABC plot , XYZ Society , PQR city , LMN State , India'})

def home2(request):
     print("This is home page ") 
     return render(request,'home.html',{'name':"Param Patel" , "isLogin" : 1})

def teams(request):
     print("This is teams page ")
     player_info = [
    # Team 1
          {"name": "Player 1", "runs": 1024, "matches": 50, "team_name": "Team A"},
          {"name": "Player 2", "runs": 876, "matches": 45, "team_name": "Team A"},
          {"name": "Player 3", "runs": 734, "matches": 48, "team_name": "Team A"},
          {"name": "Player 4", "runs": 623, "matches": 42, "team_name": "Team A"},
          {"name": "Player 5", "runs": 511, "matches": 35, "team_name": "Team A"},
          {"name": "Player 6", "runs": 456, "matches": 38, "team_name": "Team A"},
          {"name": "Player 7", "runs": 389, "matches": 31, "team_name": "Team A"},
          {"name": "Player 8", "runs": 287, "matches": 25, "team_name": "Team A"},
          {"name": "Player 9", "runs": 211, "matches": 20, "team_name": "Team A"},
          {"name": "Player 10", "runs": 165, "matches": 15, "team_name": "Team A"},
          {"name": "Player 11", "runs": 102, "matches": 10, "team_name": "Team A"},
          
          # Team 2
          {"name": "Player A", "runs": 1120, "matches": 52, "team_name": "Team B"},
          {"name": "Player B", "runs": 935, "matches": 47, "team_name": "Team B"},
          {"name": "Player C", "runs": 803, "matches": 49, "team_name": "Team B"},
          {"name": "Player D", "runs": 694, "matches": 43, "team_name": "Team B"},
          {"name": "Player E", "runs": 587, "matches": 37, "team_name": "Team B"},
          {"name": "Player F", "runs": 512, "matches": 39, "team_name": "Team B"},
          {"name": "Player G", "runs": 438, "matches": 33, "team_name": "Team B"},
          {"name": "Player H", "runs": 319, "matches": 28, "team_name": "Team B"},
          {"name": "Player I", "runs": 244, "matches": 22, "team_name": "Team B"},
          {"name": "Player J", "runs": 178, "matches": 17, "team_name": "Team B"},
          {"name": "Player K", "runs": 113, "matches": 11, "team_name": "Team B"}
     ]
     return render(request,'teams.html',{'teams':player_info})

def profile(request,name):
     print("This is profile page ")
     print("My name is " , name)
     return render(request,'profile.html',{'name':name})

def calc(request,number1,number2):
     add = number1 + number2
     sub = number1 - number2
     division = number1 / number2
     return render(request,'calc.html',{'add':add,'sub':sub,'multi':mutli , 'division':division})

def students(request):
     print("")
     data = models.student.objects.all().values()
     print(data)
     return render(request,'students.html',{'student_data':data})

def login2(request):
     print('')
     loginform = loginForm
     return render(request,'login.html',{'form':loginform})