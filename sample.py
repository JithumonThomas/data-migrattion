from  xmlrpc import client
import xmlrpc.client
import csv

username = 'admin'
pwd = 'admin'
dbname = 'Adamson_nov_22'
sock_common = client.ServerProxy('http://localhost:8069/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)
sock = client.ServerProxy('http://localhost:8069/xmlrpc/object')


url = 'http://localhost:8007'
db = 'Adamson15-Base_nov5_22'
user = 'admin'
password = 'admin'
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
u_id = common.authenticate(db, user, password, {})
version = common.version()
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))



# both_records = sock.execute_kw(dbname, uid, pwd, 'res.partner', 'search',[[['supplier','=',True],['customer','=',True]]])

# customer_records = sock.execute_kw(dbname, uid, pwd, 'res.partner', 'search',[[['customer','=',True]]])
# suppliers_records = sock.execute_kw(dbname, uid, pwd, 'res.partner', 'search',[[['supplier','=',True]]])

# suppliers_records_only = set(suppliers_records) - set(both_records)
# customer_records_only = set(customer_records) - set(both_records)
both_records =  models.execute_kw(db, u_id, password,'res.partner', 'search_read', [[['name', '=','Customer']]])
fields = ['id','is_company','type','image','category_id','name','ref','payment_responsible_id',
        'supp_name','receiving_person_id','street','street2','city','state_id','zip','country_id','website','phone','phone2','mobile','fax','email','user_id','section_id',
        'lang','date','vat_number','customer','supplier','carrier','insurance_amount','active',
        'opt_out','notification_email_send','stock_customer_rentals','rent_pricelist','property_product_pricelist','property_product_pricelist_purchase',
        'property_stock_outsourcing','property_stock_customer','property_stock_supplier','ship_method_ids',
        'payment_next_action','unreconciled_aml_ids','bank_ids',
        'property_account_receivable','property_account_payable','sale_warn','purchase_warn','picking_warn','invoice_warn','comment','child_ids','function','title','parent_id']
    


def write_value(data):
    sup = models.execute_kw(db, u_id, password,'product.supplierinfo', 'search_read', [[['id', '=', 7]]])
    print(sup)
    exit()
    id = data['id'] 
 
    if data['parent_id']:
      
        partner_parent_id = models.execute_kw(db, u_id, password,'res.partner', 'search_read', [[['name', '=', data['parent_id'][1]]]])
      
       
       
        parent_id  = partner_parent_id[0]['id'] if partner_parent_id  else False
        # print(parent_id)
        # exit()
        vals = {
        'parent_id': parent_id
        }
        print(vals)
        models.execute_kw(db, u_id, password,'res.partner','write', [[id],vals])
        # print("vals",vals)
for both_record in both_records:
         
        write_value(both_record)  
   


   from  xmlrpc import client
import xmlrpc.client

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


bill_of_materials = sock.execute_kw(dbname, uid, pwd, 'mrp.bom', 'search',[[['id','=',32480]]])

fields=['product_id','code','type','product_name','product_uom','prenote','bom_lines','routing_id','mrp_bom_operations_product_ids','sub_products','fixed_by','fixed_date']
for bill_record in bill_of_materials:
   
    bill = sock.execute_kw(dbname, uid, pwd,'mrp.bom', 'read', [bill_record],{'fields': fields})
    product_id = False
    if bill['product_id']:
        pro_name = bill['product_id'][1]
        default_id = models.execute_kw(db, u_id, password,'product.product', 'search', [[['default_code','=',pro_name]]])
        # product = models.execute_kw(db, u_id, password,'product.product', 'read', [default_id])
        if default_id:
            product_id = default_id[0]
       
    operations_product_ids = False
    if bill['mrp_bom_operations_product_ids']:
       
        operations_product_ids = []
        for id in bill['mrp_bom_operations_product_ids']:
            
            bom_operations =  sock.execute_kw(dbname, uid, pwd,'mrp.bom.operations.product', 'read', [id])
            # ope = models.execute_kw(db, u_id, password,'mrp.routing.workcenter', 'search_read', [[['name','=',bom_operations['operation_id'][1]]]])
            
            operations = bom_operations['operation_id'][1] or False
            workcenter= models.execute_kw(db, u_id, password,'mrp.workcenter', 'search_read', [[['name','=',bom_operations['workcenter_id'][1]]]])
            
            ids = workcenter[0]['id']
           
       
            workcenter = sock.execute_kw(dbname, uid, pwd,'mrp.workcenter', 'read', [bom_operations['workcenter_id'][0]])
                     
            val = {
                'operation_ids':operations or False,
                'workcenter_id':ids,
            }
            line = (0, 0, val)
            operations_product_ids.append(line)
    print(operations_product_ids)
    if bill['bom_lines']:
        
        bom_lines = []
        
        for id in bill['bom_lines']:
        
            bom_compo =  sock.execute_kw(dbname, uid, pwd,'mrp.bom', 'read', [id])
            mrp_bom_line = models.execute_kw(db, u_id, password,'uom.uom', 'search_read', [[['name','=','PCE']]])
            
        val = {
                    'product_id':product_id,
                    'code':bill['code'],
                    'type':bill['type']
                    

                }
        line = (6, 0, val)
        bom_lines.append(line)
    print(bom_lines)

    value = {
        'product_id':
        'code','type','product_name','product_uom','prenote','bom_lines','routing_id','mrp_bom_operations_product_ids','sub_products','fixed_by','fixed_date
    }
    # if bill['routing_id']:
    #     print(bill)
        

    # 'product_qty':bom_compo['product_qty'] or False,
    #                 'product_uom':mrp_bom_line[0]['id'] or False,
    #                 'name':bom_compo['name'] or False,
    #                 'code':bom_compo['code'] or False,
                    





    

