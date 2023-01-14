


from django.urls import path,include
from produits.views import contact, home, lister, delete, create, store, edit, update
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('contact',contact, name='contact'),
    path('produits', lister),
    path('produits/<id>',delete),
    path('produits/create/', create),
    path('produits/create/store', store, name='store'),
    path ('produits/edit/<id>', edit),
    path('produits/update/', update)
]
