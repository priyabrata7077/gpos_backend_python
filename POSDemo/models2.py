from django.db import models



class Sales(models.Model):
#     # business_id = models.ForeignKey(Business, on_delete=models.CASCADE)
#     transaction_id = models.ForeignKey(TransactionDetail, on_delete=models.CASCADE)
#     item_master_id = models.ForeignKey(ItemMaster, on_delete=models.CASCADE)
#     item_variation_id = models.ForeignKey(ItemVariation, null=True, blank=True, on_delete=models.CASCADE)
#      customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING , related_name='sales')
 #   store_id = models.ForeignKey(storeMaster, on_delete=models.CASCADE)  # Connecting to storeMaster model
#     store_stock_id = models.ForeignKey(StoreStock, on_delete=models.CASCADE)
      
    qty = models.PositiveIntegerField()
    purchase_rate = models.DecimalField(max_digits=10, decimal_places=2)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    sale_rate = models.DecimalField(max_digits=10, decimal_places=2)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Owner(models.Model):
    username = models.CharField(max_length=100 , blank=False)
    email = models.EmailField(blank=False , unique=True)
    password = models.CharField(blank=False , max_length=100 , unique=True)
    contact_number = models.CharField(blank=False , max_length=10)
    whatsapp_number = models.CharField(max_length=10 , blank=True)

    date_of_entry = models.DateField(blank=False)

    def __str__(self):
        return f'{self.username} - {self.pk}'
class OwnerDetails(models.Model):
    owner_id = models.ForeignKey(Owner , on_delete=models.DO_NOTHING , related_name='details')
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=20)
    pin = models.CharField(max_length=6)
    country = models.CharField(max_length=20)
    pan_card_number = models.CharField(max_length=10 , blank=False , unique=True)
    date_of_entry = models.DateField()
    
    def __str__(self):
        return f'Details of {self.owner_id}'
    
class Business(models.Model):
            
    owner_id = models.ForeignKey(Owner , related_name='business' , blank=False , on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50 , blank=False)
    email = models.EmailField(blank=True)
    phone = models.CharField(blank=True , max_length=12)
    address = models.CharField(blank=False , max_length=300)
    city = models.CharField(max_length=20)
    pin = models.CharField(max_length=6)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=10)
    pan = models.CharField(blank=False , max_length=10 , unique=True)
    gst_number = models.CharField(max_length=15)
    date_of_entry = models.DateField()

    def __str__(self):
        return f'{self.owner_id} - {self.name} - {self.pk}'

class storeMaster(models.Model):
    
    store_name = models.CharField(max_length=100 , blank=False)
    store_location = models.CharField(max_length=200 , blank=False)
    associated_owner = models.ForeignKey(Owner , on_delete=models.DO_NOTHING, related_name = 'store')
    associated_business = models.ForeignKey(Business , related_name='store' , on_delete=models.DO_NOTHING)
    def __str__(self):
        return f' store ID - {self.pk} ->> {self.store_name} + {self.associated_business}'

class auth(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100 , null=True , blank=False )
    user_ip = models.CharField(blank=True , max_length=20)
    token = models.CharField(max_length=32 , blank=False)
    token_expiry = models.DateTimeField(blank=True , null=True)
    def __str__(self):
        return f'{self.user_name} - {self.token} '


class JwtAuth(models.Model):
    jwt = models.CharField(max_length=300)
    expiry = models.DateTimeField()

    def __str__(self):
        return f'{self.jwt} jwt ID -> {self.pk}'

class Permission(models.Model):
    permission = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.permission}'

class Roles(models.Model):
    role = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    permissions = models.ManyToManyField(Permission , related_name='roles')
    def __str__(self):
        return f'{self.role} - {self.description}'

class EmployeeMaster(models.Model):
    
    name = models.CharField(max_length=100 , )
    email = models.EmailField()
    phone = models.CharField(max_length=10 ,unique=True)
    address = models.CharField(max_length=200 , )
    adhaar = models.CharField(max_length=12 , unique=True)
    #business = models.ForeignKey(Business , on_delete=models.DO_NOTHING , related_name='employee')
   
    
    def __str__(self):
        return self.name


class EmployeeCredential(models.Model):
    employee = models.ForeignKey(EmployeeMaster , related_name='credential' , on_delete=models.DO_NOTHING)
    username = models.CharField(max_length=100  , blank=False , unique=True , null = True)
    password = models.CharField(unique=True , max_length=100 , blank=False)
    modified_on = models.DateTimeField()
    
    def __str__(self):
        return f'{self.employee} - {self.password}> '


class EmployeeAuth(models.Model):
    employee = models.ForeignKey(EmployeeMaster , on_delete=models.DO_NOTHING , related_name='authentication')
    business = models.ForeignKey(Business , related_name='employee_auth' , on_delete=models.DO_NOTHING , null=True)
    jwt = models.CharField(max_length=300)
    have_access = models.BooleanField()

    def __str__(self):
        return f'{self.employee} | Have Acces -> {self.have_access}'
# =============================================================================================================

class Customer(models.Model):
    name = models.CharField(max_length=100 , blank=False)
    contact = models.CharField(max_length=10 , unique=True , blank=False) 
    address = models.CharField(max_length=200 , blank=False )
    store = models.ForeignKey(storeMaster , on_delete=models.DO_NOTHING , related_name='customer')
    
    
class TaxMaster(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return f' {self.name} - {self.pk}'



class Categories(models.Model):
    name = models.CharField(max_length=100)
    parent = models.CharField(max_length=100 , blank=True)
    store = models.ForeignKey(storeMaster , related_name='category' , on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f'Name -> {self.name} | Parent -> {self.parent} | store -> {self.store}'



class Product(models.Model):
    name = models.CharField(max_length=100)
    MRP = models.CharField(max_length=20)
    purchase_rate = models.CharField(max_length=20)
    sale_rate = models.CharField(max_length=20)
    gst = models.ForeignKey(TaxMaster , related_name='product' , on_delete=models.DO_NOTHING)
    hsn = models.CharField(max_length=7 , null=True , blank=True)
    quantity_type = models.CharField(max_length=5 , choices=[('GM' , 'gram') , ('PIECE' ,'pieces') , ('LTR' ,'litre') , ('MTR' , 'meter') ] , null=True)
    #store = models.ForeignKey(storeMaster , related_name='product' , on_delete=models.DO_NOTHING , blank=True)
    business = models.ForeignKey(Business , related_name='products' , on_delete=models.DO_NOTHING , null=True )
    variable = models.BooleanField(null=True)
    category = models.ForeignKey(Categories , related_name='product' , on_delete=models.DO_NOTHING , null=True)
    def __str__(self):
        return f'{self.name} - {self.pk}'
 

class VariableProduct(models.Model):
    parent_product =  models.ForeignKey(Product , related_name='variableproduct' , on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    MRP = models.CharField(max_length=20)
    purchase_rate = models.CharField(max_length=20)
    sale_rate = models.CharField(max_length=20)
    gst = models.ForeignKey(TaxMaster , related_name='variableproduct' , on_delete=models.DO_NOTHING)
    hsn = models.CharField(max_length=7 , null=True , blank=True)
    quantity_type = models.CharField(max_length=5 , choices=[('GM' , 'gram') , ('PIECE' , 'pieces') , ('LTR' , 'litre') , ('MTR' , 'meter')])
    
# ==============================================================================================================
'''
class EmployeeSalary(models.Model):
    salary = 
'''

     
#Component models of sales Products , Inventory , Category , Brand
class BusinessInventoryMaster(models.Model):
    updated_at = models.DateTimeField()
    product = models.ForeignKey(Product , related_name='businessinventory' , on_delete=models.DO_NOTHING , null=True)
    #product_quantity_type = models.CharField(max_length=5 , choices=[('GM' , 'gram') , ('PIECE' ,'pieces') , ('LTR' ,'litre')])
    available = models.CharField(max_length=20)
    #action = models.CharField(max_length=7 , choices=[('ADDED' ,'product added') , ('REMOVED' , 'product removed')] , null=True)
    
    associated_business = models.ForeignKey(Business , on_delete=models.DO_NOTHING , null=True)

    def __str__(self):
        return f'{self.product} + {self.associated_business}'

   
class storeInventoryMaster(models.Model):
    updated_at = models.DateTimeField()
    #store_owner = models.ForeignKey(Owner , on_delete=models.DO_NOTHING , null=True)
    business = models.ForeignKey(Business , on_delete=models.DO_NOTHING , related_name = 'storeinventory' , null=True)
    
    product = models.ForeignKey(Product , on_delete=models.DO_NOTHING , related_name='storeinventory' , null=True)
    available  = models.CharField(max_length=100 , null=True)
    #action = models.CharField(max_length=7 , choices=[('ADDED' ,'product added') , ('REMOVED' , 'product removed')] , null=True)
    
    associated_store = models.ForeignKey(storeMaster , on_delete=models.DO_NOTHING , null=True , related_name='storeinventory')
    
    def __str__(self):
        return f'{self.product} - {self.associated_store}'


class InventoryManager(models.Model):
    updated_at = models.DateTimeField()
    product = models.ForeignKey(Product , related_name='inventorymanager' , on_delete=models.DO_NOTHING)
    action = models.CharField(max_length=1 , choices=[('A' , 'added') , ('R' ,'removed')] )
    quantiy = models.CharField(max_length=100)
    store = models.ForeignKey(storeMaster , related_name='inventorymanager' , on_delete=models.DO_NOTHING)
    reason = models.CharField(max_length=100)
    
    def __str__(self):
        return f'Product - {self.product} has been {self.action}'
    


#Sales page components  ,  Barcode , stock register , sales pending , Sales Register , Transaction Details


class ModeOfPayment(models.Model):
    name = models.CharField(max_length=20)
    business = models.ForeignKey(Business , related_name='mop' , on_delete=models.DO_NOTHING , null=True)
    def __str__(self):
        return f'{self.name} -> {self.pk}'


class Barcode(models.Model):
    barcode = models.CharField(max_length=50)
    product = models.ForeignKey(Product , related_name='barcode' , on_delete=models.DO_NOTHING , null=True)
    store = models.ForeignKey(storeMaster , related_name='barcode' , on_delete=models.DO_NOTHING , null=True)
    def __str__(self):
        return f'{self.barcode} - Product -> {self.product} '


class GenBill(models.Model):
    bill_id = models.CharField(max_length=100)
    time = models.DateTimeField()
    store = models.ForeignKey(storeMaster , on_delete=models.DO_NOTHING , related_name='bill')


    def __str__(self):
        return f' Bill_pk -> {self.pk}| Bill_id {self.bill_id} -> {self.store} '

class TransactionDetailsMaster(models.Model):
    bill_id = models.ForeignKey(GenBill , on_delete=models.DO_NOTHING , related_name = 'transactiondetails')
    date_of_entry = models.DateTimeField()
    business = models.ForeignKey(Business , related_name='transactiondetails' , on_delete=models.DO_NOTHING)
    store = models.ForeignKey(storeMaster , related_name='transactiondetails' , on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(EmployeeMaster , on_delete=models.DO_NOTHING , related_name='transactiondetails')
    mop = models.JSONField()
    products = models.JSONField()
    
    def __str__(self):
        return f' EM -> {self.employee} | store -> {self.store}'
    
   




class SalesRegister(models.Model):
    bill_no = models.CharField(max_length=100 , null=True)
    bill_ID = models.ForeignKey(GenBill , related_name='salesregister' , on_delete=models.DO_NOTHING)
    business = models.ForeignKey(Business , on_delete=models.DO_NOTHING , related_name='salesregister')
    store = models.ForeignKey(storeMaster , on_delete=models.DO_NOTHING , related_name='salesregister' )
    employee = models.ForeignKey(EmployeeMaster , on_delete=models.DO_NOTHING , related_name='salesregister' , null=True)
    product = models.ForeignKey(Product , on_delete=models.DO_NOTHING , related_name='salesregister' ,null=True)
    gst = models.ForeignKey(TaxMaster , on_delete=models.DO_NOTHING , related_name='salesregister')
    customer = models.ForeignKey(Customer , related_name='salesregister', on_delete=models.DO_NOTHING , blank=True , null=True)
    
    item_barcode = models.CharField(max_length=100 , blank=True) #To be implemented later bro
    
    
    product_quantity = models.CharField(max_length=100)
    
    
    #product_name = models.CharField(max_length=100 , null =True)
    mrp = models.CharField(max_length=50 ,null =True)
    purchase_rate = models.CharField(max_length=50, null =True)
    sale_rate = models.CharField(max_length=20 ,null =True)
    #row_total = models.CharField(max_length=100, null =True)
    
    def __str__(self):
        return f' salesReg_pk -> {self.pk} | {self.bill_ID} '




class SalesPending(models.Model):
    #id specific inputs
    bill_id = models.ForeignKey(GenBill, on_delete=models.DO_NOTHING , related_name='salespending' , null=True)
    business = models.ForeignKey(Business , related_name='salespending' , on_delete=models.DO_NOTHING )
    store = models.ForeignKey(storeMaster , on_delete=models.DO_NOTHING ,  related_name='salespending')
    employee = models.ForeignKey(EmployeeMaster , on_delete=models.DO_NOTHING , related_name='salespending')
    product = models.ForeignKey(Product , on_delete=models.DO_NOTHING , related_name= 'salespending')
    gst = models.ForeignKey(TaxMaster , on_delete=models.DO_NOTHING , related_name='salespending' )
    #input from form
    
    product_quantity = models.CharField(max_length=20)
    
    #calculated inputs 
    
    product_name = models.CharField(max_length=100)
    mrp = models.CharField(max_length=20 , null=True)
    purchase_rate = models.CharField(max_length=20)
    sale_rate = models.CharField(max_length=20)
    row_total = models.CharField(max_length=20) 
    customer = models.ForeignKey(Customer , on_delete=models.DO_NOTHING , related_name='salespending' , blank=True , null=True)
    def __str__(self):
        return f' sales pending pk = {self.pk} | {self.product} -> TOTAL -> {self.row_total} '


class SalesReturnRegister(models.Model):
    bill_no = models.CharField(max_length=100 , null=True)
    #bill_ID = models.ForeignKey(GenBill , related_name='salesreturn' , on_delete=models.DO_NOTHING)
    business = models.ForeignKey(Business , on_delete=models.DO_NOTHING , related_name='salesreturn')
    store = models.ForeignKey(storeMaster , on_delete=models.DO_NOTHING , related_name='salesreturn' )
    employee = models.ForeignKey(EmployeeMaster , on_delete=models.DO_NOTHING , related_name='salesreturn' , null=True)
    
    '''    
    product_structure = {
        'product_id':'2',
        'product_name':'ching',
        'mrp':'100',
        'purchase_rate':'90',
        'sale_rate':''
        'return_reason':'broken_or_some_shit_bro'
    }
    '''    
    
    product = models.JSONField(null=True)
    
    #gst = models.ForeignKey(TaxMaster , on_delete=models.DO_NOTHING , related_name='salesreturn')
    customer = models.ForeignKey(Customer , related_name='salesreturn', on_delete=models.DO_NOTHING , blank=True , null=True)
    
    item_barcode = models.CharField(max_length=100 , blank=True) #To be implemented later bro
    
    
    quantity_returned = models.CharField(max_length=100)
    
    
    
    #mrp = models.CharField(max_length=50 ,null =True)
    #purchase_rate = models.CharField(max_length=50, null =True)
    #sale_rate = models.CharField(max_length=20 ,null =True)
    #row_total = models.CharField(max_length=100, null =True)
    
    def __str__(self):
        return f'{self.bill_no} - {self.customer.name}'    

class ReturnTransactionDetails(models.Model):
    bill_id = models.CharField(max_length=100)
    date_of_entry = models.DateTimeField()
    business = models.ForeignKey(Business , related_name='returntransaction' , on_delete=models.DO_NOTHING)
    store = models.ForeignKey(storeMaster , related_name='returntransaction' , on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(EmployeeMaster , on_delete=models.DO_NOTHING , related_name='returntransaction')
    mop = models.ForeignKey(ModeOfPayment , related_name='returntransactiondetails' , on_delete=models.DO_NOTHING , null=True)
    #product = models.ForeignKey(Product , related_name='returntransactiondetails' , on_delete=models.DO_NOTHING , null=True)
    amount = models.CharField(max_length=100 , null=True)
    #reason = models.CharField(max_length=100 , blank=True , null=True)
    
    def __str__(self):
        return f' EM -> {self.employee} | store -> {self.store}'    

class SupplierMaster(models.Model):
    date_of_entry = models.DateTimeField()
    name = models.CharField(max_length=100)
    store = models.ForeignKey(storeMaster , related_name='supplier' , on_delete=models.DO_NOTHING , null=True)
    
    def __str__(self):
        return f'{self.name} | pk -> {self.pk}'

class ReturnSalesPending(models.Model):
    date_of_entry = models.DateTimeField()
    bill_ID = models.ForeignKey(GenBill , on_delete=models.DO_NOTHING , related_name = 'returnsalespending')
    business = models.ForeignKey(Business, on_delete=models.DO_NOTHING , related_name='returnsalespending')
    store = models.ForeignKey(storeMaster , on_delete=models.DO_NOTHING , related_name='returnsalespending')
    employee = models.ForeignKey(EmployeeMaster , null=True , on_delete=models.DO_NOTHING , related_name = 'returnsalespending')
    product = models.ForeignKey(Product , on_delete=models.DO_NOTHING , related_name = 'returnsalespending')
    customer = models.ForeignKey(Customer , related_name='returnsalespending' , on_delete=models.DO_NOTHING , blank=True , null=True)
    return_quantity = models.CharField(max_length=50 , null=True)
    def __str__(self):
        return f'{self.date_of_entry} | {self.bill_ID} | {self.customer}'



class PurchaseBill(models.Model):
    created_at = models.DateTimeField()
    bill_id = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.bill_id}'
    

class PurchasePending(models.Model):
    date_and_time = models.DateTimeField(null=True)
    supplier = models.ForeignKey(SupplierMaster , related_name = 'purchasepending' , on_delete=models.DO_NOTHING )
    products = models.ForeignKey(Product , related_name='purchasepending' , on_delete=models.DO_NOTHING , null=True)
    quantity = models.CharField(max_length=20)
    purchase_rate = models.CharField(max_length=100)
    store = models.ForeignKey(storeMaster , related_name='purchasepending' , on_delete=models.DO_NOTHING , null=True)
    total = models.CharField(max_length=100 , null=True)
    
    def __str__(self):
        return f'{self.supplier.name} | {self.products} | {self.quantity}'


class PurchaseRegister(models.Model):
    bill_id = models.CharField(max_length=100 , null=True)
    date_and_time = models.DateTimeField()
    supplier = models.ForeignKey(SupplierMaster , on_delete=models.DO_NOTHING , related_name = 'prchaseregister')
    '''
    product_structure = {
        'product_id':'5'
        "product_name":'ching',
        'product_quantity':'133',
        'product_:''
    }
    '''
    
    products = models.ForeignKey(Product , related_name = 'purchaseregister' , on_delete=models.DO_NOTHING)
    
    quantity = models.CharField(max_length=20)
    purchase_rate = models.CharField(max_length=100 , null=True)
    store = models.ForeignKey(storeMaster , related_name='purchaseregister' , on_delete=models.DO_NOTHING , null=True)
    total = models.CharField(max_length=100 , null=True)
    def __str__(self):
        return f" BILL_ID -> {self.bill_id}  | supplier_id ->  {self.supplier.pk} name-> {self.supplier.name} | {self.products} + {self.quantity}"
    
class PurchaseTransactionDetails(models.Model):
    bill_id = models.CharField(max_length=100 , null = True)
    supplier_id = models.ForeignKey(SupplierMaster , related_name='purchasetransaction' , on_delete=models.DO_NOTHING , null=True)
    date_of_entry = models.DateTimeField()
    #related_purchase = models.ForeignKey(PurchaseRegister , on_delete=models.DO_NOTHING , related_name = 'purtransactiondetails')
    mop = models.JSONField()
    
    def __str__(self):
        return f' {self.date_of_entry} -- {self.bill_id} '


    
class EmployeeAttendance(models.Model):
    date = models.DateField()
    employee = models.ForeignKey(EmployeeMaster , on_delete=models.DO_NOTHING , related_name='attendance')
    store = models.ForeignKey(storeMaster , on_delete=models.DO_NOTHING , related_name='employeeAttendance')
    
    time_of_entry = models.TimeField()
    
    time_of_relief = models.TimeField()
    
    def __str__(self):
        return f' {self.date} ->  {self.employee} -> {self.store} '

'''int
class PurchaseRegister:
    pass

class CategoriesMaster(models.Model):
    name = models.CharField()
'''




'''
class RolesHasPermission(models.Model):
    pass
'''


    


class Daily_employee_management(models.Model):
    date = models.DateField()
    employee = models.ForeignKey(EmployeeMaster , related_name = 'dailymanager' , on_delete=models.DO_NOTHING)
    designation = models.CharField(max_length=100)
    store = models.ForeignKey(storeMaster , related_name='dailymanager' , on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f'{self.employee} , {self.designation}'


