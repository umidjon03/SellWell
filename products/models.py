from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import User

# Create your models here.
class SellerInfo(models.Model):
    pass


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Product(models.Model):
    title          = models.CharField(max_length=50)
    type_prod      = models.CharField(max_length=10) # , choices=[
    #     ('personal', _('personal')),
    #     ('business', _('business')), #The first element in each tuple is the actual value to be set on the model, and the second element is the human-readable name 
    # ])
    decsription    = models.TextField()
    category       = models.ForeignKey(Category, null=True ,on_delete=models.SET_NULL)
    price          = models.FloatField()
    negotiable     = models.BooleanField()
    image          = models.ImageField()
    seller         = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_name   = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    email          = models.EmailField()
    address        = models.TextField()
    
    def __str__(self):
        return self.title