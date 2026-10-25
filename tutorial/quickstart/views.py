from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSeriallizer


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSeriallizer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSeriallizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET','PUT','DELETE'])
def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
         return Response(
            {"error": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = ProductSeriallizer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSeriallizer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': f'product with {id} updated.'})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    elif request.method == 'DELETE':
        product.delete()
        return Response(
            {"message": "Product deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )

@api_view(['GET'])
def health_check(request):
    return Response({'message': "Health OK"})
