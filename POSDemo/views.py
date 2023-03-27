from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
from .models import SubCategory, ProductInventoryManagement, Customer
from .models2 import Owner, Business, auth
from .serializer import OwnerSerializer, BusinessSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from pprint import pprint
import json
import string
import secrets
import hashlib


def pass_encrypt(password):
    hash_obj = hashlib.sha256(password.encode())
    pass_crypt = hash_obj.hexdigest()
    return pass_crypt


def gen_token():
    choices = string.ascii_letters + string.digits
    token = ''.join((secrets.choice(choices) for i in range(32)))
    return token


@api_view(['GET', 'POST'])
def handle_login(request):
        user_agent = request.META
        print(f'{user_agent} -------- {type(user_agent)}')
        if request.method == 'POST':
            
            login_data = request.data
            login_data_dict = dict(login_data)
            if 'email' in login_data_dict.keys():
                print(
                    f'{login_data_dict["email"]} -------- {type(login_data_dict)}')
                user_name = login_data_dict['username'][0]
                email = login_data_dict['email'][0]
                passwd = login_data_dict['password'][0]
                print(f'{user_name} ------- {email} ------- {passwd}')
                data_from_db = Owner.objects.filter(name=user_name)
                if len(data_from_db) == 0:
                    return Response({'no user'})
                else:
                    data_from_db_values = list(
                        data_from_db.values('name', 'email', 'password'))
                    if email != data_from_db_values[0]['email'] and passwd != data_from_db_values[0]['password']:
                        return Response({'invalid email and password'})
                    if email != data_from_db_values[0]['email']:
                        return Response({'Invalid Email'})
                    if passwd != data_from_db_values[0]['password']:
                        return Response({'invalid password'})

                    # checking the the user has already been logged in with the token
                    # checking if the user is already in the auth db.
                    check_user_in_auth = list(auth.objects.filter(user_email = email).values('token'))

                    if len(check_user_in_auth) == 0:
                        user_token = gen_token()
                        user_auth = auth(user_name=data_from_db_values[0]['name'], user_email=data_from_db_values[0]['email'], token=user_token)
                        user_auth.save()
                        return Response({'auth': 'success', 'token': user_token})
                    else:
                        
                        print(check_user_in_auth[0]['token'])
                        return Response({'user': 'validated' , 'token':check_user_in_auth[0]['token']})
            if 'token' in login_data_dict.keys():
                checK_token = auth.objects.filter(token = login_data_dict['token'][0]).values('user_name')
                if len(checK_token) == 0:
                    return Response({'invalid token'})
                else:
                    user_of_token = list(checK_token)[0]['user_name']
                    return Response({'token' : 'valid' , 'user': user_of_token })
                

       








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

            
        