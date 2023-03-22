
from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from POSDemo import views





urlpatterns = [
    path('admin/', admin.site.urls),
    path('sub-categories/' , views.SubCategoryGetView.as_view() , name='sub-categories'),
    path('customer' , views.handle_customer_view , name = 'customer')
]


