from django.urls import path
from shipping.views import *

urlpatterns = [
    path('list/', shipping_list, name='shipping-list'),
    path('add/', shipping_create, name='shipping-create')
]
