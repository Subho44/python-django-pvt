from django.urls import path
from.views import home,add_product

urlpatterns = [
    path('',home, name='home'),
    path('add-product/',add_product,name='add_product'),
]