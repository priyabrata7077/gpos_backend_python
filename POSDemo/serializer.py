from rest_framework import serializers
from .models import ProductInventoryManagement , Product , Customer , Orders , Employee , Categories , SubCategory , Company , Brand
from .models2 import Owner , Business


class OwnerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Owner
        fields = ['name', 'email' , 'password' , 'contact_number' , 'whatsapp_number', 'address' , 'city', 'pin' , 'country' , 'pan_card_number' , 'date_of_entry']
        
    
class BusinessSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Business
        fields = '__all__'
