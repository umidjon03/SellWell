from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class SellerInfo(models.Model):
    pass


class Products(models.Model):
    title = models.CharField(max_length=50)
    type_prod = models.CharField(max_length=10, choices=[
        ('personal', _('personal')),
        ('business', _('business')), #The first element in each tuple is the actual value to be set on the model, and the second element is the human-readable name 

    ])
    decsription = models.TextField()
    price = models.FloatField()
    negotiable = models.BooleanField()
    image = models.ImageField()



class User(models.Model):
    pass


