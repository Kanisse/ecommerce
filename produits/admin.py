from django.contrib import admin

# Register your models here.
from produits.models import Article, Category

admin.site.register(Article)
admin.site.register(Category)

