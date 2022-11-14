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
bom_rec = [49990,48962,51114,32152]
fields=['product_id','code','type','product_name','product_uom','prenote','bom_lines','routing_id','product_qty','mrp_bom_operations_product_ids','sub_products','fixed_by','fixed_date']

with open('bill_of_uncreated_rec_new.csv', 'w', newline='') as file:
    count = 0
    print()
    for bill_record in bom_rec:
       
        bill = sock.execute_kw(dbname, uid, pwd,'mrp.bom', 'read', [bill_record],{'fields': fields})
       
        product_id = False
        
        if bill['product_id']:
           
            pro_code = bill['product_id'][1]
            temp = models.execute_kw(db, u_id, password,'product.template', 'search_read', [[['default_code','=',pro_code]]])
            
            temp_id = temp[0]['id'] if temp  else False
           
            pro_active = models.execute_kw(db, u_id, password,'product.product', 'search', [[['default_code','=',pro_code]]])
            pro_inactive = models.execute_kw(db, u_id, password,'product.product', 'search', [[['active','=',False],['default_code','=',pro_code]]])
            
            if pro_active or pro_inactive:
                product_id = pro_active or pro_inactive
            
       
        
        operations_product_ids = False
        if bill['mrp_bom_operations_product_ids']:
        
            operations_product_ids = []
            for id in bill['mrp_bom_operations_product_ids']:
                
                bom_operations =  sock.execute_kw(dbname, uid, pwd,'mrp.bom.operations.product', 'read', [id])
                # ope = models.execute_kw(db, u_id, password,'mrp.routing.workcenter', 'search_read', [[['name','=',bom_operations['operation_id'][1]]]])
                
                operations = bom_operations['operation_id'][1] or False
                # print(bom_operations['workcenter_id'])
                
                workcenter= models.execute_kw(db, u_id, password,'mrp.workcenter', 'search_read', [[['name','=',bom_operations['workcenter_id'][1]]]])
                
                #  workcenter = sock.execute_kw(dbname, uid, pwd,'mrp.workcenter', 'read', [bom_operations['workcenter_id'][0]])
                ids = workcenter[0]['id'] if workcenter else False
            
        
               
                        
                val = {
                    'name':operations or False,
                    'workcenter_id':ids,
                    'time_cycle_manual':bom_operations['hour']
                }
                line = (0,0, val)
                operations_product_ids.append(line)
        bom_lines =  False
        if bill['bom_lines']:
            
            bom_lines = []
            
            bom_compo =  sock.execute_kw(dbname, uid, pwd,'mrp.bom', 'read', [bill['bom_lines']])
            
            for bom_co in bom_compo:
            
                pro_code = bom_co['product_id'][1]
                
                # print(pro_code)
                pro_active_line = models.execute_kw(db, u_id, password,'product.product', 'search', [[['default_code','=',pro_code]]])
                pro_inactive_line = models.execute_kw(db, u_id, password,'product.product', 'search', [[['active','=',False],['default_code','=',pro_code]]])
           
                uom = models.execute_kw(db, u_id, password,'uom.uom', 'search_read', [[['name','=',bom_co['product_uom'][1]]]])
                uom_id = uom[0]['id'] if uom else False
                
                
                if pro_active_line or pro_inactive_line:
                    val = {
                                'product_id':False,
                                'product_uom_id':uom_id,
                                'description':bom_co['product_name'],
                                'product_qty':bom_co['product_qty'] or False
                            }
                    if pro_active_line:
                        d1 = { 'product_id':  pro_active_line[0]}
                        val.update(d1)
                    if pro_inactive_line:
                        d1 = { 'product_id':  pro_inactive_line[0]}
                        val.update(d1)
                line = (0, 0, val)
                bom_lines.append(line)
           
        value = {
                'product_id':product_id[0] if product_id else False,
                'code':bill['code'],
                'type':bill['type'],
                'bom_line_ids':bom_lines,
                'operation_ids':operations_product_ids,
                'product_tmpl_id':temp_id
            }
        # print(value)
        try:
            bom = models.execute_kw(db, u_id, password,'mrp.bom', 'create', [value])
            count += 1
            print("Record :-" ,count ,"created")
        except BaseException as error:
        
                writer = csv.writer(file)
                writer.writerow([bill['id'],bill['product_id'], error])
               
                print('An exception occurred: {}'.format(error))
        
       
   





    
