from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name     = models.CharField(max_length=25, null=True)
    last_name      = models.CharField(max_length=25, null=True)
    community_name = models.CharField(max_length=45, null=True)
    # avatar         = models.ImageField()
    zip_code       = models.IntegerField(null=True)
    email          = models.EmailField(unique=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

