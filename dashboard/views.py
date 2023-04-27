from django.shortcuts import render,redirect
from django import request
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def home(request):
     return render(request, 'home.html')
 
def register(request):
     if request.method == 'POST':
         first_name = request.POST['first_name']
         last_name = request.POST['last_name']
         username = request.POST['username']
         email =request.POST['email']
         password = request.POST['password']
         confirm_password = request.POST['confirm_password']
     if password==confirm_password:
       if User.objects.filter(username=username).exists():
         messages.info(request, 'Username already exists ')
         return redirect(register)     
     else:
      user = User.objects.create_user(username=username,password=password, email=email, first_name=first_name, last_name=last_name) 
      user.set_password(password) 
      user.save()
      print("success")
     return redirect('login_user') 


     else:
     print("this is not post method")
     return render(request, 'register.html')

def login_user(request):
      if request.method == 'POST':
       email =request.POST['email']
      password = request.POST['password']
      user = auth.authenticate(email=email, password=password)

      if user is not None:
       auth.login(request, user)
      return redirect('home')
 
 
      else:
      messages.info(request, 'Invalid Email or Password')
      return redirect('login_user')
 
      else:
      return render(request, 'login.html')

def logout_user(request):
    auth.logout(request)
    return redirect('home') 
 
