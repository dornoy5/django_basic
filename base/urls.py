
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contact', views.contact),
    # path('products', views.products),
    path('prods', views.ProductViewSet.as_view()),
    path('prods/<pk>', views.ProductViewSet.as_view()),
    path('orders', views.orders),
]
