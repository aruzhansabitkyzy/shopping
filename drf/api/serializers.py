from rest_framework import serializers
from .models import *

        
class CitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = City    
        fields = '__all__'
        depth = 1
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        depth = 1
        
class ProductsSerializer(serializers.ModelSerializer):
     categoryList = CategorySerializer(many=True, read_only=True)
     cityList = CitySerializer(many=True, read_only=True)
     class Meta:
        model = Products
        fields = '__all__'
        depth = 1

        

