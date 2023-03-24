from django.db import models

class Owner(models.Model):
   
    name = models.CharField(max_length=100 , blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(blank=False , max_length=100)
    contact_number = models.CharField(blank=False , max_length=20)
    whatsapp_number = models.CharField(max_length=20 , blank=True)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=20)
    pin = models.IntegerField()
    country = models.CharField(max_length=20)
    pan_card_number = models.CharField(max_length=20 , blank=False , unique=True)
    date_of_entry = models.DateField(blank=False)

    def __str__(self):
        return f'{self.name}'


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
    business_pan = models.CharField(blank=False , max_length=15 , unique=True)
    business_gst_number = models.CharField(max_length=100)
    data_entered_on = models.DateField()

    def __str__(self):
        return f'{self.owned_by} - {self.business_name}'





    