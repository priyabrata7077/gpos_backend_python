from django.db import models

'''class Owner(models.Model):
    name = models.CharField(max_length=100 , blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=10 , blank=False)
    whatsapp = models.CharField(max_length=10 , blank=True)
    password = models.CharField(max_length=66)

class OwnerDetails(models.Model):
    owner_id = models.ForeignKey(Owner , on_delete=models.DO_NOTHING , related_name='details')
    pan = models.CharField(max_length=10 , blank=False)
    city = models.CharField(max_length=20 , blank=False)
    state = models.CharField(max_length=20 , blank=False)
    pin_code = models.CharField(max_length=6 , blank=False)
    country = models.CharField(max_length=20 , blank=False)
'''


    
    
    
    






















'''
class Day_Wise_Employee_Management(models.Model):
    date = models.DateField()
    employee_name = models.OneToOneField(Employee , related_name='Day_Wise_employee' , on_delete=models.DO_NOTHING , null=True)
    designation_for_the_day = models.CharField(max_length=30)
    time_of_joining = models.DateTimeField()
    cash_collected = models.IntegerField()
    time_of_leaving = models.DateTimeField()
    orders_handled = models.ForeignKey(Orders , on_delete=models.DO_NOTHING)


class Wastage(models.Model):
    product_name = models.ForeignKey(Product , on_delete=models.DO_NOTHING)
    quantity_type = models.CharField(max_length=10)
    wasted_amount = models.IntegerField()
    date_entered = models.DateField()
    reason = models.CharField(max_length=200)


class Item_Return_Management(models.Model):
    product_name = models.CharField(max_length=50)
    customer_returned = models.ForeignKey(Customer , on_delete=models.DO_NOTHING , null=True)
    employee_handled = models.ForeignKey(Employee , on_delete=models.DO_NOTHING)
    date_and_time_of_return = models.DateTimeField()
    reson_for_return = models.CharField(max_length=200)
'''  

    
