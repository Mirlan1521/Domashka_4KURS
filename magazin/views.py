from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *


@api_view(['GET'])
def products_list(request):
    products = Product.objects.all()
    data = ProductSerializer(products, many=True).data
    return Response(data=data)


@api_view(['GET', 'PUT', 'DELETE'])
def products_item(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(data={'message': 'Продукт не найден'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        product.delete()
        return Response(data={"message": "Product is удален"})
    elif request.method == "PUT":
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        product.tags.set(request.data['tags'])
        return Response(data={'message': 'Product updated', 'product': ProductSerializer(product).data})

    data = ProductSerializer(product).data
    return Response(data=data)


@api_view(['GET'])
def product_reviews(request):
    products = Product.objects.all()
    data = ProductReviewSerializer(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def activ_tag_list_view(request):
    products = Product.objects.all()
    data = ProductActivTagSerializer(products, many=True).data
    return Response(data=data)
