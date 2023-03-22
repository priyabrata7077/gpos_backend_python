from rest_framework import serializers
from .models import ProductInventoryManagement , Product , Customer , Orders , Employee , Categories , SubCategory , Company , Brand



class InventorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductInventoryManagement
        fields = ['name' , 'quantity_type' , 'quantity']


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields ='__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubCategory
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ['name' , 'phone']