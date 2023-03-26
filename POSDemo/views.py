from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SubCategory , ProductInventoryManagement , Customer
from .models2 import Owner , Business
from .serializer import OwnerSerializer , BusinessSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from pprint import pprint
import json

'''
class SubCategoryGetView(APIView):
    def get(self , response):
        data = ProductInventoryManagement.objects.all()
        serializer = InventorySerializer(data , many=True)
        return Response(serializer.data)


@api_view(['GET' , 'POST'])
def handle_customer_view(request):
    if request.method == 'GET':
        customer_data = Customer.objects.all().values('name' , 'phone')
        serializer = CustomerSerializer(customer_data , many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        parser = JSONParser()
        
        if request.query_params:
            try:
                QUERY = request.query_params.dict()
                print(QUERY)
                print(type(QUERY))
                if 'name' in QUERY.keys():
                    if 'phone' in QUERY.keys():
                        customer_name = request.query_params.get('name')
                        customer_phone = request.query_params.get('phone')
                        
                        pprint(f"{customer_name} - {customer_phone}")
                        return Response("Done Bro")
            except Exception as e:
                return Response(e)
        else: 
            return Response('Nothing Bro')
    
'''
@api_view(['GET' , 'POST'])
def handle_owner(request):
    owner_email = request.query_params.get('userEmail')
    owner_pass = request.query_params.get('pass')
    if owner_email == None or owner_pass == None:
        return Response({'invalid input'})
    print(f'{owner_email}  ----------  {owner_pass}')
    if request.method == 'GET':
        owner_data = Owner.objects.filter(email =  owner_email)
        if len(owner_data) != 0:
            owner_data_dict = list(owner_data.values('name' , 'password'))
            owner_password_db = owner_data_dict[0]['password']
            print(owner_data_dict)
            if owner_pass == owner_password_db:
                print(owner_password_db)
                return Response({'auth' : 'success' , 'name':owner_data_dict[0]['name']})
            else:
                return Response({'auth failed'})
        elif len(owner_data) == 0:
            return Response({'no user'})
        
        

    if request.method == 'POST':
        data = request.data
        print(f'{data} ---------------------- {type(data)}')
        serializer = OwnerSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'id':serializer.instance.id})
        else:
            return Response({'Broo What u did?':serializer.errors})

@api_view(['GET' , 'POST'])        
def handle_business(request):
    if request.method == 'GET':
        business_data = Business.objects.all()
        serializer = BusinessSerializer(business_data, many=True)
        return Response(serializer.data) 
    
    if request.method == 'POST':
       
        data = request.data
        data_from_frontend = json.loads(data)
        serializer = BusinessSerializer(data = data_from_frontend)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'Bro what u looking for' : serializer.errors})

            
        