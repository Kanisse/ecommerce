
from django.urls import path, include

urlpatterns = [
    path('', include('ecommerce.urls')),
    path('/produits', include('ecommerce.urls')),
    path('/produits/create', include('ecommerce.urls')),
    path('/store', include('ecommerce.urls')),
    
]
