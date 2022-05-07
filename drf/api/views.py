from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, viewsets
from .models import City, Category, Products
from .serializers import CitySerializer, CategorySerializer, ProductsSerializer
# Create your views here.
class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    def list(self, request):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
          city = get_object_or_404(self.queryset, pk=pk)
        except (TypeError, ValueError):
            raise Http404
        else: 
            serializer = self.get_serializer(city)
            return Response(serializer.data)
        
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def list(self, request):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
          category = get_object_or_404(self.queryset,pk=pk)
        except (TypeError, ValueError):
            raise Http404
        else: 
            serializer = self.get_serializer(category)
            return Response(serializer.data)

    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    def list(self, request, category_pk = None):
        self.queryset = Products.objects.filter(category__id = category_pk)
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, category_pk = None , pk = None):
        try:
          city = get_object_or_404(self.queryset, category__pk = category_pk, pk = pk)
        except (TypeError, ValueError):
            raise Http404
        else: 
            serializer = self.get_serializer(city)
            return Response(serializer.data)
    
    def create(self, request):
        product_data= request.data
        new_product = Products.objects.create(product_name = product_data['product_name'], description = product_data['description'],
                                              price = product_data['price'],image = product_data['image'],
                                              upload_data = product_data['upload_data'], discount = product_data['discount'],
                                              category = product_data['category'])
        new_product.save()
        serializer  = self.get_serializer(new_product)
        return Response(serializer.data)
        
    def update(self, request, pk=None):
        product_data = request.data
        updating_product = Products.objects.get(id=pk)
        
        updating_product['product_name'] = product_data['product_name']
        updating_product['description'] = product_data['description']
        updating_product['price'] = product_data['price']
        updating_product['image'] = product_data['image']
        updating_product['upload_data'] = product_data['upload_data']
        updating_product['discount'] = product_data['discount']
        updating_product['category'] = product_data['category']
        
        updating_product.save()
        serializer = self.get_serializer(updating_product)
        return Response(serializer.data)
        
        
        
    