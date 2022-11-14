from  xmlrpc import client
import xmlrpc.client
import csv
# username = 'admin'
# pwd = 'admin'
# dbname = 'Adamson_nov_22'
# sock_common = client.ServerProxy('http://localhost:8069/xmlrpc/common')
# uid = sock_common.login(dbname, username, pwd)
# sock = client.ServerProxy('http://localhost:8069/xmlrpc/object')

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

with open('bill_of_records_error.csv', 'w', newline='') as file:
        bills = sock.execute_kw(dbname, uid, pwd,'mrp.bom', 'read', [bill_of_materials],{'fields': fields})
       
        for bill in bills:
            print(bill['id'])
            product_set = sock.execute_kw(dbname, uid, pwd,'mrp.routing',  'search',[[('product_id','=',bill['product_id'][1])]])

            routing = sock.execute_kw(dbname, uid, pwd,'mrp.routing', 'read', [3678],{'fields':['routing_line_ids','product_id']})
            routing_line_id = routing['routing_line_ids']
          
            work_center = sock.execute_kw(dbname, uid, pwd,'mrp.production.workcenter.line', 'read', [routing_line_id])
            print(len(work_center))
            exit()
            for work in work_center:
                print(work['time_run'])
            exit()