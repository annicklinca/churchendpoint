from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Charity(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
   
    
    def _str_(self):
        return self.name 

class ChurchDonation(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
   
    
    def _str_(self):
        return self.name 