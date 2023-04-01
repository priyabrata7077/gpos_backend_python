from rest_framework import serializers
#from .models import ProductInventoryManagement , Product , Customer , Orders , Employee , Categories , SubCategory , Company , Brand
from .models2 import Owner , Business , storeMaster , BusinessInventoryMaster , storeInventoryMaster , OwnerDetails , Product


class OwnerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Owner
        fields = '__all__'        
    
class BusinessSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Business
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = storeMaster
        fields = ['store_name' , 'store_location' , 'associated_business']

class BusinessInventorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BusinessInventoryMaster
        fields = '__all__'

class StoreInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = storeInventoryMaster
        fields = '__all__'
        
class OwnerDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OwnerDetails
        fields = '__all__'

class ProductDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name' , 'MRP' , 'purchase_rate' , 'sale_rate' , 'gst']