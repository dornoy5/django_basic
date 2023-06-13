from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Product,Order

from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import status

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# @api_view(['GET','post'])
# def products(request):
#     all_products=ProductSerializer(Product.objects.all(),many=True).data
#     return Response ( all_products)

class ProductViewSet(APIView):
    def get(self, request):
        my_model = Product.objects.all()
        serializer = ProductSerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def put(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        serializer = ProductSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

@api_view(['GET','post'])
def orders(request):
    all_orders=OrderSerializer(Order.objects.all(),many=True).data
    return Response ( all_orders)


def index(req):
    return HttpResponse('<h1>hello')


def about(req):
    return JsonResponse(f'about', safe=False)

def contact(req):
    return JsonResponse(f'contact', safe=False)