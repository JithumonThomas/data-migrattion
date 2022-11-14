from  xmlrpc import client
import xmlrpc.client
import csv
username = 'admin'
pwd = 'admin'
dbname = 'Adamson_nov_22'
sock_common = client.ServerProxy('http://localhost:8069/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)
sock = client.ServerProxy('http://localhost:8069/xmlrpc/object')



db ='Adamson15-Base_nov8_migrated'
user = 'admin'
password = 'admin*#1234'
common = client.ServerProxy('http://3.109.84.120:5079/xmlrpc/common', allow_none=True)
u_id = common.login(db, user, password)
models = client.ServerProxy('http://3.109.84.120:5079/xmlrpc/object')

# 32153
bill_of_materials = sock.execute_kw(dbname, uid, pwd, 'mrp.bom', 'search',[[('bom_id','=',False)]])

fields=['product_id','code','type','product_name','product_uom','prenote','bom_lines','routing_id','product_qty','mrp_bom_operations_product_ids','sub_products','fixed_by','fixed_date']
count = 0
with open('bom_operation_write.csv', 'w', newline='') as file:
    bills = sock.execute_kw(dbname, uid, pwd,'mrp.bom', 'read', [bill_of_materials],{'fields': fields})
    for bill in bills:
       
        
        if bill['mrp_bom_operations_product_ids']:
            pro_code = bill['product_id'][1]
            record = models.execute_kw(db, u_id, password,'mrp.bom', 'search', [[['product_id', '=', pro_code]]])
            if not record:
                count +=1
                print(count)
                print("======> product ",bill['product_id'])
                print("======> bill ",bill['id'])
          
       
   





    
