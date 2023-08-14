from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import *
from .models2 import Category, Company, ItemMaster, ItemVariation, Owner , Sales, Business, StoreStock, storeMaster , BusinessInventoryMaster , storeInventoryMaster , OwnerDetails , Product , SalesPending,GenBill,SalesRegister , Customer , EmployeeMaster , TransactionDetailsMaster , ReturnSalesPending , EmployeeCredential , EmployeeAuth , SupplierMaster , PurchaseRegister , PurchasePending , PurchaseTransactionDetails , ReturnTransactionDetails

class StoreStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreStock
        fields = '__all__'
class ItemVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVariation
        fields = '__all__'
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'
class OwnerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Owner
        fields = '__all__'  
class ItemMasterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ItemMaster
        fields = '__all__'      
class BusinessSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Business
        fields = '__all__'
class StoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = storeMaster
        fields = '__all__'
class BusinessInventorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BusinessInventoryMaster
        fields = '__all__'
class StoreInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = storeInventoryMaster
        fields = '__all__'
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(trim_whitespace=False)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            # You can add any additional validation here, if needed.
            return data
        else:
            raise serializers.ValidationError("Username and password are required.")
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
class OwnerDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OwnerDetails
        fields = '__all__'
class ProductDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
class ProductMasterserBusinessializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'
class SalesPendingSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalesPending
        fields = '__all__'
class GenerateBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenBill
        fields = '__all__'
class SalesRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalesRegister
        fields = '__all__'
class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = '__all__'
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeMaster
        fields = '__all__'
class TransactionDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TransactionDetailsMaster
        fields = '__all__'
class ReturnSalesPendingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReturnSalesPending
        fields = '__all__'
class ReturnTransactionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnTransactionDetails
        fields = '__all__'
class EmployeeCredentialSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmployeeCredential
        fields = '__all__'
class EmployeeAuthSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmployeeAuth
        fields = '__all__'

class SupplierMasterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SupplierMaster
        fields = '__all__'

class PurchaseRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRegister
        fields = '__all__'

class PurchasePendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasePending
        fields = '__all__'

class PurchaseTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseTransactionDetails
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

