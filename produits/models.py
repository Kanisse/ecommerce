from django.db import models

# Create your models here.


class Category (models.Model):
      nom=models.CharField(max_length=200)
      def __str__(self):
        return f'{self.nom}' 
      
class Article (models.Model):
  nom=models.CharField(max_length=100)
  description=models.CharField(max_length=100)
  prix=models.IntegerField(max_length=20)
  category= models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
  def __str__(self):
    return f'{self.nom}'  
