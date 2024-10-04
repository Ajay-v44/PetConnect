from django.urls import include, path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('login/',login_user,name='login')
    
]