from django.contrib import admin
from .models import Orders , Product , Customer , Categories , Employee , SubCategory , ProductInventoryManagement ,Day_Wise_Employee_Management

admin.site.register(ProductInventoryManagement)
admin.site.register(Day_Wise_Employee_Management)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Orders)
admin.site.register(Categories)
admin.site.register(SubCategory)
admin.site.register(Employee)