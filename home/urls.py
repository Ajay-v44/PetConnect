from django.urls import include, path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    # path("__reload__/", include("django_browser_reload.urls")),
    
]