
from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from POSDemo import views





urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login', views.handle_login , name = 'add-owner'),
    path('add-business' , views.handle_business , name='add-business' ),
    path('add-owner' , views.handle_owner , name = 'add-owner' ),
    path('add-store' , views.handle_store , name = 'add-store'),
    path('business-inventory' , views.handle_business_inventory , name = 'business-inventory-management' ),
    path('store-inventory' , views.handle_store_inventory , name = 'store-inventory-management'),
    path('add-owner-details' , views.handle_owner_details , name='Handle-Owner-Details'),
    path('handle-customer' , views.handle_customer_details , name='get-customer-details'),
    path('handle-products' , views.handle_products_data , name = 'handle-products-data'),
    path('sales-pending' , views.handle_sales_pending , name = 'handle-sales-pending'),
    path('generate-bill' , views.handle_sales_register , name = 'generate-bill-and-handle-sales-register')
]


