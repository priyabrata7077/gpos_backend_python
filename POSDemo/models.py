from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=30)
    main_category = models.ManyToManyField(Categories , related_name='sub_category')

    def __str__(self):
        return self.name



class ProductInventoryManagement(models.Model):
    date_of_update = models.DateTimeField(primary_key=True , blank=False)
    product_name = models.CharField(max_length=50)
    quantity_choices = [
        ('GM' , 'Gram'),
        ('LT' , 'Litre'),
        ('UNIT' , 'Units')]

    quantity_type = models.CharField(max_length=10 , choices=quantity_choices , default=quantity_choices[2][0])
    quantity_added = models.IntegerField(blank=True)
    quantity_removed = models.IntegerField(blank=True)
    remaining_quantity = models.IntegerField(blank=False)

    def __str__(self):
        return self.name
    
    
class Company(models.Model):
    company_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.company_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=50)
    company = models.ForeignKey(Company , blank=True , on_delete=models.DO_NOTHING , null = True)

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    quantity_choices = [
        ('GM' , 'Gram'),
        ('LT' , 'Litre'),
        ('PIECE' , 'Pieces')
    ]
    product_name = models.CharField(max_length=100)
    product_quantity_type = models.CharField(max_length=10 , choices=quantity_choices , default=quantity_choices[2][0])
    product_price = models.IntegerField()
    product_quantity_in_inventory = models.IntegerField(blank=False , null=True)
    product_category = models.ForeignKey(Categories, related_name='product' , on_delete=models.DO_NOTHING)
    product_sub_category = models.ForeignKey(SubCategory , related_name = 'product_sub_category' , on_delete = models.DO_NOTHING , null = True)
    
    product_company = models.ForeignKey(Company , on_delete=models.DO_NOTHING , blank = True , null=True)
    product_brand = models.ForeignKey(Brand , on_delete=models.DO_NOTHING , null=True)
    def __str__(self):
        return f'{self.product_name} {self.product_quantity_type}' 


class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    adhaar = models.CharField(max_length=12)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50 , null=True , blank=True)
    address = models.CharField(max_length=200)
   
    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id = models.IntegerField(unique=True)
    order_created = models.DateTimeField()
    products = models.ManyToManyField(Product)
    total_order_price = models.IntegerField()
    customer_ordered = models.ForeignKey(Customer, related_name='customer_order', on_delete=models.DO_NOTHING , null=True)
    employee = models.ForeignKey(Employee , related_name='order_handler', on_delete=models.DO_NOTHING , null=True)
    def __str__(self):
        return f"{self.order_id} - {self.total_order_price}"



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
  

    
