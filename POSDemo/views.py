from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
#from django.forms.models import model_to_dict
#from .models import SubCategory, ProductInventoryManagement, Customer
from .models2 import Owner, Business, auth , storeMaster, BusinessInventoryMaster , Customer , Product ,TaxMaster , GenBill , SalesPending
from .serializer import OwnerSerializer, BusinessSerializer , StoreSerializer , BusinessInventorySerializer , StoreInventorySerializer , OwnerDetailsSerializer , ProductDataSerializer , SalesPendingSerializer , GenerateBillSerializer , SalesRegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from pprint import pprint
from datetime import datetime, timezone
import json
import string
import secrets
import hashlib
import json
from dateutil import tz
from pprint import pprint
from time import sleep
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
def expiry_time_calc(seconds_to_add):
    dt_obj = datetime.today()
    time_now_in_seconds = dt_obj.timestamp()
    expt_time = int(time_now_in_seconds)+seconds_to_add
    
    return expt_time

def check_token_expiry(token_expiry_from_db):
    #token_expiry_from_db = float(token_expiry_from_db)  
    timestamp_now_obj = datetime.today()
    timestamp_now_seconds = timestamp_now_obj.timestamp()
    timestamp_now = int(timestamp_now_seconds)
    
    
    
    
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
        return True
    else:
        return True

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
            login_data_dict = dict(login_data)
            if 'email' in login_data_dict.keys():
                print(
                    f'{login_data_dict["email"]} -------- {type(login_data_dict)}')
                #user_name = login_data_dict['username'][0]
                email = login_data_dict['email'][0]
                passwd = login_data_dict['password'][0]
                print(f'{email} ------- {passwd}')
                data_from_db = Owner.objects.filter(email=email , password = hash_pass(passwd))
                
                if len(data_from_db) == 0:
                    return Response({'no user'})
                else:
                    data_from_db_values = list(
                        data_from_db.values('name', 'email', 'password'))
                    if email != data_from_db_values[0]['email'] and passwd != data_from_db_values[0]['password']:
                        return Response({'invalid email and password'})
                    if email != data_from_db_values[0]['email']:
                        return Response({'Invalid Email'})
                    if hash_pass(passwd) != data_from_db_values[0]['password']:
                        return Response({'invalid password'})

                    # checking the the user has already been logged in with the token
                    # checking if the user is already in the auth db.
                    check_user_in_auth = list(auth.objects.filter(user_email = email).values('token'))

                    if len(check_user_in_auth) == 0:
                        user_token = gen_token()
                        user_token_expiry = expiry_time_calc(86400)
                        user_auth = auth(user_name=data_from_db_values[0]['name'], user_email=data_from_db_values[0]['email'], token=user_token , token_expiry = user_token_expiry , user_ip = ip_of_host_from_header , user_password = hash_pass(passwd))
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
    
    header_info = request.META
    print(header_info)
    if request.method == 'GET':
        business_data = Business.objects.all()
        serializer = BusinessSerializer(business_data, many=True)
        return Response(serializer.data) 
    
    if request.method == 'POST':
        if 'HTTP_AUTHORIZATION' in header_info.keys():
           
            token_from_res = header_info['HTTP_AUTHORIZATION']
            
            

            print(f'token found from header {token_from_res}')
            if token_from_res == "":
                return Response({'token':"Null"})
            token_from_res = token_from_res.split(' ')[1].strip()
            token_status , token_expiry , associated_user_id = check_token_validity(token_from_res , need_business_id=False)
            data = request.data
            print(data)
            data_dict = dict(data)
            print(data_dict)
            
            #here I'm fist getting the owner data from the Owner model with .filter method and getting its primary_key with .values method which gives a dictionary in then converting the whole thing into a list slicing it at the zeroth index wich gives us the data dictionary {'pk' : int_value}.
            '''
            owner_pk_from_db = list(Owner.objects.filter(name=data_dict['owned_by'][0]).values('pk'))[0]['pk']
            print(owner_pk_from_db)
            '''
            
            data_dict['owned_by'] = [f'{associated_user_id}']
            print(data_dict)
            
            #converting the modified python dict back to json data
            clean_data_dict = clean_dict_to_serialize(data_dict)
            print(clean_data_dict)
            clean_data_dict['data_entered_on'] = datetime.now().date()
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
        else:
            return Response({'access':'denied'})

         
         
         
         

@api_view(['POST' , 'GET'])         
def handle_owner_details(request):
    header_info = request.META
    if request.method == 'POST':
        if 'HTTP_BEARER_TOKEN' in header_info.keys():
           
            token_from_res = header_info['HTTP_BEARER_TOKEN']
            print(f'token found from header {token_from_res}')
            if token_from_res == "":
                return Response({'token':"Null"})
            token_status , token_expiry , associated_user_id = check_token_validity(token_from_res , need_business_id=False)
            print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
            #checking if the token has expired with the help of the custom function check_token_expiry()
            if check_token_expiry(int(token_expiry)) == True:
                if token_status == True:
                    data_dict = clean_dict_to_serialize(dict(request.data))
                    data_dict['owner_id'] = associated_user_id
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
                return Response({'token':'expired'})
                

    
    
    
@api_view(['POST'])
def handle_owner(request):
    header_info = request.META
    if request.method =='POST':
        
        ip_of_host_from_header = header_info['REMOTE_ADDR']
        data = request.data
        clean_data_dict = clean_dict_to_serialize(dict(data))
        clean_data_dict['password'] = hash_pass(clean_data_dict['password'])
        clean_data_dict['date_of_entry'] = datetime.now().date()
        print(f'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ password has been hashed bro')
        #print(f'{data} ============================================= {type(data)}')
        print(f'{clean_data_dict} ============================================= {type(clean_data_dict)}')
        serializer = OwnerSerializer(data = clean_data_dict)
        if serializer.is_valid():
            user_token = gen_token()
            user_token_expiry = expiry_time_calc(30)
            user_auth = auth(user_name=data['name'], user_email=data['email'], token=user_token , token_expiry = user_token_expiry , user_ip = ip_of_host_from_header , user_password = clean_data_dict['password'])
            user_auth.save()
            serializer.save()
            return Response({'user added':True , 'generated token':user_token})
        else:
            serializer_error_dict = dict(serializer.errors)
            error_list_for_response =[]
            for error in serializer_error_dict.keys():
                error_list_for_response.append(serializer_error_dict[error][0])
            return Response({'error':error_list_for_response})
    if request.method == 'GET':
        if 'HTTP_BEARER_TOKEN' in header_info.keys():
            token_from_header = header_info['HTTP_BEARER_TOKEN']
            if token_from_header == "":
                return Response({'token':'NULL'})
        token_status , token_expiry , associated_business_id = check_token_validity(token_from_header)
        print(f'{token_status} -+ -+ -+ -+ -+ {token_expiry} -+ -+ -+ -+ -+ {associated_business_id}')
        if token_status == True:
            data = request.data


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
def handle_store_inventory(request):
    if request.method == 'POST':
        header_info = request.META
        
        if 'HTTP_BEARER_TOKEN' in header_info.keys():
            token_from_header = header_info['HTTP_BEARER_TOKEN']
            print(f'Token found from store-inventory api header {token_from_header} ')
            if token_from_header == '':
                return Response({'token':'null'})
            
            
            token_status , token_expiry , associated_owner_id_token = check_token_validity(token_from_header , need_business_id=False)
            
            
            if token_status == True:
                
                store_inventory_data_dict = clean_dict_to_serialize(dict(request.data))
                store_inventory_data_dict['store_owner'] = associated_owner_id_token
                store_inventory_data_dict['updated_at'] = datetime.now()
                
                store_owner_from_db_relation = list(storeMaster.objects.filter(pk = store_inventory_data_dict['associated_store']).values('associated_owner'))[0]['associated_owner']
                print(f'Store Owner ID from Database StoreMaster and Owner Model relation is {store_owner_from_db_relation}')
                
                if associated_owner_id_token == str(store_owner_from_db_relation):
                    store_inventory_data_dict['store_owner'] = store_owner_from_db_relation
                    store_inventory_data_dict['updated_at'] = datetime.now()
                    
                    #getting the associated business id of the owner related the store from the api request data.
                    store_owner = Owner.objects.get(pk=store_owner_from_db_relation)
                    associated_business_id_store_owner = store_owner.business.pk
                    print(f'{associated_business_id_store_owner} ++++++++++++++++++++++++++++++++++++++++++++++++++++++ ')
                    business_and_store_product_management_status = store_and_business_inventory_logic(store_inventory_data_dict , associated_business_id_store_owner)
                    
                    serializer = StoreInventorySerializer(data = store_inventory_data_dict)
                    if serializer.is_valid() == True:
                        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                        print()
                        print(f' {store_inventory_data_dict["product_quantity"]} {store_inventory_data_dict["product_name"]} has been removed from BUSINESS {associated_business_id_store_owner} owned by {store_owner_from_db_relation} and added to STORE {store_inventory_data_dict["associated_store"]}  ')
                        
                        
                        return Response({'Owner Id':associated_owner_id_token , 'Business Id':associated_business_id_store_owner , 'store_data':store_inventory_data_dict})
                    else:
                        serializer_error_dict = dict(serializer.errors)
                        error_list_for_response =[]
                        for error in serializer_error_dict.keys():
                            error_list_for_response.append(serializer_error_dict[error][0])
                        return Response({'error':error_list_for_response})
                else:
                    return Response({'store_access':'Denied' , 'User Id From Token': associated_owner_id_token , 'User ID from Db relation':store_owner_from_db_relation})
            
            if token_status == False:
                return Response({'token':'invalid'})




#--------------------------------------------------------FOR SALES PAGE , ITS WITHOUT TOKEN AUTHENTICATION FOR NOW ---------------------------------            
@api_view(['POST'])
def handle_customer_details(request):
    
    if request.method == 'POST':
        
        data = request.data
        data_dict =clean_dict_to_serialize(dict(data))
        
        if 'name' in data_dict.keys() or 'contact' in data_dict.keys():
            
            
            if 'contact' != '':
                customer = Customer.objects.filter(contact = data_dict['contact']).values('name' , 'address')
                
                name = customer[0]['name']
                address = customer[0]['address']
                
                return Response({'name': name , 'address': address})

            if 'name' != '':
                
                customer = Customer.objects.filter(name = data_dict['name']).values('contact' , 'address')
                
                contact = customer[0]['contact']
                address = customer[0]['address']
                
                return Response({'customer_contatc' : contact , 'customer_address':address})

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




@api_view(['POST'])
def handle_sales_register(request):



    last = GenBill.objects.filter(store=1).order_by('-pk').first().bill_id
    
    
    
    if request.method =='POST':
        data_dict = clean_dict_to_serialize(dict(request.data))
        bill_from_store = GenBill.objects.filter(store=data_dict['store']).order_by('-pk').values('pk' , 'bill_id').first()
        print('6566666666666666666666666666666666666666666666666666666666666666')
        print(f'{data_dict["business"]} ======== {data_dict["store"]}  ============{data_dict["employee"]}')

        if bill_from_store == None:
            new_bill_id = 1
            generate_bill_dict = {'bill_id' : new_bill_id, 'time' : datetime.now() , 'store' : int(data_dict['store']) }
            
        else:
            new_bill_id = int(bill_from_store['bill_id']) +1
            generate_bill_dict = {'bill_id' : new_bill_id, 'time' : datetime.now(), 'store' : int(data_dict['store'])}
            
        genBillSerializer = GenerateBillSerializer(data=generate_bill_dict)
        if genBillSerializer.is_valid():
            genBillSerializer.save()
        #sleep(5)
        data_from_sales_pending = SalesPending.objects.filter(business = int(data_dict['business']) , store = int(data_dict['store']) , employee=int(data_dict['employee']) ).values( 'business' ,'store' , 'employee' ,'product' , 'gst' , 'product_quantity' , 'product_name' , 'mrp' , 'purchase_rate' , 'sale_rate' , 'row_total')
        pprint(list(data_from_sales_pending))
        
        data_from_sales_pending_with_bill_id = []
        for sales_pending_dict in list(data_from_sales_pending):
            sales_pending_dict['bill_ID'] = bill_from_store['pk']
            sales_pending_dict['bill_no'] = bill_from_store['bill_id']
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
            SalesPending.objects.filter(business = data_dict['business'] , store = data_dict['store'] , employee=data_dict['employee'] ).delete()
            print('Data has been removed from sales pending successfully')

            #handling of removal of purchased products from  store Inventory

            return Response({'data':list(data_from_sales_pending_with_bill_id)})
        else:
            return Response(sales_register_serializer.errors)
        
        
@api_view(['POST'])
def handle_sales_pending(request):

    if request.method == 'POST':
        
        data_dict = clean_dict_to_serialize(dict(request.data))
        #serializer = SalesPendingSerializer
        product_id_from_api = data_dict['product']
        product_data = Product.objects.filter(pk=int(product_id_from_api)).values('name' , 'MRP' , 'purchase_rate' , 'sale_rate' , 'gst')
        if len(product_data) != 0:

                
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




