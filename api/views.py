from rest_framework import generics
from products.models import Product
from .serializers import ProductSerializer


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
