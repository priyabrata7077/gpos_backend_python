from django.db import models

class Owner(models.Model):
   
    name = models.CharField(max_length=100 , blank=False)
    email = models.EmailField(blank=False , unique=True)
    password = models.CharField(blank=False , max_length=100 , unique=True)
    contact_number = models.CharField(blank=False , max_length=10)
    whatsapp_number = models.CharField(max_length=10 , blank=True)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=20)
    pin = models.CharField(max_length=6)
    country = models.CharField(max_length=20)
    pan_card_number = models.CharField(max_length=10 , blank=False , unique=True)
    date_of_entry = models.DateField(blank=False)

    def __str__(self):
        return f'{self.name} - {self.pk}'


class Business(models.Model):
    
    owned_by = models.ForeignKey(Owner , related_name='business' , blank=False , null=True , on_delete=models.DO_NOTHING)
    business_name = models.CharField(max_length=50 , blank=False)
    business_email = models.EmailField(blank=True)
    business_phone = models.CharField(blank=True , max_length=12)
    business_address = models.CharField(blank=False , max_length=300)
    business_city = models.CharField(max_length=20)
    business_pin = models.IntegerField()
    business_state = models.CharField(max_length=20)
    business_country = models.CharField(max_length=10)
    business_pan = models.CharField(blank=False , max_length=10 , unique=True)
    business_gst_number = models.CharField(max_length=15)
    data_entered_on = models.DateField()

    def __str__(self):
        return f'{self.owned_by} - {self.business_name} - {self.pk}'

class storeMaster(models.Model):
    
    store_name = models.CharField(max_length=100 , blank=False)
    store_location = models.CharField(max_length=200 , blank=False)
    associated_business = models.ForeignKey(Business , related_name='business' , on_delete=models.DO_NOTHING)
    def __str__(self):
        return f'{self.store_name} + {self.associated_business}'

class auth(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100 , null=True , blank=False )
    user_ip = models.CharField(blank=True , max_length=20)
    token = models.CharField(max_length=32 , blank=False)
    token_expiry = models.CharField(blank=True , null=True , max_length=200)
    def __str__(self):
        return f'{self.user_name} - {self.token} '

     
#Component models of sales Products , Inventory , Category , Brand

class BusinessInventoryMaster(models.Model):
    updated_at = models.DateTimeField()
    product_name = models.CharField(max_length=150)
    product_quantity_type = models.CharField(max_length=5 , choices=[('GM' , 'gram') , ('PIECE' ,'pieces') , ('LTR' ,'litre')])
    product_quantity = models.CharField(max_length=20)
    action = models.CharField(max_length=7 , choices=[('ADDED' ,'product added') , ('REMOVED' , 'product removed')] , null=True)
    price_per_unit = models.CharField(max_length=10 , null=True)
    associated_business = models.OneToOneField(Business , on_delete=models.DO_NOTHING , null=True)

    def __str__(self):
        return f'{self.product_name} + {self.action} + {self.associated_business}'

   
class storeInventoryMaster(models.Model):
    updated_at = models.DateTimeField()
    product_name = models.CharField(max_length=100)
    product_quantity_type = models.CharField(max_length=5 , choices=[('GM' , 'gram') , ('PIECE' ,'pieces') , ('LTR' ,'litre')] )
    product_quantity = models.CharField(max_length=20)
    action = models.CharField(max_length=7 , choices=[('ADDED' ,'product added') , ('REMOVED' , 'product removed')] , null=True)
    price_per_unit = models.CharField(max_length=10 , null=True)
    associated_store = models.OneToOneField(storeMaster , on_delete=models.DO_NOTHING , null=True)
    
    def __str__(self):
        return f'{self.product_name} - {self.associated_store}'





