from django.db import models

# Create your models here.
class Article (models.Model):
  nom=models.CharField(max_length=100)
  description=models.CharField(max_length=100)
  prix=models.IntegerField(max_length=20)
  
  
  

