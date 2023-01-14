


from django.urls import path
from produits.views import  home, lister, delete, create, store, edit, update
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('produits', lister),
    path('produits/<id>',delete),
    path('produits/create/', create),
    path('produits/create/store', store, name='store'),
    path ('produits/edit/<id>', edit),
    path('produits/edit/update/<id>', update)
]
