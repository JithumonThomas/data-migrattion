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


# test = sock.execute_kw(dbname, uid, pwd, 'res.partner', 'search',[[['id','=',9330]]])
# print(test)
rec = sock.execute_kw(dbname, uid, pwd, 'res.partner', 'search',[[]])

records = sock.execute_kw(dbname, uid, pwd, 'res.partner', 'search',[[['parent_id',"!=",False],['is_company','=',True]]])



fields = ['id','is_company','type','image','category_id','name','ref','payment_responsible_id',
        'supp_name','receiving_person_id','street','street2','city','state_id','zip','country_id','website','phone','phone2','mobile','fax','email','user_id','section_id',
        'lang','date','vat_number','customer','supplier','carrier','insurance_amount','active',
        'opt_out','notification_email_send','stock_customer_rentals','rent_pricelist','property_product_pricelist','property_product_pricelist_purchase',
        'property_stock_outsourcing','property_stock_customer','property_stock_supplier','ship_method_ids',
        'payment_next_action','unreconciled_aml_ids','bank_ids',
        'property_account_receivable','property_account_payable','sale_warn','purchase_warn','picking_warn','invoice_warn','comment','child_ids','function','title','parent_id']
    


def write_value(data):
    
    if data['parent_id']:
      
        partner = models.execute_kw(db, u_id, password,'res.partner', 'search_read', [[['name', '=', data['parent_id'][1]],['type','=',False],['is_company','=',False]]])
        id= partner[0]['id'] if partner else False
   
        if id:
            print(len(partner))
            print(data['parent_id'])
            if len(partner) > 1:
                print(data['parent_id'])
                print(id)
            # vals = {
            #     'parent_id': id
            # }
            # parent_id  =False
            # print(len(partner))
            # if len(partner) == 1:
            #     try:
            #         models.execute_kw(db, u_id, password,'res.partner','write', [[id],vals])
            #     except BaseException as error:
                       
            #             writer.writerow([data['id'],data['name'], error])
            #             print(data['id'])
            #             print('An exception occurred: {}'.format(error))
            # else:
            #     print("id ->" , id)
            # # print("vals",vals)
with open('data_migration_write.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for record in records:
            both = sock.execute_kw(dbname, uid, pwd,'res.partner', 'read', [record],{'fields': fields})  
            write_value(both)  
    # ---------------------------------------suppliers_records---------------------------------------
    # for suppliers_record in suppliers_records_only:
    #     suppliers = sock.execute_kw(dbname, uid, pwd,'res.partner', 'read', [suppliers_record],{'fields': fields})
    
    #     write_value(suppliers)  

    # # # ---------------------------------------customer_records---------------------------------------
    # for customer_record in customer_records:
    #         customer = sock.execute_kw(dbname, uid, pwd,'res.partner', 'read', [customer_record],{'fields': fields})     
    #         write_value(customer)  