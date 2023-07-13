from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

#from .models import ProductInventoryManagement , Product , Customer , Orders , Employee , Categories , SubCategory , Company , Brand
from .models2 import Owner , Business , storeMaster , BusinessInventoryMaster , storeInventoryMaster , OwnerDetails , Product , SalesPending,GenBill,SalesRegister , Customer , EmployeeMaster , TransactionDetailsMaster , ReturnSalesPending , EmployeeCredential , EmployeeAuth , SupplierMaster , PurchaseRegister , PurchasePending , PurchaseTransactionDetails , ReturnTransactionDetails , Categories

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
        fields = '__all__'
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


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'