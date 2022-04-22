from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

import random
# Create your models here.
class User(AbstractUser):
    first_name     = models.CharField(default='User', max_length=25, null=True, blank=True)
    last_name      = models.CharField(default=str(random.randint(10000, 100000)), max_length=25, null=True, blank=True)
    community_name = models.CharField(max_length=45, null=True, blank=True)
    avatar         = models.ImageField(null=True, default="avatar.svg")
    zip_code       = models.IntegerField(null=True, blank=True)
    email          = models.EmailField(unique=True, null=True, blank=True)
    username       = models.CharField(max_length=25, null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

