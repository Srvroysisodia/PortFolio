from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Home(models.Model):
    name = models.CharField(max_length=50)
    photo = CloudinaryField('image',null=True)
    proffession = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    
class Skills(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_percentage = models.IntegerField()

class Language(models.Model):
    Language_name = models.CharField(max_length=50)
    Language_percentage = models.IntegerField()
    
    
class WorkExp(models.Model):
    position = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    date_joined = models.DateField()
    date_leave = models.DateField(blank=True,null=True)
    remarks = models.TextField(max_length=500)
        
    

class Education(models.Model):
    school_name = models.CharField(max_length=100)
    date_joined = models.DateField()
    date_leave = models.DateField()
    degree = models.CharField(max_length=100)