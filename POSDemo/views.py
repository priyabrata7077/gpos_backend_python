from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
#from .models import SubCategory, ProductInventoryManagement, Customer
from .models2 import Owner, Business, auth , storeMaster, BusinessInventoryMaster , Customer , Product ,TaxMaster , GenBill , SalesPending , storeInventoryMaster , JwtAuth, TransactionDetailsMaster , ModeOfPayment , SalesRegister , EmployeeMaster , EmployeeCredential , EmployeeAuth , PurchasePending , PurchaseRegister

from .serializer import OwnerSerializer, BusinessSerializer , StoreSerializer , BusinessInventorySerializer , StoreInventorySerializer , OwnerDetailsSerializer , ProductDataSerializer , SalesPendingSerializer , GenerateBillSerializer , SalesRegisterSerializer , ProductMasterserBusinessializer , CustomerSerializer , EmployeeSerializer , TransactionDetailsSerializer , ReturnSalesPendingSerializer , ReturnSalesPendingSerializer , EmployeeCredentialSerializer , EmployeeAuthSerializer , SupplierMasterSerializer , PurchaseRegisterSerializer , PurchasePendingSerializer , PurchaseTransactionSerializer


from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from pprint import pprint
from datetime import datetime, timezone , timedelta
import json
import string
import secrets
import hashlib
import json
from dateutil import tz
from pprint import pprint
from time import sleep
import jwt
from jwt.exceptions import InvalidKeyError
import os

#Custom Helper Functions 
########################################################################
def gen_token():
    choices = string.ascii_letters + string.digits
    token = ''.join((secrets.choice(choices) for i in range(32)))
    return token

def clean_dict_to_serialize(data_dict):
    for i in data_dict.keys():
        data_dict[i] = data_dict[i][0]
    
    return data_dict


def check_jwt_validity(jwt_from_api):
    
    decoded_jwt = jwt.decode(jwt_from_api , key = 'password123' , algorithms=['HS256'])
    #pprint(decoded_jwt)
    try:
        if 'owner' in decoded_jwt.keys:
            owner_id = decoded_jwt['owner']
            pass_hash = decoded_jwt['pass']
            
            check_jwt_in_db = JwtAuth.objects.filter(jwt = decoded_jwt).values('expiry')
            
            if len(check_jwt_in_db) == 0:
                return False , None
            else:
                check_owner = list(Owner.objects.filter(pk = owner_id , password=pass_hash).values('name' , 'pk'))
                if len(check_owner) == 0:
                    return False , None
                else:
                    jwt_expiry = check_jwt_in_db[0]['expiry']
                    if jwt_expiry < datetime.now(tz=timezone.utc):
                        return True , check_owner[0]['pk']
                    else:
                        return False , None
        if 'employee' in decoded_jwt.keys():
            employee_id = decoded_jwt['employee']
            pass_hash = decoded_jwt['pass']
            
            check_jwt_in_db = EmployeeAuth.objects.filter(jwt = jwt_from_api).values('employee' , 'employee__credential__password')
            if not check_jwt_in_db.exists():
                return False , None
            else:
                if pass_hash == list(check_jwt_in_db)[0]['employee__credential__password'] and employee_id == list(check_jwt_in_db[0]['employee']):
                    return True , employee_id
                else:
                    return False , None
    except InvalidKeyError:
        return False , None



def create_jwt(hashed_pass , owner_id=None ,  employee_id=None ,  owner=True , employee=False):
    
    if owner==True and employee==False:
    
        payload = {
            'owner':owner_id,
            'pass':hashed_pass,
        }

        jwt_key =  'password123'   #os.environ.get('GPOS_JWT_PASS')
        
        encoded_jwt = jwt.encode(payload=payload , key=jwt_key , algorithm='HS256')
        #print(f'the following json web token {encoded_jwt} has been created for {owner_id}')
        return encoded_jwt
    if employee == True and owner == False:
        payload = {
            'employee': employee_id,
            'pass': hashed_pass
            
        }

#Has been used in handle_login and handle_owner functions
def expiry_time_calc(seconds_to_add):
    time_now = datetime.now()
    #time_now_in_seconds = dt_obj.timestamp()
    future = time_now + timedelta(seconds=seconds_to_add)
    
    return future

def check_token_expiry(token_expiry_from_db):
    #token_expiry_from_db = float(token_expiry_from_db)  
    timestamp_now = datetime.now()
    #timestamp_now_seconds = timestamp_now_obj.timestamp()
    #timestamp_now = int(timestamp_now_seconds)
    
    
    
    
    print(f'{token_expiry_from_db} ------------ >>>>>>>>>>>>>>>>>>> -------------')
    print(f'{timestamp_now} ------- ================= ------------ ')
    

    
    print()
    print('))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
    print('----------------------------------------------------------------')
    print()
    print('((((((((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))))))))')
    if timestamp_now < token_expiry_from_db:
        #time now is less than the future token expiry time so that would imply that the tokken hasnt expired yet
        return True
    else:
        return False

def check_token_validity(token_from_response , need_business_id=True , need_user=False):
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
            associated_business_id = list(Business.objects.filter(owned_by = user_id_of_the_token).values('pk'))[0]['pk']
            if need_user == True:
                print('------------Returning User ID and Associated Business Id BRO-------------')
                print(f'{user_id_of_the_token} -- {associated_business_id}')
                print('----------------------------------------------------')
                
                return True , token_expiry , user_id_of_the_token , associated_business_id
            else:
                print('----------------------------------------------------')
                print(f'{user_id_of_the_token} -- {associated_business_id}')
                print('----------------------------------------------------')
                return True , token_expiry , str(associated_business_id)
        if need_business_id == False:
            return True , token_expiry , user_id_of_the_token
    else:
        return False , None , None


#this function decodes the json web token from api and checks if it has expired or not from jwtAuth tableand then checks if the user with given id and password hash exists in db if exists in 

  
def hash_pass(passwd):
    hash_object = hashlib.sha256(passwd.encode())
    pass_hash = hash_object.hexdigest()
    print(f'{passwd} - - - - - - - - - - - - - - - - - - - - - - hashed {pass_hash}')
    return pass_hash
def convert_time_to_ist(datetimeObj):
    #auto detecting zones
    from_zone = tz.gettz('IST')
    to_zone = tz.gettz('Asia/Kolkata')
    
    IST = datetimeObj.replace(tzinfo = from_zone)
    #converting time zone
    central = IST.astimezone(to_zone)
    print(central)
#################################################################################################

# token data in header 'HTTP_AUTHORIZATION': 'Bearer oEYOaVC955Onygsp3jjNmNQ8NTFUEDcv'
@api_view(['GET', 'POST'])
def handle_login(request):
        header_info = request.META
        ip_of_host_from_header = header_info['REMOTE_ADDR']
        #print(f'{header_info} -------- {type(header_info)}')
        print('-------------------------------------------------------------------')
        
        if request.method == 'POST':
        

            login_data = request.data
            login_data_dict =dict(login_data)
            print(f'+++++++++++++++++++++ Login Data Bro +++++++++++++++++')
            pprint(login_data_dict)
            if 'email' in login_data_dict.keys():
                print(
                    f'{login_data_dict["email"]} -------- {type(login_data_dict)}')
                #user_name = login_data_dict['username'][0]
                email = login_data_dict["email"]
                passwd = login_data_dict["password"]
                print(f'{email} ------- {passwd}')
                data_from_db = list(Owner.objects.filter(email=email , password = hash_pass(passwd)).values('pk' , 'name'))
                pprint(data_from_db)
                if len(data_from_db) == 0:
                    return Response({'No user found'})
                else:
                    new_jwt = create_jwt(owner_id = data_from_db[0]['pk'] , hashed_pass= login_data_dict['password'] , employee=False)
                    jwt_expiry = expiry_time_calc(86400)
                    
                    
                    
                    #before saving the newly created json web token after login I got
                    save_jwt = JwtAuth(jwt = new_jwt , expiry = jwt_expiry)
                    save_jwt.save()
                    
                    return Response({'user':data_from_db[0]['pk'] ,'bearer':new_jwt})                    
                    # checking the the user has already been logged in with the token
                    # checking if the user is already in the auth db.

'''            
            if 'token' in login_data_dict.keys():
                checK_token = auth.objects.filter(token = login_data_dict['token'][0]).values('user_name')
                if len(checK_token) == 0:
                    return Response({'invalid token'})
                else:
                    user_of_token = list(checK_token)[0]['user_name']
                    return Response({'token' : 'valid' , 'user': user_of_token })
'''                

@api_view(['POST'])
def handle_logout(request):
    header_info = request.META
    if request.method == 'POST':
        if 'HTTP_AUTHORIZATION' in header_info.keys():
            if header_info['HTTP_AUTHORIZATION'].split(' ')[0] == 'bearer' and header_info['HTTP_AUTHORIZATION'].split(' ')[1] != '':
                jwt_from_header = header_info['HTTP_AUTHORIZATION'].split(' ')[1]
                
                #checking if its in jwtauth table
                jwt_exists = list(JwtAuth.objects.filter(jwt = jwt_from_header))
                if len(jwt_exists) == 0:
                    return Response({"access":"denied"})
                else:
                    jwt_exists[0].delete()
                    print(f'JWT {jwt_from_header} removed successfully on user logout ')
                    return Response({'logout':'success'})
            else:
                return Response({'access':'denied'})
        else:
            return Response({'access':'denied'})
        
        
       
@api_view(['GET' , 'POST'])        
def handle_business(request):
    
    header_info = request.META
    print(header_info)
    if request.method == 'GET':
        business_data = Business.objects.all()
        serializer = BusinessSerializer(business_data, many=True)
        return Response(serializer.data) 
    
    if request.method == 'POST':
        if 'HTTP_AUTHORIZATION' in header_info.keys():
           
            token_from_res = header_info['HTTP_AUTHORIZATION'].split(' ')[1]
            
            data_dict = dict(request.data)           

            #print(f'token found from header {token_from_res}')
            if token_from_res == "":
                return Response({'access':'denied'})
            
            jwt_status , owner_pk = check_jwt_validity(token_from_res)
            
            if jwt_status == False:
                return Response({'access':'denied'})
            
            
            data_dict['date_of_entry'] = datetime.now().date()
            print(f'primary key of the owner from token {owner_pk} ')
            data_dict['owner_id'] = owner_pk
            
            serializer = BusinessSerializer(data = data_dict)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                serializer_error_dict = dict(serializer.errors)
                error_list_for_response =[]
                for error in serializer_error_dict.keys():
                    error_list_for_response.append(serializer_error_dict[error][0])
                return Response({'error':error_list_for_response})
        else:
            return Response({'access':'denied'})

         
         
         
         

@api_view(['POST' , 'GET'])         
def handle_owner_details(request):
    header_info = request.META
    if request.method == 'POST':
        if 'HTTP_AUTHORIZATION' in header_info.keys():
           
            jwt_from_res = header_info['HTTP_AUTHORIZATION'].split(' ')[1]
            print(f'token found from header {jwt_from_res}')
            if jwt_from_res == "":
                return Response({'access':"denied"})
            token_status , owner_id = check_jwt_validity(jwt_from_res)
            print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
            #checking if the token has expired with the help of the custom function check_token_expiry()
            
            if token_status == True:
                data_dict = clean_dict_to_serialize(dict(request.data))
                data_dict['owner_id'] = owner_id
                data_dict['date_of_entry'] = datetime.now().date()
                serializer = OwnerDetailsSerializer(data = data_dict)
                
                if serializer.is_valid():
                    serializer.save()
                    return Response(data_dict)
                else:
                    serializer_error_dict = dict(serializer.errors)
                    error_list_for_response =[]
                    for error in serializer_error_dict.keys():
                        error_list_for_response.append(serializer_error_dict[error][0])
                    return Response({'error':error_list_for_response})
                        

            else:
                return Response({"access":"denied"})
                

    
    
    
@api_view(['POST'])
def handle_owner(request):
    header_info = request.META
    if request.method =='POST':
        
        ip_of_host_from_header = header_info['REMOTE_ADDR']
        
        
        clean_data_dict = dict(request.data)
        pprint(clean_data_dict)
        
        #hashing the password
        clean_data_dict['password'] = hash_pass(clean_data_dict['password'])
        
        #converting the password into a jwt (JSON Web Token) format for authentication
        
        
        clean_data_dict['date_of_entry'] = datetime.now().date()
        print(f'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ password has been hashed bro')
        #print(f'{data} ============================================= {type(data)}')
        print(f'{clean_data_dict} ============================================= {type(clean_data_dict)}')
        serializer = OwnerSerializer(data = clean_data_dict)
        if serializer.is_valid():
            owner_instance = serializer.save()
            
            #user_token = gen_token()
            
            #creating a jwt (Json Web Token) with the owner id and his/her hashed password as payload
            user_jwt = create_jwt(owner_id = owner_instance.pk , hashed_pass =  clean_data_dict['password'] , employee=False)

            user_token_expiry = datetime.now() + timedelta(days=1)
            user_auth = JwtAuth(jwt=user_jwt , expiry = user_token_expiry)
            user_auth.save()
            
            
            return Response({'user added':True , 'generated jwt token':user_jwt})
        else:
            serializer_error_dict = dict(serializer.errors)
            error_list_for_response =[]
            for error in serializer_error_dict.keys():
                error_list_for_response.append(serializer_error_dict[error][0])
            return Response({'error':error_list_for_response})
    
    
    if request.method == 'GET':
        if 'HTTP_AUTHORIZATION' in header_info.keys():
            token_from_header = header_info['HTTP_AUTHORIZATION']
            if token_from_header.split(' ')[1] == " ":
                return Response({'token':'NULL'})
        token_status , owner_pk = check_jwt_validity(token_from_header)
        print(f'{token_status} -+ -+ -+ -+ -+ {owner_pk}')
        if token_status == True:
            data = request.data
            return Response({'access':'granted'})
        else:
            return Response({'access':'denied'})


@api_view(['POST'])
def handle_store(request):

    if request.method == 'POST':
        header_info = request.META
        if 'HTTP_AUTHORIZATION' in header_info.keys():
           
            token_from_res = header_info['HTTP_AUTHORIZATION'].split(' ')[1]
            if token_from_res == "":
                return Response({'access':'denied'})
            token_status , owner_pk = check_token_validity(token_from_res)
            print(f'{token_status} =========== {owner_pk}')
            if token_status == True:
                data = request.data
                data_dict = clean_dict_to_serialize(dict(data))
                data_dict['associated_owner'] = owner_pk
                print(data_dict)
                #data_dict['associated_business'] = list(associated_business_id)
                serializer = StoreSerializer(data = data_dict)
                
                
                if serializer.is_valid() == True:
                    print(data)
                    serializer.save()
                    return Response({'user':'valid' , 'store-data-addition':'success'})
                else:
                    serializer_error_dict = dict(serializer.errors)
                    error_list_for_response = []
                    for error in serializer_error_dict.keys():
                        error_list_for_response.append(serializer_error_dict[error][0])
                    return Response({'error':error_list_for_response})
            if token_status == False:
                return Response({'token':'invalid'})
        else:
            return Response({'access':'denied'})

@api_view(['POST'])
def handle_business_inventory(request):
    if request.method == 'POST':
        header_info = request.META
        if 'HTTP_BEARER_TOKEN' in header_info.keys():
           
            token_from_res = header_info['HTTP_BEARER_TOKEN']
            print(f'token found from header {token_from_res}')
            if token_from_res == "":
                return Response({'token':"Null"})
            token_status , token_expiry , associated_business_id = check_token_validity(token_from_res , need_business_id=True)
            print(f'{token_status} =========== {token_expiry} ========== {associated_business_id}')
            
            #note the choices in the product_quantity_type must be GM , PIECE or LTR
            
            if token_status == True:
                data_dict = clean_dict_to_serialize(dict(request.data))
                data_dict['updated_at'] = datetime.now()
                data_dict['associated_business'] = associated_business_id
                print(data_dict)
                serializer = BusinessInventorySerializer(data = data_dict)
                if serializer.is_valid() == True:
                    serializer.save()
                    return Response(data_dict)
                else:
                    serializer_error_dict = dict(serializer.errors)
                    error_list_for_response =[]
                    for error in serializer_error_dict.keys():
                        error_list_for_response.append(serializer_error_dict[error][0])
                    return Response({'error':error_list_for_response})
        else:
            return Response({'Token not found'})

#-------------------------------------------------------------------------------------------------------------------------
def store_and_business_inventory_logic(store_data_dict , associated_business_id_store_owner):
    business = Business.objects.get(pk = associated_business_id_store_owner)
    Business_inventory_update = BusinessInventoryMaster(updated_at = datetime.now() , product_name = store_data_dict['product_name'] , product_quantity_type = store_data_dict['product_quantity_type'] , product_quantity = store_data_dict['product_quantity'] , action='REMOVED' , price_per_unit = store_data_dict['price_per_unit'] , associated_business = business)
    Business_inventory_update.save()
    return True
#-------------------------------------------------------------------------------------------------------------------------



#in this function for now Im just taking the raw store id from api request I thinking of CREATING separate functionality for authenticating a store with a specific user thorugh some special token or jwt ( JSON Web Token )

        
@api_view(['POST'])
def get_all_stores_from_business_id(request):
    header_info = request.META
    if request.method == 'POST':
        if 'HTTP_AUTHORIZATION' in header_info.keys():
            if header_info['HTTP_AUTHORIZATION'] != 0:
                data_dict = clean_dict_to_serialize(dict(request.data))
                
                #Bro I just found a reverse relation query trick 
                all_stores = list(Business.objects.filter(pk = data_dict['business']).values('store__store_name' , 'store__associated_owner__name' , 'store__store_location'))
                
                if len(all_stores) == 0:
                    return Response({'No Store Was found under the given business ID '})
                else:
                    return Response({'all stores': all_stores})
            else:
                return Response({'access':'denied'})
        else:
            return Response({'access':'denied'})
        
        
     



#--------------------------------------------------------FOR SALES PAGE , ITS WITHOUT TOKEN AUTHENTICATION FOR NOW ---------------------------------            
@api_view(['POST' , 'GET'])
def handle_customer_details(request):
    
    if request.method == 'GET':
        data = request.data
        data_dict =clean_dict_to_serialize(dict(data))
        
        if 'name' in data_dict.keys() or 'contact' in data_dict.keys():
            
            
            if 'contact' != '':
                customer = list(Customer.objects.filter( store__pk = data_dict['store'] ,  contact = data_dict['contact']).values('name' , 'address'))
                
                if len(customer) != 0:
                    name = customer[0]['name']
                    address = customer[0]['address']
                    return Response({'name': name , 'address': address})
                else:
                    return Response({'customer':'None'})
            else:
                return Response({'invalid':'input'})
        else:
            return Response({'invalid':'input'})

    if request.method == 'POST':
        data_dict = clean_dict_to_serialize(dict(request.data))
        if data_dict['address'] == '':
            data_dict['address'] = list(storeMaster.objects.filter(pk=1).values('associated_business__address'))[0]['associated_business__address']
        serializer = CustomerSerializer(data = data_dict)
        if serializer.is_valid():
            customer_instance = serializer.save()
            return Response({f'{customer_instance.pk}':'added'})
        else:
            serializer_error_dict = dict(serializer.errors)
            error_list_for_response =[]
            for error in serializer_error_dict.keys():
                error_list_for_response.append(serializer_error_dict[error][0])
            return Response({'error':error_list_for_response})         
            



@api_view(['POST'])
def handle_products_data(request):
    if request.method == 'POST':
        
        data_dict = clean_dict_to_serialize(dict(request.data))
        
        
        if 'product_name' in data_dict.keys():
            dict_for_response = {}
            print(f' ========================================== {data_dict["product_name"]}')
            products = Product.objects.filter(name__startswith = data_dict['product_name']).values( 'pk' , 'name' , 'MRP' , 'purchase_rate' , 'sale_rate' , 'gst')
            if len(products) != 0:
                if len(products) == 1:
                    print(list(products)[0])
                    return Response({ 'products' : list(products)})
                else:
                    print(list(products))
                    '''
                    for queryset in products:
                        print(' +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ')
                        print(queryset)
                        dict_for_response.update(dict(queryset))
                    '''
                    return Response({'products' : list(products)})
        else:
            return Response({'No name to search for bro'})


#def handling_store_inventory():
def update_removed_product_from_store_inventory(product_id , product_count , store_id):
    
    product_quantity_from_db = list(storeInventoryMaster.objects.filter(associated_store = store_id , product = product_id).values('available' , 'pk'))
    print(product_quantity_from_db)
    
    if len(product_quantity_from_db) != 0:
        product_quantity_from_db_updated = int(product_quantity_from_db[0]['available']) - int(product_count)
        store_inventory = storeInventoryMaster.objects.get(pk = int(product_quantity_from_db[0]['pk']))
        store_inventory.available = product_quantity_from_db_updated
        store_inventory.save()
        
        return True
    else:
        return False

'''
def test_decorator(*args, **kwargs):

    print('Running decorator')
    def wrapper(func):
        print(args[0])
        #print(f'result from api is {result_from_api}')
        result = func(*args[0])
        return result
    return wrapper
'''

@api_view(['POST'])

def handle_sales_register(request):
    header_info = request.META
    #print(header_info)
    if 'HTTP_AUTHORIZATION' in header_info.keys():
        if header_info['HTTP_AUTHORIZATION'] != '':
            token_from_header = header_info['HTTP_AUTHORIZATION'].split(' ')[1]
            print(f'Token Found From HEADER -> {token_from_header}')
            token_status , owner_pk  = check_jwt_validity(token_from_header)
            
            if token_status == True:
                if request.method =='POST':
                    data_dict = clean_dict_to_serialize(dict(request.data))
                    bill_from_store = GenBill.objects.filter(store=data_dict['store']).order_by('-pk').values('pk' , 'bill_id').first()
                    print('6566666666666666666666666666666666666666666666666666666666666666')
                    print(f'{data_dict["store"]}  ============{data_dict["employee"]}')

                    if bill_from_store == None:
                        new_bill_id = 1
                        generate_bill_dict = {'bill_id' : new_bill_id, 'time' : datetime.now() , 'store' : int(data_dict['store']) }
                        
                    else:
                    
                        new_bill_id = int(bill_from_store['bill_id']) +1
                        generate_bill_dict = {'bill_id' : new_bill_id, 'time' : datetime.now(), 'store' : int(data_dict['store'])}
                        
                    genBillSerializer = GenerateBillSerializer(data=generate_bill_dict)
                    if genBillSerializer.is_valid():
                        new_bill_pk = genBillSerializer.save()

                    #sleep(5)
                    data_from_sales_pending = SalesPending.objects.filter(store = int(data_dict['store']) , employee=int(data_dict['employee']) ).values( 'business' ,'store' , 'employee' ,'product' , 'gst' , 'product_quantity' , 'mrp' , 'purchase_rate' , 'sale_rate')
                    pprint(list(data_from_sales_pending))
                    
                    data_from_sales_pending_with_bill_id = []
                    for sales_pending_dict in list(data_from_sales_pending):
                        print(sales_pending_dict)
                        
                        #handling of removal of purchased products from  store Inventory
                        update_removed_product_from_store_inventory(sales_pending_dict['product'] , sales_pending_dict['product_quantity'] , sales_pending_dict['store'])
                        sales_pending_dict['bill_ID'] = new_bill_pk.pk
                        sales_pending_dict['bill_no'] = new_bill_id
                        '''
                        print()
                        print(sales_pending_dict)
                        print(' 0000000000000000000000000000000000 ')
                        '''
                        data_from_sales_pending_with_bill_id.append(sales_pending_dict)

                    sales_register_serializer  = SalesRegisterSerializer(data = data_from_sales_pending_with_bill_id , many=True)
                    if sales_register_serializer.is_valid():
                        sales_register_serializer.save()

                        #handling of removal of data from sales pending data base
                        
                        
                        
                        SalesPending.objects.filter(store = data_dict['store'] , employee=data_dict['employee'] ).delete()
                        
                        
                        
                        
                        print('Data has been removed from sales pending successfully')
                        
                        #handle putting data in paymentdetailsmaster table here
                        #list_data = list(data_dict['mop_amt'])
                        
                        
                        return Response(data_from_sales_pending_with_bill_id)
                        
                        

                        #return Response({'data':list(data_from_sales_pending_with_bill_id)})
                    else:
            
                        return Response(sales_register_serializer.errors)
            else:
                return Response({'access':'denied'})
        else:
            return Response({'access':'denied'})
    else:
        return Response({'access':'denied'})


@api_view(['POST'])
def handle_transaction_details(request):

    if request.method ==  'POST':
        data_dict = clean_dict_to_serialize(dict(request.data))
        list_mop_amt_data = data_dict['mop_amt'][1:-1].split(',')
        
        transaction_details_dict = {}
        
        #business_id_from_store_id = list(storeMaster.objects.filter(pk = data_dict['store']).values('associated_business__pk'))
        data_from_sales_register = list(SalesRegister.objects.filter(bill_ID = data_dict['bill_ID']))
        
        print('???????????????????????????????????????????????????????????????????????')
        pprint(data_from_sales_register)
        
        mop_names_and_amout_dict = [ { 'mop_name' : list(ModeOfPayment.objects.filter(pk = data2.split(':')[0]).values('name' , 'pk'))[0]['name'] ,'mop_id' :  list(ModeOfPayment.objects.filter(pk = data2.split(':')[0]).values('name' , 'pk'))[0]['pk'] ,  'amount_paid' : data2.split(':')[1] } for data2 in list_mop_amt_data]
        
        
        product_id_and_name = [ { 'product_id' : model_to_dict(sales_register)['product'] , 'product_name': model_to_dict(sales_register)['product_name']  , 'product_quantity':model_to_dict(sales_register)['product_quantity'] } for sales_register in data_from_sales_register ]
        
        transaction_details_dict['bill_id'] = model_to_dict(data_from_sales_register[0])['bill_ID']
        transaction_details_dict['date_of_entry'] = datetime.now()
        transaction_details_dict['business'] = model_to_dict(data_from_sales_register[0])['business']
        transaction_details_dict['store'] = model_to_dict(data_from_sales_register[0])['store']
        transaction_details_dict['employee'] = model_to_dict(data_from_sales_register[0])['employee']
        transaction_details_dict['mop'] = mop_names_and_amout_dict
        transaction_details_dict['products'] = product_id_and_name

        transaction_details_serializer = TransactionDetailsSerializer(data = transaction_details_dict)
        
        if transaction_details_serializer.is_valid():
            transaction_details_serializer.save()
            return Response(transaction_details_dict)
        else:
            return Response(transaction_details_serializer.errors)

        #return Response(transaction_details_dict)
        '''
        except Exception as e:
            print(e)
            return Response({'Some Error Occured bro'})
        '''
 
@api_view(['POST' , 'PATCH'])
def handle_sales_pending(request):
    header_info = request.META
    if request.method == 'POST':
        
        if 'HTTP_AUTHORIZATION' in header_info.keys():
            if header_info['HTTP_AUTHORIZATION'] != '':
                
                token_from_header = header_info['HTTP_AUTHORIZATION'].split(' ')[1]
                
                token_status , owner_pk = check_jwt_validity(token_from_header)
                
                if token_from_header == False:
                    return Response({'access':'denied'})
                else:
                    data_dict = clean_dict_to_serialize(dict(request.data))
                    #serializer = SalesPendingSerializer
                    product_id_from_api = data_dict['product']
                    product_data = Product.objects.filter(pk=int(product_id_from_api)).values('name' , 'MRP' , 'purchase_rate' , 'sale_rate' , 'gst')
                    if len(product_data) != 0:
                        
                        associated_business_store = list(storeMaster.objects.filter(pk = data_dict['store']).values('associated_business'))
                            
                        item_name = list(product_data)[0]['name']
                        item_mrp = list(product_data)[0]['MRP']
                        item_purchase_rate = list(product_data)[0]['purchase_rate']
                        item_sale_rate = list(product_data)[0]['sale_rate']
                        item_gst = list(product_data)[0]['gst']
                        '''
                        product_name = models.CharField(max_length=100)
                        mrp = models.CharField
                        purchase_rate = models.CharField(max_length=20)
                        sale_rate = models.CharField(max_length=20)
                        gst = models.ForeignKey(TaxMaster , on_delete=models.DO_NOTHING , related_name='salespending' )
                        row_total =
                        '''
                        #now putting the data from product db to salespending db by modifying the requst data_dict
                        data_dict['product_name'] = item_name
                        data_dict['mrp'] = item_mrp
                        data_dict['purchase_rate'] = item_purchase_rate
                        data_dict['sale_rate'] = item_sale_rate
                        data_dict['gst'] = str(item_gst)
                        data_dict['row_total'] = str(int(data_dict['product_quantity']) * int(item_sale_rate))
                        
                        #fist getting the associated_business id from store with  .filter.values method and using the store id from request as pk and then setting it in the data dict before serializing the data.
                        data_dict['business'] = int(associated_business_store[0]['associated_business'])
                        print(' >->->->->->->->->->->->->->->->->->->->->->')
                        print(data_dict)
                        serializer = SalesPendingSerializer(data = data_dict)
                        if serializer.is_valid():
                            serializer.save()
                            return Response({'data' : data_dict})
                        else:
                            serializer_error_dict = dict(serializer.errors)
                            error_list_for_response = []
                            for error in serializer_error_dict.keys():
                                error_list_for_response.append(serializer_error_dict[error][0])
                            return Response({'error':error_list_for_response})
                    else:
                        return Response({'no product in inventory'})
            else:
                return Response({'access':'denied'})
        else:
            return Response({'access':'denied'})

    if request.method == 'PATCH':
        
        try:
            patch_data_dict = clean_dict_to_serialize(dict(request.data))
            sales_pending_query_set = SalesPending.objects.filter(pk=patch_data_dict['sales_pending_id'])
            sales_pending_query_set.update(product_quantity = patch_data_dict['product_quantity'])
            #sales_pending_query_set.save()
            return Response({'update':'success'})
        except Exception as e:
            print(e)
            return Response({'error occured bro'})
        


''' 
            serializer_error_dict = dict(serializer.errors)
            error_list_for_response =[]
            for error in serializer_error_dict.keys():
                error_list_for_response.append(serializer_error_dict[error][0])
            return Response({'error':error_list_for_response})

'''     
 
@api_view(['POST'])
def handle_product_master(request):
    header_info = request.META
    if request.method == 'POST':
        if 'HTTP_AUTHORIZATION' in header_info.keys():
            if header_info['HTTP_AUTHORIZATION'] != '':
                
                token_from_header = header_info['HTTP_AUTHORIZATION'].split(' ')[1]
                
                token_status , owner_pk = check_jwt_validity(token_from_header)
                
                if token_status == False:
                    return Response({'access':'denied'})
                else:
                    data_dict = clean_dict_to_serialize(dict(request.data))
                    print(data_dict)
                    serializer = ProductMasterserBusinessializer(data = data_dict)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(data_dict)
                    else:
                        serializer_error_dict = dict(serializer.errors)
                        error_list_for_response =[]
                        for error in serializer_error_dict.keys():
                            error_list_for_response.append(serializer_error_dict[error][0])
                        return Response({'error':error_list_for_response})
            else:
                return Response({'access':'denied'})
        else:
            return Response({'access':'denied'})
    
@api_view(['POST'])
def add_store_under_business_id(request):
    header_info = request.META
    if request.method == 'POST':
        if 'HTTP_AUTHORIZATION' in header_info.keys():
            if header_info['HTTP_AUTHORIZATION'] !=  '': 
                
                token_from_header = header_info['HTTP_AUTHORIZATION'].split(' ')[1]
                
                token_status , owner_pk = check_jwt_validity(token_from_header)
                
                if token_status == False:
                    return Response({'access':'denied'})
                else:
                    data_dict = clean_dict_to_serialize(dict(request.data))
                    
                    #owner_of_business_id_from_api = list(Business.objects.filter(pk = data_dict['business']).values('owner_id'))
                    #heres two way to do the same thing u getting bro?
                    owner_of_business_id_from_api = list(Owner.objects.filter(business__pk = data_dict['business']).values('pk')) #using reverse relation
                    if len(owner_of_business_id_from_api) == 0:
                        return Response({'No business was found'})
                    else:
                        data_dict['associated_owner'] = owner_of_business_id_from_api[0]['pk']
                        data_dict['associated_business'] = data_dict['business']
                        serializer = StoreSerializer(data = data_dict)
                        if serializer.is_valid():
                            serializer.save()
                            return Response(data_dict)
                        else:
                            serializer_error_dict = dict(serializer.errors)
                            error_list_for_response = []
                            for error in serializer_error_dict.keys():
                                error_list_for_response.append(
                                serializer_error_dict[error][0])
                            return Response({'error':error_list_for_response})
            else:
                return Response({'access':'denied'})
        else:
            return Response({'access':'denied'})

def is_product_available_in_store(store_id , product_id):
    data = list(storeInventoryMaster.objects.filter(associated_store = store_id , product = product_id).values('pk' , 'product__name'))
    if len(data) == 0:
        return False , None
    else:
        return True , data[0]['product__name']
    

@api_view(['POST'])
def add_product_in_the_store_inventory(request):
    header_info = request.META
    pprint(header_info)
    if request.method == 'POST':
        if 'HTTP_AUTHORIZATION' in header_info.keys():
            if header_info['HTTP_AUTHORIZATION'] != '':
                
                token_from_header = header_info['HTTP_AUTHORIZATION'].split(' ')[1]
                
                token_status , owner_pk  = check_jwt_validity(token_from_header)
                if token_status == False:
                    return Response({'access':'denied'})
                else:
                    data_dict = clean_dict_to_serialize(dict(request.data))
                    
                    #putting the current date time
                    data_dict['updated_at'] = datetime.now()
                    data_dict['associated_store'] = data_dict['store']
                    
                    product_in_store , name = is_product_available_in_store(data_dict['store'] , data_dict['product'])
                    if product_in_store == True:
                        return Response({f'Product {name} Already in store'})
                    else:
                        business_id_from_product= list(Business.objects.filter(products__pk = data_dict['product']).values('pk'))
                        if len(business_id_from_product) == 0:
                            return Response({'No relation found'})
                        else:
                            data_dict['business'] = business_id_from_product[0]['pk']
                            serializer = StoreInventorySerializer(data = data_dict)
                        
                        if serializer.is_valid():
                            serializer.save()
                            data_dict['product_name'] = list(Product.objects.filter(pk = data_dict['product']).values('name'))[0]['name']
                            return Response(data_dict)
                        else:
                            serializer_error_dict = dict(serializer.errors)
                            error_list_for_response =[]
                            for error in serializer_error_dict.keys():
                                error_list_for_response.append(serializer_error_dict[error][0])
                            return Response({'error':error_list_for_response})
            else:
                return Response({'access':'denied'})
        else:
            return Response({'access':'denied'})                
            
            
#Now I need to authenticate users with jwt and store it in the auth file bro
#Okay I got it I need to hash the password of the during login and signup
#and store it in the auth table , and then I need to create a jwt json web token which I will return to the front end and it will be stored in the browser cookies and I will get it in each subsequent request for validation.
      
@api_view(['POST'])
def add_business_employee(request):
    header_info = request.META
    if request.method == 'POST':
        
        if 'HTTP_AUTHORIZATION' not in header_info.keys():
            #if header_info['HTTP_AUTHORIZATION'].split(' ')[0] == 'bearer' and header_info['HTTP_AUTHORIZATION'].split(' ')[1] != '':
            
                
            data_dict = dict(request.data)
            print(data_dict)
            serializer =  EmployeeSerializer(data=data_dict)
            if serializer.is_valid():
                employee_instance = serializer.save()
                data_dict['id'] = employee_instance.pk
                return Response(data_dict)
            else:
                serializer_error_dict = dict(serializer.errors)
                error_list_for_response =[]
                for error in serializer_error_dict.keys():
                    error_list_for_response.append(serializer_error_dict[error][0])
                return Response({'error':error_list_for_response}) 
            #else:
            #    return Response({'access':'denied'})
        else:
            return Response({'access':'denied'})      


@api_view(['POST'])
def handle_product_return(request):
    header_info = request.META
    
    if 'HTTP_AUTHORIZATION' in header_info.keys():
        if header_info['HTTP_AUTHORIZATION'] != '':
            
            token_from_header = header_info['HTTP_AUTHORIZATION'].split(' ')[1]
            
            token_status , owner_pk = check_jwt_validity(token_from_header)
            
            if token_status == False:
                return Response({'access':'denied'})
            if request.method == 'POST':
            
                data_dict = clean_dict_to_serialize(dict(request.data))
                pprint(data_dict)
                search_bill = list(TransactionDetailsMaster.objects.filter(bill_id = data_dict['bill_id']).values("products" , 'date_of_entry' , 'mop'))
                pprint(search_bill)
                if len(search_bill) == 0:
                    return Response({'no bill found'})
                
                else:
                    products_from_bill_id = search_bill[0]['products']
                    print(']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
                    print(products_from_bill_id)
                    
                    product_id_list = [ i['product_id'] for i in products_from_bill_id ]
                    print(f' =================================== {product_id_list}')
                    
                    if int(data_dict['product']) in product_id_list:
                        found = True
                    else:
                        found = False
                    
                    if found == False:
                        return Response({"Product Not In Bill"})

                    #look for customer in a store
                    data_from_sales_register = SalesRegister.objects.filter(bill_ID = data_dict['bill_id'])
                    #data_from_sales_register = model_to_dict(data_from_sales_register[1])
                    for i in range(len(data_from_sales_register)):
                        data = model_to_dict(data_from_sales_register[i])
                        print(data)
                        
                        return_sales_pending_data_dict = {}
                        return_sales_pending_data_dict['date_of_entry'] = datetime.now()
                        
                        
                        data['date_of_entry'] = datetime.now()
                        if str(data['product']) == data_dict['product']:
                            data['return_quantity'] = data_dict['return_quantity']
                            pprint(data)
                            save_in_sales_pending_table_serializer = ReturnSalesPendingSerializer(data = data)
                            if save_in_sales_pending_table_serializer.is_valid():
                                save_in_sales_pending_table_serializer.save()
                                saving_in_return_sales_pending_success = True
                            else:
                                saving_in_return_sales_pending_success = False
                                return Response(save_in_sales_pending_table_serializer.errors)   

                    #print(data_from_sales_register)
                
                    return Response({'Holla'})
        else:
            return Response({'access':'denied'})
    else:
        return Response({'access':'denied'})
            
            


def jwt_header_auth(header):
    
    if 'HTTP_AUTHORIZATION' not in header.keys():
        return False , None

    if header['HTTP_AUTHORIZATION'].split(' ')[0] != 'bearer':
        return False , None
    
    if header['HTTP_AUTHORIZATION'].split(' ')[1] == '':
        return False , None
    
    jwt_status , owner_id = check_jwt_validity(header['HTTP_AUTHORIZATION'].split(' ')[1].strip() )

    if jwt_status == False:
        return False  , None
    
    return True , owner_id



@api_view(['POST'])
def handle_employee_signup(request):
    if request.method == 'POST':
        
        data_dict = clean_dict_to_serialize(dict(request.data))
        pass


@api_view(['POST' , 'PATCH'])
def handle_employee_login(request):
    
    if request.method == 'POST':
        
        data_dict = clean_dict_to_serialize(dict(request.data))
        data_dict['password'] = hash_pass(data_dict['password'])
        data_dict['modified_on'] = datetime.now()
        
        #Cheking If the employee id Exists in the EmployeeMaster Database
        check_employee = list(EmployeeMaster.objects.filter(pk = data_dict['employee']).values('name' , 'credential' ,'business'))
        
        if len(check_employee) == 0:
            return Response({'access':'denied'})
        '''
        if check_employee[0]['credential__password'] != data_dict['password']:
            return Response({'access':'denied'})
        '''
        #If the employee is already in EmployeeCredential table the data no more rows can be created with the same employee ID through POST method We'll Implement PATCH method for that bruv :)
        if check_employee[0]['credential'] != None:
            print('|||||||||||||||||||||')
            
            return Response({'employee':check_employee[0]['name'] , 'business':check_employee[0]['business']})
        #Now Checking If the employee is already in  the EmployeeCredential Table
        
        
        data_dict['Employee Name'] = check_employee[0]['name']
        employee_credential_serializer = EmployeeCredentialSerializer(data = data_dict)
        
        if employee_credential_serializer.is_valid():
            employee_jwt = create_jwt(employee_id = data_dict['employee'] , hashed_pass= data_dict['password'] , employee=True , owner=False , owner_id=None)
            data_dict['jwt'] = employee_jwt
            employee_credential_serializer.save()
            
            #now adding the generated employee auth json web token in EmployeeAuth table
            
            #adding the store in the data dict for employeeAuth Table
            data_dict['business'] = check_employee[0]['business']
            
            data_dict['have_access'] = True 
            pprint(data_dict)
            employee_auth_serializer = EmployeeAuthSerializer(data = data_dict)
            
            if employee_auth_serializer.is_valid():
                employee_auth_serializer.save()
                return Response(data_dict)

            else:

                serializer_error_dict = dict(serializer.errors)
                error_list_for_response =[]
                for error in serializer_error_dict.keys():
                    error_list_for_response.append(serializer_error_dict[error][0])
                return Response({'error':error_list_for_response})

               
            
            
            
        else:
            serializer_error_dict = dict(employee_credential_serializer.errors)
            error_list_for_response =[]
            for error in serializer_error_dict.keys():
                error_list_for_response.append(serializer_error_dict[error][0])
            return Response({'error':error_list_for_response})
        
    if request.method == 'PATCH':
        data_dict = clean_dict_to_serialize(dict(request.data))
        
        employee_credential = EmployeeCredential.objects.filter(employee = data_dict['employee'] , username = data_dict['username'])
        
        
        
        if employee_credential.exists():
            print(employee_credential.explain())
            if 'password' in data_dict.keys():
                data_dict['password'] = hash_pass(data_dict['password'])
                data_dict['modified_on'] = datetime.now()
                
                serializer = EmployeeCredentialSerializer(instance=employee_credential[0] ,data=data_dict)
                
                if serializer.is_valid():
                    serializer.save()
                    return Response({'auth':'success'})
                

                
            
            return Response({'user':'exists'})
        else:
            return Response({'user':'unverified'})
        
        
@api_view(['POST'])
def handle_employee_auth(request):
    
    header_info = request.META
    if request.method == 'POST':
        pass
        
@api_view(['POST'])
def handle_supplier(request):
    
    header_info = request.META
    if request.method == 'POST':
        
        if 'HTTP_AUTHORIZATION' in header_info.keys():
            token = header_info['HTTP_AUTHORIZATION'].split(' ')[1]
            
            token_status , owner_pk = check_jwt_validity(token)
            
            if token_status == False:
                return Response({'access':'denied'})
            
            data_dict = clean_dict_to_serialize(dict(request.data))
            data_dict['date_of_entry'] = datetime.now()
            
            serializer = SupplierMasterSerializer(data= data_dict)
            if serializer.is_valid():
                supplier_instance = serializer.save()
                data_dict['supplied_id'] = supplier_instance.pk
                return Response(data_dict)
            else:
                serializer_error_dict = dict(serializer.errors)
                error_list_for_response =[]
                for error in serializer_error_dict.keys():
                    error_list_for_response.append(serializer_error_dict[error][0])
                return Response({'error':error_list_for_response})               
        
        else:
            return Response({'access':'denied'})
        
        

@api_view(['POST'])
def purchase_pending(request):
    
    header_info = request.META
    
    if 'HTTP_AUTHORIZATION' not in header_info.keys():
        return Response({'access':'denied'})
    
    if header_info['HTTP_AUTHORIZATION'] == '':
        return Response({'access':'denied'})
    
    if request.method == 'POST':
        data_dict = clean_dict_to_serialize(dict(request.data))
        pprint(data_dict)
        
        data_dict['date_and_time'] = datetime.now()
        
        product_purchase_rate = Product.objects.filter(pk=data_dict['products']).values('MRP' , 'purchase_rate')
        print("nigga what?")
        if product_purchase_rate.exists():
            dict_product_data = list(product_purchase_rate)[0]
            data_dict['total'] = float(dict_product_data['purchase_rate']) * float(data_dict['quantity'])
            data_dict['purchase_rate'] = dict_product_data['purchase_rate']
            serializer = PurchasePendingSerializer(data = data_dict)
            if serializer.is_valid():
                pur_reg_instance = serializer.save()
                return Response({'operation':'successful'})
            else:
                serializer_error_dict = dict(serializer.errors)
                error_list_for_response =[]
                for error in serializer_error_dict.keys():
                    error_list_for_response.append(serializer_error_dict[error][0])
                return Response({'error':error_list_for_response})            

@api_view(['POST'])
def purchase_register(request):
    
    
    header_info = request.META  
    
    if 'HTTP_AUTHORIZATION' not in header_info.keys():
        return Response({'access':'denied'})
    
    if header_info['HTTP_AUTHORIZATION'] == '':
        return Response({'access':'denied'})  

    if request.method == 'POST':
        
        data_dict = clean_dict_to_serialize(dict(request.data))
    
        data_from_purchase_pending = PurchasePending.objects.filter(store = data_dict['store'] ,  supplier = data_dict['supplier'])
            
        if data_from_purchase_pending.exists():
            
            
            data_from_sales_register = PurchaseRegister.objects.filter(store = data_dict['store']).order_by('-bill_id').first()
            
            if data_from_sales_register == None:
                bill_id = 1
            else:
                bill_id = int(model_to_dict(data_from_sales_register)['bill_id']) + 1
            
            
            data_list_from_purchase_pending = []
            for data in data_from_purchase_pending:
                data = model_to_dict(data)
                del data['id']
                data['bill_id'] = bill_id
                data_list_from_purchase_pending.append(data)
                
            serializer = PurchaseRegisterSerializer(data = data_list_from_purchase_pending , many=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":data_list_from_purchase_pending})
            else:
                serializer_error_dict = dict(serializer.errors)
                error_list_for_response =[]
                for error in serializer_error_dict.keys():
                    error_list_for_response.append(serializer_error_dict[error][0])
                return Response({'error':error_list_for_response})  
    
@api_view(['POST'])
def handle_purchase_transaction(request):
    header_info = request.META
    
    if 'HTTP_AUTHORIZATION' not in header_info.keys():
        return Response({'access':'denied'})
    
    if header_info['HTTP_AUTHORIZATION'] == '':
        return Response({'access':'denied'})
    
    if request.method == 'POST':
        data_dict = clean_dict_to_serialize(dict(request.data))
        data_dict['date_of_entry'] = datetime.now()
        
        
        stripped_mop = data_dict['mop'][1:-1].split(',')
        data_dict['mop'] = stripped_mop
        
        
        
        
        data_from_purchase_register = PurchaseRegister.objects.filter(bill_id = data_dict['bill_id']).values('supplier' , 'total')
        
        if data_from_purchase_register.exists():
            supplier = data_from_purchase_register[0]['supplier']
            print(supplier)
            data_dict['supplier_id'] = supplier
           
        else:
            return Response({'Error':'occured'})
        
        mop_names_and_amout_dict = [ { 'mop_name' : list(ModeOfPayment.objects.filter(pk = data2.split(':')[0]).values('name' , 'pk'))[0]['name'] ,'mop_id' :  list(ModeOfPayment.objects.filter(pk = data2.split(':')[0]).values('name' , 'pk'))[0]['pk'] ,  'amount_paid' : data2.split(':')[1] } for data2 in stripped_mop]
    
        data_dict['mop'] = mop_names_and_amout_dict
        
        serializer = PurchaseTransactionSerializer(data = data_dict)
        
        if serializer.is_valid():
            transaction_instance = serializer.save
            return Response({'Operation':'Success'})
        
        else:
            
            serializer_error_dict = dict(serializer.errors)
            error_list_for_response =[]
            for error in serializer_error_dict.keys():
                error_list_for_response.append(serializer_error_dict[error][0])
            return Response({'error':error_list_for_response})




def handle_stock_change(request):
    
    if request.method == 'POST':
        pass

@api_view(['POST'])
def handle_product_categories(request):

    if request.method == 'POST':
        data_dict = clean_dict_to_serialize(dict(request.data))
        
        return Response(data_dict)





