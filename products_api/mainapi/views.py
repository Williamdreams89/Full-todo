from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    RetrieveAPIView, 
    UpdateAPIView, 
    DestroyAPIView
)

from products_api.models import Products
from .serializers import ProductSerializer


class ProductListView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteView(DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductCreateView(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer