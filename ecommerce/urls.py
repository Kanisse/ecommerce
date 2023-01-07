

from django.urls import path
from produits.views import home, lister, delete, create, store

urlpatterns = [
    path('', home),
    path('produits', lister),
    path('produits/<id>',delete),
    path('produits/create/', create),
    path('produits/create/store', store, name='store')
]
