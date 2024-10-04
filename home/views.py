from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index (request):
    try:
        return render(request,'base.html')
    except Exception as e:
        print(e)
        return redirect(page404)
  
def login_user(request):
    try:
        return render(request,'login.html')
    except Exception as e:
        print(e)
        return redirect(page404)  
     
def register_user(request):
    try:
        if request.method == "POST":
            messages.warning(request, 'Username / Email already exists')
            
            print("post")
            if User.objects.filter(email=request.POST['regemail']).exists() or User.objects.filter(username=request.POST['username']).exists():
                messages.warning(request, 'Username / Email already exists')
            else:
                if request.POST['password'] != request.POST['repeat_password']:
                    messages.warning(request, 'Passwords dont match')
                else:
                    query = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], username=request.POST[
                        'username'], email=request.POST['regemail'], password=request.POST['password'])
                    query.set_password(request.POST['password'])
                    query.save()
                    messages.success(request, 'User Created Successfully')
                    return redirect(login_user)
        return render(request,'register.html')
    except Exception as e:
        print(e)
        return redirect(page404)  
 
        
def page404(request):
    return render(request, '404.html')