
from  xmlrpc import client
import xmlrpc.client
import csv
username = 'admin'
pwd = '@Adamson#ERP'
dbname = 'adamson_oct19_2022'
sock_common = client.ServerProxy('http://adamson.dev.bds.space/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)
sock = client.ServerProxy('http://adamson.dev.bds.space/xmlrpc/object')


url = 'http://3.109.84.120:5079'
db = 'Adamson15-Base-test-migrate'
user = 'admin'
password = '@Ad@m$0n*#135'
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
u_id = common.authenticate(db, user, password, {})
version = common.version()
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))





both_records = sock.execute_kw(dbname, uid, pwd, 'res.partner', 'search',[[['supplier','=',True],['customer','=',True]]])

customer_records = sock.execute_kw(dbname, uid, pwd, 'res.partner', 'search',[[['customer','=',True],['supplier','=',False]]])
suppliers_records = sock.execute_kw(dbname, uid, pwd, 'res.partner', 'search',[[['supplier','=',True],['customer','=',False]]])

suppliers_records_only = set(suppliers_records) - set(both_records)
customer_records_only = set(customer_records) - set(both_records)


fields = ['id','is_company','type','image','category_id','name','ref','payment_responsible_id',
        'supp_name','receiving_person_id','street','street2','city','state_id','zip','country_id','website','phone','phone2','mobile','fax','email','user_id','section_id',
        'lang','date','vat_number','customer','supplier','carrier','insurance_amount','active',
        'opt_out','notification_email_send','stock_customer_rentals','rent_pricelist','property_product_pricelist','property_product_pricelist_purchase',
        'property_stock_outsourcing','property_stock_customer','property_stock_supplier','ship_method_ids',
        'payment_next_action','unreconciled_aml_ids','bank_ids',
        'property_account_receivable','property_account_payable','sale_warn','purchase_warn','picking_warn','invoice_warn','comment','child_ids','function','title','parent_id']
    


def create_value(data): 
    
    contact_ids_list = False
    if data['child_ids']:
        
        contact_ids_list = []
        for id in data['child_ids']:
            
            contact_ids_old = sock.execute_kw(dbname, uid, pwd,'res.partner', 'search', [[['id', '=', id]]])
            contact = sock.execute_kw(dbname, uid, pwd,'res.partner', 'read', [contact_ids_old])[0] if contact_ids_old else False
           
            if contact:
                
                partner_contact = models.execute_kw(db, u_id, password,'res.partner', 'search_read', [[['name', '=', contact['name']]]])
                
                partner_contact_ids = partner_contact[0]['id'] if partner_contact  else False
                if partner_contact_ids:
                    
                    contact_ids_list.append(partner_contact_ids)
                    
                
    partner_login = False
    if data['user_id']:    
       
        partner_user_old = sock.execute_kw(dbname, uid, pwd,'res.users', 'search', [[['id', '=', data['user_id'][0]]]])
        
        partner_user = sock.execute_kw(dbname, uid, pwd,'res.users','read', [partner_user_old])
        
        partner_login =  partner_user[0]['login'] if partner_user else False
        user_id = partner_login
        if partner_login:
           
            res_user = models.execute_kw(db, u_id, password,'res.users', 'search_read', [[['login', '=', partner_login]]])
            
            user_id = res_user[0]['id'] if res_user else False
        
        
   
       
    if data['title']:
        
        partner_title = models.execute_kw(db, u_id, password,'res.partner.title', 'search_read', [[['name', '=', data['title'][1]]]])
        title = partner_title[0]['id'] if  partner_title else False
        if not partner_title:
            title_old = sock.execute_kw(dbname, uid, pwd,'res.partner.title', 'search', [[['id', '=', data['title'][0]]]])
            result = sock.execute_kw(dbname, uid, pwd,'res.partner.title', 'read', [title_old])
            val = {
                    'shortcut':result[0]['shortcut'],
                    'name':result[0]['name'],
            }
            title =  models.execute_kw(db, u_id, password,'res.partner.title', 'create', [val])

    if data['state_id']:
        
        partner_state = models.execute_kw(db, u_id, password,'res.country.state', 'search_read', [[['name', '=', data['state_id'][1]]]])
        state_id = partner_state[0]['id'] if  partner_state else False
      
        if not partner_state: 
            
            state_old = sock.execute_kw(dbname, uid, pwd,'res.country.state', 'search', [[['name', '=', data['state_id'][1]]]])
            
            result = sock.execute_kw(dbname, uid, pwd,'res.country.state', 'read', [state_old])
            
            val = {
                'name':result[0]['name'],
                'code':result[0]['code'],
                'country_id':result[0]['country_id'][0]
            }
           
            state_id =  models.execute_kw(db, u_id, password,'res.country.state', 'create', [val])
    country_id = False
    if data['country_id']:
     
        partner_country = models.execute_kw(db, u_id, password,'res.country', 'search_read', [[['name', '=', data['country_id'][1]]]])
        
        country_id = partner_country[0]['id'] if  partner_country else False
        
    category_list = False
    if data['category_id']:
        
        category_list = []
        for id in data['category_id']:
            
            category_old = sock.execute_kw(dbname, uid, pwd,'res.partner.category', 'search', [[['id', '=', id]]])
            cate = sock.execute_kw(dbname, uid, pwd,'res.partner.category', 'read', [category_old])[0] if category_old else False
            
            
            if cate:
               
                partner_cate = models.execute_kw(db, u_id, password,'res.partner.category', 'search_read', [[['name', '=', cate['name']]]])
                category_id = partner_cate[0]['id'] if partner_cate  else False
               
                if not partner_cate:
                    
                    val = {
                        'name':cate['name'],
                        'active':cate['active'] 
                    }
            
                    category_id = models.execute_kw(db, u_id, password,'res.partner.category', 'create', [val])
                
                    category_list.append(category_id)
                else:
                     partner_cate_id = partner_cate[0]['id'] 
                     category_list.append(partner_cate_id)
           
       

    parent_id  =False
    if data['parent_id']:
      
        partner_parent_id = models.execute_kw(db, u_id, password,'res.users', 'search_read', [[['name', '=', data['parent_id'][1]]]])
        parent_id  = partner_parent_id[0]['id'] if partner_parent_id  else False
        

    value = {
        'image_1920':  data['image'] if  data['image'] else False,
        'child_ids': [(6, 0, contact_ids_list)] if contact_ids_list else False,
        'user_id':user_id if partner_login else False,
        'is_company':data['is_company'],
        'customer_rank':1 if data['customer'] else 0,
        'supplier_rank': 1 if data['supplier'] else 0 ,
        'name':data['name'],
        'type':False if data['type']=='default' or data['type']=='sales_representative' else data['type'],
        'street': data['street'] ,
        'street2':data['street2'],
        'city':data['city'] ,
        'zip':data['zip'] ,
        'state_id':state_id if data['state_id'] else False,
        'country_id':country_id if data['country_id'] else False,
        'vat':data['vat_number'] ,
        'category_id':[(6,0,category_list)] if category_list else False,
        'phone':data['phone'],
        'mobile':data['mobile'],
        'email':data['email'],
        'website':data['website'],
        'lang':data['lang'],  
        'team_id':1 if data['section_id'] else False,
        # 'property_product_pricelist':data['property_product_pricelist'][0] if data['property_product_pricelist'] else False,
        'ref':data['ref'],
      
        # 'payment_next_action':data['payment_next_action'][0] if data['payment_next_action'] else False,
        # 'unreconciled_aml_ids':data['unreconciled_aml_ids'][0] if data['unreconciled_aml_ids'] else False,
        # 'bank_ids':data['bank_ids'][0] if data['bank_ids'] else False,
        # 'property_account_receivable_id':data['property_account_receivable'][0] if data['property_account_receivable'] else False,
        # 'property_account_payable_id':data['property_account_payable'][0] if data['property_account_payable'] else False,
        'sale_warn':data['sale_warn'] if data['sale_warn'] else False,
        'purchase_warn':data['purchase_warn'] if data['purchase_warn'] else False,
        'picking_warn':data['picking_warn'] if data['picking_warn'] else False,
        'invoice_warn':data['invoice_warn'] if data['invoice_warn'] else False,
        'comment':data['comment'],
        'function':data['function'][1] if data['function'] else False,
        'title':title  if data['title'] else False,
        'parent_id': parent_id if parent_id else False,
    }   
    
    try:
        models.execute_kw(db, u_id, password,'res.partner', 'create', [value])
    except BaseException as error:
       
            writer = csv.writer(file)
            writer.writerow([data['id'],value['name'], error])
            print(data['id'])
            print('An exception occurred: {}'.format(error))
# ---------------------------------------Both Records--------------------------------------
with open('data_migration_error.csv', 'w', newline='') as file:
    # for both_record in both_records:
    #     both = sock.execute_kw(dbname, uid, pwd,'res.partner', 'read', [both_record],{'fields': fields})  
    #     create_value(both)  
    # ---------------------------------------suppliers_records---------------------------------------
    # for suppliers_record in suppliers_records_only:
    #     suppliers = sock.execute_kw(dbname, uid, pwd,'res.partner', 'read', [suppliers_record],{'fields': fields})
    
    #     create_value(suppliers)  

    # # ---------------------------------------customer_records---------------------------------------
    for customer_record in customer_records_only:
            customer = sock.execute_kw(dbname, uid, pwd,'res.partner', 'read', [customer_record],{'fields': fields})     
            create_value(customer)  
    
    
    
