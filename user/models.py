from django.db import models

from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from .manager import UserManager
# Create your models here.






class User(AbstractUser):


    otp = models.CharField(max_length=6,null=True,blank=True)
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name= models.CharField(max_length=255,null=True,blank=True)
    user_photo = models.FileField(null=True,blank=True,default='')
    gender= models.CharField(max_length=255,null=True,blank=True)
    mobile= models.BigIntegerField(null=True,blank=True)
    email= models.EmailField(unique=True,null=True,blank=True)
    dob= models.DateField(null=True,blank=True)
    status= models.BooleanField(null=True,blank=True,default=1)
    created_by= models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_by = models.DateField(auto_now=True,null=True,blank=True)
    otp = models.CharField(max_length=6,null=True,blank=True)
    username = None


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


    def __str__(self):
        return f"{self.email}"