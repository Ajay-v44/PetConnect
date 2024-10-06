from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type=models.CharField(max_length=150)
    profilepicture = models.ImageField(
        upload_to='images', height_field=None, width_field=None, max_length=None)
    banner = models.ImageField(
        upload_to='images', height_field=None, width_field=None, max_length=None, blank=True)
    about = models.TextField()
    phone_number=models.CharField(max_length=150)
    phone_number_2=models.CharField(max_length=150,null=True,blank=True)
    twitter = models.CharField(max_length=150, blank=True)
    fb = models.CharField(max_length=150, blank=True)
    insta = models.CharField(max_length=150, blank=True)
    username = models.CharField(max_length=150,blank=True,null=True)
    def __str__(self):
        return f"{self.phone_number}"

    class Meta:
        db_table = 'UserProfile'


class Posts(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    post_type=models.CharField(max_length=50)
    image =  models.ImageField(
        upload_to='images', height_field=None, width_field=None, max_length=None, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)