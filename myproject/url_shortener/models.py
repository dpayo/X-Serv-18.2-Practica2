from django.db import models

# Create your models here.

class Table( models.Model):
    url= models.CharField(max_length= 200)
 
    
