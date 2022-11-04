from  xmlrpc import client
import xmlrpc.client
username = 'admin'
pwd = 'admin'
dbname = 'Adamson_nov_22'
sock_common = client.ServerProxy('http://localhost:8069/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)
sock = client.ServerProxy('http://localhost:8069/xmlrpc/object')


url = 'http://localhost:8007'
db = 'Adamson15_oct31_22_new'
user = 'admin'
password = 'admin'
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
u_id = common.authenticate(db, user, password, {})
version = common.version()
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

bill_of_materials = sock.execute_kw(dbname, uid, pwd, 'mrp.bom', 'search',[[]])

fields=['product_id','code','type','product_name','product_uom','prenote','bom_lines','routing_id','mrp_bom_opetration_product_ids','sub_products','fixed_by','fixed_date']
for bill_record in bill_of_materials:
    bill = sock.execute_kw(dbname, uid, pwd,'mrp.bom', 'read', [bill_record],{'fields': fields})
    if bill['routing_id']:
    	print(bill)  
    	exit()






    

