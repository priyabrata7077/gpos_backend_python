from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
from .models import SubCategory, ProductInventoryManagement, Customer
from .models2 import Owner, Business, auth
from .serializer import OwnerSerializer, BusinessSerializer , StoreSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from pprint import pprint
from datetime import datetime, timezone
import json
import string
import secrets
import hashlib
import json

#Custom Helper Functions ########################################################################
def pass_encrypt(password):
    hash_obj = hashlib.sha256(password.encode())
    pass_crypt = hash_obj.hexdigest()
    return pass_crypt


def gen_token():
    choices = string.ascii_letters + string.digits
    token = ''.join((secrets.choice(choices) for i in range(32)))
    return token

def clean_dict_to_serialize(data_dict):
    for i in data_dict.keys():
        data_dict[i] = data_dict[i][0]
    
    return data_dict
def expiry_time_calc(seconds_to_add):
    dt_obj = datetime.today()
    time_now_in_seconds = dt_obj.timestamp()
    expt_time = int(time_now_in_seconds)+seconds_to_add
    
    return expt_time

def check_token_expiry(token_expiry_from_db):
    #token_expiry_from_db = float(token_expiry_from_db)  
    timestamp_now = expiry_time_calc(0)
    print(f'{token_expiry_from_db} ------------ >>>>>>>>>>>>>>>>>>> -------------')
    print(f'{timestamp_now} ------- ================= ------------ ')
    
    exp_time_rev = timestamp_now - token_expiry_from_db
    exp_dif = token_expiry_from_db - timestamp_now  
    
    print()
    print('))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
    print(exp_dif)
    print()
    print('((((((((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))))))))')
    if exp_dif <= 0:
        return False
    else:
        return True

def check_token_validity(token_from_response , need_business_id=True):
    token = auth.objects.filter(token = token_from_response).values('user_name' , 'token_expiry' , 'user_password' )
    
    print(token)
    if len(token) != 0:
        token_expiry = list(token)[0]['token_expiry']
        print(f'{token} found bro')
        token_list = list(token)
        print(token_list)
        user_id_of_the_token = Owner.objects.filter(name = token_list[0]['user_name'] , password = token_list[0]['user_password'] ).values('pk')
        user_id_of_the_token = str(list(user_id_of_the_token)[0]['pk'])
        print(f'{user_id_of_the_token} +++++++++++++++++++++++++++++++++++++++++++++++++++')
        if need_business_id:
            associated_business_id = Business.objects.filter(owned_by = user_id_of_the_token).values('pk')
            print('----------------------------------------------------')
            print(f'{user_id_of_the_token} -- {associated_business_id}')
            print('----------------------------------------------------')
            return True , token_expiry , str(list(associated_business_id)[0]['pk'])
        if need_business_id == False:
            return True , token_expiry , user_id_of_the_token
    else:
        return False , None , None
        


#################################################################################################

# token data in header 'HTTP_AUTHORIZATION': 'Bearer oEYOaVC955Onygsp3jjNmNQ8NTFUEDcv'
@api_view(['GET', 'POST'])
def handle_login(request):
        header_info = request.META
        ip_of_host_from_header = header_info['REMOTE_ADDR']
        #print(f'{header_info} -------- {type(header_info)}')
        print('-------------------------------------------------------------------')
        if request.method == 'POST':
            if 'HTTP_BEARER_TOKEN' in header_info.keys():
                check_token_queryset = auth.objects.filter(token=header_info['HTTP_BEARER_TOKEN'])
                checK_token = auth.objects.filter(token=header_info['HTTP_BEARER_TOKEN']).values('user_name' , 'token_expiry')
                print(f'{checK_token} ------- queryset')
                #print(int(checK_token[0]['token_expiry']))
                if len(checK_token) == 0:
                    return Response({'invalid token'})
                else:
                    token_check_condition = check_token_expiry(int(checK_token[0]['token_expiry']))
                    print(f'{token_check_condition} ----- True hai bro')
                    if  token_check_condition == True:
                        
                        user_of_token = list(checK_token)[0]['user_name']
                        return Response({'token' : 'valid' , 'user': user_of_token })
                    else:
                        check_token_queryset.delete()
                        return Response({'Token Validity': ' Expired', 'token deleted' : True})
                '''              
            if 'HTTP_BEARER_TOKEN' not in header_info.keys():
                return Response({'No valid token found '})
                pass    
                '''

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
                        user_token_expiry = expiry_time_calc(86400)
                        user_auth = auth(user_name=data_from_db_values[0]['name'], user_email=data_from_db_values[0]['email'], token=user_token , token_expiry = user_token_expiry , user_ip = ip_of_host_from_header , user_password = passwd)
                        user_auth.save()
                        return Response({'auth': 'success', 'token': user_token})
                    else:
                        
                        print(check_user_in_auth[0]['token'])
                        return Response({'user': 'validated' , 'token':check_user_in_auth[0]['token']})
'''            
            if 'token' in login_data_dict.keys():
                checK_token = auth.objects.filter(token = login_data_dict['token'][0]).values('user_name')
                if len(checK_token) == 0:
                    return Response({'invalid token'})
                else:
                    user_of_token = list(checK_token)[0]['user_name']
                    return Response({'token' : 'valid' , 'user': user_of_token })
'''                

       
@api_view(['GET' , 'POST'])        
def handle_business(request):
    if request.method == 'GET':
        business_data = Business.objects.all()
        serializer = BusinessSerializer(business_data, many=True)
        return Response(serializer.data) 
    
    if request.method == 'POST':
       
        data = request.data
        print(data)
        data_dict = dict(data)
        print(data_dict)
        
        #here I'm fist getting the owner data from the Owner model with .filter method and getting its primary_key with .values method which gives a dictionary in then converting the whole thing into a list slicing it at the zeroth index wich gives us the data dictionary {'pk' : int_value}.
        owner_pk_from_db = list(Owner.objects.filter(name=data_dict['owned_by'][0]).values('pk'))[0]['pk']
        print(owner_pk_from_db)
        data_dict['owned_by'] = [f'{owner_pk_from_db}']
        print(data_dict)
        
        #converting the modified python dict back to json data
        clean_data_dict = clean_dict_to_serialize(data_dict)
        print(clean_data_dict)
        #data_dict['owned_by'] = Owner.objects.filter(name=data_dict['owned_by']).values('pk')
        
        #data_from_frontend = json.loads(data)
        serializer = BusinessSerializer(data = clean_data_dict)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            serializer_error_dict = dict(serializer.errors)
            error_list_for_response =[]
            for error in serializer_error_dict.keys():
                error_list_for_response.append(serializer_error_dict[error][0])
            return Response({'error':error_list_for_response})

            
@api_view(['POST'])
def handle_owner(request):
    if request.method =='POST':
        header_info = request.META
        ip_of_host_from_header = header_info['REMOTE_ADDR']
        data = request.data
        
        print(f'{data} ============================================= {type(data)}')
        serializer = OwnerSerializer(data = data)
        if serializer.is_valid():
            user_token = gen_token()
            user_token_expiry = expiry_time_calc(30)
            user_auth = auth(user_name=data['name'], user_email=data['email'], token=user_token , token_expiry = user_token_expiry , user_ip = ip_of_host_from_header)
            user_auth.save()
            serializer.save()
            return Response({'user added':True , 'generated token':user_token})
        else:
            serializer_error_dict = dict(serializer.errors)
            error_list_for_response =[]
            for error in serializer_error_dict.keys():
                error_list_for_response.append(serializer_error_dict[error][0])
            return Response({'error':error_list_for_response})


@api_view(['POST'])
def handle_store(request):

    if request.method == 'POST':
        header_info = request.META
        if 'HTTP_BEARER_TOKEN' in header_info.keys():
           
            token_from_res = header_info['HTTP_BEARER_TOKEN']
            if token_from_res == "":
                return Response({'token':"Null"})
            token_status , token_expiry , associated_business_id = check_token_validity(token_from_res)
            print(f'{token_status} =========== {token_expiry} ========== {associated_business_id}')
            if token_status == True:
                data = request.data
                data_dict = clean_dict_to_serialize(dict(data))
                data_dict['associated_business'] =associated_business_id
                print(data_dict)
                #data_dict['associated_business'] = list(associated_business_id)
                serializer = StoreSerializer(data = data_dict)
                
                
                if serializer.is_valid() == True:
                    print(data)
                    serializer.save()
                    return Response({'user':'valid' , 'token TTL':token_expiry , 'store-data-addition':'success'})
                else:
                    serializer_error_dict = dict(serializer.errors)
                    error_list_for_response = []
                    for error in serializer_error_dict.keys():
                        error_list_for_response.append(serializer_error_dict[error][0])
                    return Response({'error':error_list_for_response})
        else:
            return Response({'access':'denied'})

@api_view(['POST'])
def handle_business_inventory(request):
    if request.method == 'POST':
        header_info = request.META
        if 'HTTP_BEARER_TOKEN' in header_info.keys():
           
            token_from_res = header_info['HTTP_BEARER_TOKEN']
            if token_from_res == "":
                return Response({'token':"Null"})
            token_status , token_expiry , associated_business_id = check_token_validity(token_from_res , need_business_id=True)
            print(f'{token_status} =========== {token_expiry} ========== {associated_business_id}')
            if token_status == True:
                data_dict = clean_dict_to_serialize(dict(request.data))
                print(data_dict)
                return Response({"Looks like valid bro"})    