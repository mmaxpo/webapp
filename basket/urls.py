from django.urls import path
from basket.views import *

urlpatterns = [
    path('list/', product_list, name='list'),
    path('detail/<int:pk>/', product_detail, name='detail'),
    path('add/', add_to_basket, name='add_to_cart'),
]

