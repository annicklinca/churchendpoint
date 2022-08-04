from django.test import TestCase
from django.db import models

# Create your tests here.
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(max_length=255)
    location = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
   
  
    
    def _str_(self):
        return self.title 