from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout

from home.models import UserProfile

# Create your views here.

def index (request):
    try:
        return render(request,'base.html')
    except Exception as e:
        print(e)
        return redirect(page404)
  
def login_user(request):
    try:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            if username != "" and password != "":
                query = authenticate(
                    request, username=username, password=password)
                if query is None:
                    messages.error(request, "Invalid Credentials")
                else:
                    login(request, query)
                    messages.success(request, 'Welcome To Pet Connect')
                    if UserProfile.objects.filter(user=request.user).exists():
                        return redirect(index)
                    else:
                        return redirect(addUserProfile)
            else:
                messages.warning(request, "Null Values are not allowed")
        return render(request, 'login.html')
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
 
def addUserProfile(request):
    try:
        if request.method == "POST":
            UserProfile.objects.create(user=request.user, username=request.user,profilepicture=request.FILES.get('profile'),user_type="normal", banner=request.FILES.get(
                'banner'), about=request.POST['about'], phone_number=request.POST['phone1'], phone_number_2=request.POST['phone2'], fb=request.POST['facebook'], twitter=request.POST['twitter'], insta=request.POST['instagram'])
            messages.info(request, "Data Updated Sccessfully")
            return redirect(index)
        return render(request, 'add_profile.html')
    except Exception as e:
        print(e)
        return redirect(page404)
 
@login_required(login_url='/login')
def user_profile(request):
    try:
        query = UserProfile.objects.filter(user=request.user)
        if query:
            return render(request, 'profile.html', {"query": query})
        else:
            return redirect(addUserProfile)
    except Exception as e:
        print(e)
        return redirect(page404)

def viewPublicProfile(request, username):
    try:
        query = UserProfile.objects.filter(username=username)
        return render(request, 'public_profile.html', {"query": query})
    except Exception as e:
        print(e)
        return redirect(page404)
  
def page404(request):
    return render(request, '404.html')