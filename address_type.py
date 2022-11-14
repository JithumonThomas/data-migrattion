from  xmlrpc import client
import xmlrpc.client
import csv


username = 'admin'
pwd = 'admin'
dbname = 'Adamson_nov_22'
sock_common = client.ServerProxy('http://localhost:8069/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)
sock = client.ServerProxy('http://localhost:8069/xmlrpc/object')



db ='Adamson15-Base-test-migrate'
user = 'admin'
password = '@Ad@m$0n*#135'
common = client.ServerProxy('http://3.109.84.120:5079/xmlrpc/common', allow_none=True)
u_id = common.login(db, user, password)
models = client.ServerProxy('http://3.109.84.120:5079/xmlrpc/object')


default_types = sock.execute_kw(dbname, uid, pwd, 'res.partner', 'search',[[['type','=','default'],['is_company','=',False]]])


fields = ['id','is_company','type','image','category_id','name','ref','payment_responsible_id',
        'supp_name','receiving_person_id','street','street2','city','state_id','zip','country_id','website','phone','phone2','mobile','fax','email','user_id','section_id',
        'lang','date','vat_number','customer','supplier','carrier','insurance_amount','active',
        'opt_out','notification_email_send','stock_customer_rentals','rent_pricelist','property_product_pricelist','property_product_pricelist_purchase',
        'property_stock_outsourcing','property_stock_customer','property_stock_supplier','ship_method_ids',
        'payment_next_action','unreconciled_aml_ids','bank_ids',
        'property_account_receivable','property_account_payable','sale_warn','purchase_warn','picking_warn','invoice_warn','comment','child_ids','function','title','parent_id']
    



def write_value(data):
   
    partner_type = models.execute_kw(db, u_id, password,'res.partner', 'search_read', [[['name', '=', data['name']],['type','=',False],['is_company','=',False]]])
    
   
    id= partner_type[0]['id'] if partner_type else False
   
    if id:
            vals = {
                'type': 'other'

            }
            try:
                models.execute_kw(db, u_id, password,'res.partner','write', [[id],vals])
            except BaseException as error:
                       
                    writer.writerow([data['id'],data['name'], error])
                    print(data['id'])
                    # print('An exception occurred: {}'.format(error))
           
with open('data_migration_type_write.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    count =0
    
    for default_type in default_types:
                both = sock.execute_kw(dbname, uid, pwd,'res.partner', 'read', [default_type],{'fields': fields})  
                write_value(both)
                count += 1
                print(count)