
from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from POSDemo import views





urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login', views.handle_login , name = 'add-owner'),
    path('add-business' , views.handle_business , name='add-business' )
]


