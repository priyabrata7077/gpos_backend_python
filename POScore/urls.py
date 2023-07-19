
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from POSDemo import views


def test_decorator(func):
    
    print('Running decorator')
    def wrapper(*args, **kwargs):
        result_from_api = args[0]
        print(f'result from api is {result_from_api}')
        result = func(*args, **kwargs)
        return result
    return wrapper()


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #path('', include('myapp.urls')),
    path('login', views.handle_login , name = 'add-owner'),
    path('logout' , views.handle_logout , name='logout'  ),
    
    
    path('add-business' , views.handle_business , name='add-business' ),
    path('add-owner' , views.handle_owner , name = 'add-owner' ),
    path('add-store' , views.handle_store , name = 'add-store'),
    
    #paths not to be given importance ri8 now
    path('business-inventory' , views.handle_business_inventory , name = 'business-inventory-management' ),
    
   
    
    path('add-owner-details' , views.handle_owner_details , name='Handle-Owner-Details'),
    path('handle-customer' , views.handle_customer_details , name='get-customer-details'),
    path('handle-products' , views.handle_products_data , name = 'handle-products-data'),
    
    
    path('sales-pending' , views.handle_sales_pending , name = 'handle-sales-pending'),
    path('generate-bill' , views.handle_sales_register , name = 'generate-bill-and-handle-sales-register'),
    path( 'transaction-details' , views.handle_transaction_details , name = 'handle-transaction-details' ),
    path('business/store/get' , views.get_all_stores_from_business_id , name='all-stores-under-the-business-id'),
    path('business/store/add' , views.add_store_under_business_id , name='all-stores-under-the-business-id'),
    
    #paths for the master inputs
    path('business/product-master' , views.handle_product_master , name = 'add-product-in-business' ),
    
    #paths for adding elements in a store under a business
    
    path('business/store/supplier/add' , views.handle_supplier , name = 'add-aupplier'),
    path('business/employee/update/<int:pk>', views.UpdateBusinessEmployee.as_view(), name='update-employee-in-store'),
    path('business/employee/add' , views.add_business_employee.as_view() , name = 'add-employee-in-store'),
     path('business/employee/delete/<int:pk>',views.delete_business_employee.as_view(), name = 'delete-employee-in-store'),
    path('business/store/inventory' , views.add_product_in_the_store_inventory, name = 'add-products-in-the-store-inventory'),
    path('business/store/products/return' , views.handle_product_return , name = 'manage-return-from-customer-in-a-store' ),
    path('business/store/products/return/transaction' , views.handle_product_return_transaction , name = 'manage-return-transaction-customer-in-a-store' ),
    
    path('business/store/employee/signup' , views.handle_employee_signup , name = 'employee-signup' ),
    path('business/store/employee/login' , views.handle_employee_login , name = 'employee-login' ),
    
    path('business/store/purchase/pending' , views.purchase_pending , name = 'handle-purchase-pending' ),
    path('business/store/purchase/register' , views.purchase_register , name = 'handle-purchase-register' ),
    path('business/store/purchase/transaction' , views.handle_purchase_transaction , name = 'handle-purchase-transaction' ),
    path('business/store/products/category/add' , views.handle_product_categories , name='add-product-categories')

    #path('handle-business/store-inventory' , views.handle_store_inventory , name = 'handle-store-inventory')
]


