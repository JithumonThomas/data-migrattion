from  xmlrpc import client
import xmlrpc.client
import csv
username = 'admin'
pwd = '@Ad@m$0n*#135'
dbname = 'adamson_oct19_2022'
sock_common = client.ServerProxy('http://adamson.dev.bds.space/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)
sock = client.ServerProxy('http://adamson.dev.bds.space/xmlrpc/object')



db ='Adamson15-Base_nov8_migrated'
user = 'admin'
password = 'admin*#1234'
common = client.ServerProxy('http://3.109.84.120:5079/xmlrpc/common', allow_none=True)
u_id = common.login(db, user, password)
models = client.ServerProxy('http://3.109.84.120:5079/xmlrpc/object')

# 32153
bill_of_materials = sock.execute_kw(dbname, uid, pwd, 'mrp.bom', 'search',[[('bom_id','=',False)]])

# print(len(bill_of_materials))
# exit()
length = len(bill_of_materials)
count = 0
fields=['product_id','code','type','product_name','product_uom','prenote','bom_lines','routing_id','product_qty','mrp_bom_operations_product_ids','sub_products','fixed_by','fixed_date']
count = 0
with open('bom_operation_write.csv', 'w', newline='') as file:
    bills = sock.execute_kw(dbname, uid, pwd,'mrp.bom', 'read', [bill_of_materials],{'fields': fields})
    for bill in bills:
        count +=1
        print(count)
        id = bill['id']
        
        product_id = False
      
        operations_product_ids = False
        if bill['mrp_bom_operations_product_ids']:
            pro_code = bill['product_id'][1]
           
            operations_product_ids = []
            for id in bill['mrp_bom_operations_product_ids']:
                
                bom_operations =  sock.execute_kw(dbname, uid, pwd,'mrp.bom.operations.product', 'read', [id])
        
                operations = bom_operations['operation_id'][1] or False
                workcenter= models.execute_kw(db, u_id, password,'mrp.workcenter', 'search_read', [[['name','=',bom_operations['workcenter_id'][1]]]])

                ids = workcenter[0]['id'] if workcenter else False
              
                val = {
                    'name':operations or False,
                    'workcenter_id':ids,
                    'time_cycle_manual':bom_operations['hour']
                }
                line = (0,0, val)
                operations_product_ids.append(line)
            value = {
               
                'operation_ids':operations_product_ids,
              
            }
          
            record = models.execute_kw(db, u_id, password,'mrp.bom', 'search', [[['product_id', '=', pro_code]]])
            print(record)
            if not record:
                print("======>",bill['product_id'])
            try:
                models.execute_kw(db, u_id, password,'mrp.bom','write', [record,value])

            except BaseException as error:
            
                    writer = csv.writer(file)
                    writer.writerow([bill['id'],bill['product_id'], error])
                
                    print('An exception occurred: {}'.format(error))