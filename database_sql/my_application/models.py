from django.db import models

# Create your models here.
class data(models.Model):
    Name=models.CharField(max_length=20,default=' ')
    Age=models.IntegerField(default=' ')
    Address=models.CharField(max_length=20,default=' ')
   
    Mail=models.CharField(max_length=50,default=' ')