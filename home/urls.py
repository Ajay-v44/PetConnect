from django.urls import include, path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('login/',login_user,name='login'),
    path('register/',register_user,name='register'),
    path('add_profile/',addUserProfile,name='add_profile'),
    path('my_profile/',user_profile,name='my_profile'),
    path('public_profile/<str:username>/',viewPublicProfile,name='public_profile'),
    path('page404/',page404,name='page404'),
    
]