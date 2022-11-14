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
pwd = '@Adamson#ERP'
dbname = 'adamson_oct19_2022'
sock_common = client.ServerProxy('http://adamson.dev.bds.space/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)
sock = client.ServerProxy('http://adamson.dev.bds.space/xmlrpc/object')

db ='Adamson15-Base-test-migrate'
user = 'admin'
password = '@Ad@m$0n*#135'
common = client.ServerProxy('http://3.109.84.120:5079/xmlrpc/common', allow_none=True)
u_id = common.login(db, user, password)
models = client.ServerProxy('http://3.109.84.120:5079/xmlrpc/object')

# 32153
bill_of_materials = sock.execute_kw(dbname, uid, pwd, 'mrp.bom', 'search',[[]])
print(bill_of_materials.index(32421))

exit()
fields=['product_id','code','type','product_name','product_uom','prenote','bom_lines','routing_id','product_qty','mrp_bom_operations_product_ids','sub_products','fixed_by','fixed_date']
with open('bill_of_records_error.csv', 'w', newline='') as file:
    count = 0
    for bill_record in bill_of_materials:
        count += 1
        print(count)
       
        bill = sock.execute_kw(dbname, uid, pwd,'mrp.bom', 'read', [bill_record],{'fields': fields})
        print("bill",bill['id'])
        product_id = False
        
        if bill['product_id']:
            
            pro_name = bill['product_id'][1]
            print(pro_name)
            temp = models.execute_kw(db, u_id, password,'product.template', 'search_read', [[['default_code','=',pro_name]]])
            print(temp)
            temp_id = temp[0]['id'] if temp  else False
           
            # exit()
            default_id = models.execute_kw(db, u_id, password,'product.product', 'search', [[['default_code','=',pro_name]]])
        
            # product = models.execute_kw(db, u_id, password,'product.product', 'read', [default_id])
            if default_id:
                product_id = default_id[0]
        
        operations_product_ids = False
        if bill['mrp_bom_operations_product_ids']:
            print("mrp_bom_operations_product_ids",bill['id'])
            operations_product_ids = []
            for id in bill['mrp_bom_operations_product_ids']:
                
                bom_operations =  sock.execute_kw(dbname, uid, pwd,'mrp.bom.operations.product', 'read', [id])
                # ope = models.execute_kw(db, u_id, password,'mrp.routing.workcenter', 'search_read', [[['name','=',bom_operations['operation_id'][1]]]])
                
                operations = bom_operations['operation_id'][1] or False
            
                workcenter= models.execute_kw(db, u_id, password,'mrp.workcenter', 'search_read', [[['name','=',bom_operations['workcenter_id'][1]]]])
                
                ids = workcenter[0]['id'] or False
            
        
                workcenter = sock.execute_kw(dbname, uid, pwd,'mrp.workcenter', 'read', [bom_operations['workcenter_id'][0]])
                        
                val = {
                    'name':operations or False,
                    'workcenter_id':ids,
                }
                line = (0,0, val)
                operations_product_ids.append(line)
        bom_lines =  False
        if bill['bom_lines']:
            print("bom_lines",bill['id'])
            bom_lines = []
            
            bom_compo =  sock.execute_kw(dbname, uid, pwd,'mrp.bom', 'read', [bill['bom_lines']])
            
            for bom_co in bom_compo:
            
                pro_name = bom_co['product_id'][1]
                
                product =  models.execute_kw(db, u_id, password,'product.product', 'search', [[['default_code','=',pro_name]]])
                
                uom = models.execute_kw(db, u_id, password,'uom.uom', 'search_read', [[['name','=',bom_co['product_uom'][1]]]])
                uom_id = uom[0]['id'] if uom else False
                
                val = {
                            'product_id':product[0] or False,
                            'product_uom_id':uom_id,
                            'description':bom_co['product_name'],
                            'product_qty':bom_co['product_qty'] or False

                        }
                line = (0, 0, val)
                bom_lines.append(line)
    
        value = {
                'product_id':product_id,
                'code':bill['code'],
                'type':bill['type'],
                'bom_line_ids':bom_lines,
                'operation_ids':operations_product_ids,
                'product_tmpl_id':temp_id
            }
        print(value)
        exit()
        # try:
        #     bom = models.execute_kw(db, u_id, password,'mrp.bom', 'create', [value])
        # except BaseException as error:
        
        #         writer = csv.writer(file)
        #         writer.writerow([bill['id'],value['product_id'], error])
        #         print(bill['id'])
        #         print(bill)
        #         print('An exception occurred: {}'.format(error))
    # bom = models.execute_kw(db, u_id, password,'mrp.bom', 'create', [value])
   





    

