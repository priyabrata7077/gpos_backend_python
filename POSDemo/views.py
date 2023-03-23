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
    if request.method == 'GET':
        owner_data = Owner.objects.all()
        serializer = OwnerSerializer(owner_data, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data
        serializer = OwnerSerializer(data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({'Broo What u did?'})        
        
        