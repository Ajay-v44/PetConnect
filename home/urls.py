from django.urls import include, path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('login/',login_user,name='login'),
    path('register/',register_user,name='register'),
    path('add_profile/',addUserProfile,name='add_profile'),
    path('page404/',page404,name='page404')
    
]