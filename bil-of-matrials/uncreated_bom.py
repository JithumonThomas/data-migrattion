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

rec = [32461,32466,32061,63038,30760,30753,30677,43472,47725,32120,32105,32096,32074,32068,31520,31486,31370,31980,31295,31722,31532,31684,31655,31978,31533,31512,31447,31339,31603,31506,31513,31976,31531,31530,31529,31519,31349,31973,31778,31601,31690,31493,31647,31694,31278,31275,31518,31517,31510,31934,31314,31336,31820,31505,32458,50298,63080,47460,63041,46050,46052,32255,50249,31958,31856,31746,31910,31418,30795,31449,31805,30905,30871,32106,31591,31741,31796,32132,31861,31593,32360,49990,32012,31263,63082,43374,31290,31632,31708,32002,31548,31546,31523,31999,31715,31728,31638,31618,31972,31282,32418,31555,31587,48962,50251,51102,51114,51126,58514,63056,31830,51732,31633,31258,31611,31384,30925,31028,31069,56702,56717,56698,56712,57301,56827,56678,56707,58094,56693,56688,62903,62688,44616,45303,62734,62657,62679,62496,62499,62634,62728,62810,62813,62749,62746,43463,58616,58619,58622,58613,58610,58607,58589,58592,58595,58598,58601,58604,58047,57942,57911,57990,58011,58035,57921,57999,57744,62794,57963,58059,58041,57927,58005,57984,58065,58017,57918,57996,57978,58062,57860,62697,62706,62722,62725,30889,32152,31421,32477,31566,31781,31896,31624,31834,58981,58984,58987,58990,31470,57945,57753,57747,57936,57939,58996,57759,58993,58999,59002,59005,59008,31460,63088,58008,58026,58029,57960,57948,58014,58032,57966,58038,58571,58050,58577,58020,57957,58044,57975,57993,59303,57987,58002,58574,58580,58583,58586,32289,58179,31259,31267,31445,32315,32309,31413,30988,63117,32121,32367,55724,55503,55506,55509,55512,55632,59642,59215,59165,59264,59117,59069,58144,58250,58121,58271,58182,58206,58228,50672,63063,56904,56917,56945,56956,56856,56892,56968,57615,57495,56978,56931,56868,56880,60425,60463,60706,31792,31215,31812,58068,58077,60271,60436,63066,30695,31726,31849,32467,31660,32180,32320,30634,32465,32464,31220,30665,30855,30941,31121,32448,31887,31929,31659,31724,58360,58375,58338,58349,58453,58464,58475,58494,58292,58303,58314,58326,58412,58433,58390,58401,57638,57535,57341,57633,57715,57720,57553,57710,57627,57672,57678,57547,57725,57730,57735,57403,57703,57660,57666,57520,57652,31151,31758,32184,30893,31382,31649,31653,32303,59298,58167,58173,58138,58110,58161,58099,63091,57006,56779,57330,57014,56789,56755,56766,56991,56738,56750,56720,56795,57024,57508,56806,57306,56743,56812,57035,56820,57846,56170,63263,31485,31908,30513,59313,59380,62682,59449,62528,31871,43439,59466,62816,62784,62797,62737,62731,62709,62752,62629,59434,59439,62691,62700,32271,31744,31750,32264,57270,43411,32345,32296,57432,51029,57590,63172,56854]
fields=['product_id','code','type','product_name','product_uom','prenote','bom_lines','routing_id','product_qty','mrp_bom_operations_product_ids','sub_products','fixed_by','fixed_date']

with open('bill_of_uncreated_rec.csv', 'w', newline='') as file:
    count = 0
    for bill_record in rec:
       
        bill = sock.execute_kw(dbname, uid, pwd,'mrp.bom', 'read', [bill_record],{'fields': fields})
       
        product_id = False
        
        if bill['product_id']:
           
            pro_code = bill['product_id'][1]
            # print(pro_code)
        
            default_id = models.execute_kw(db, u_id, password,'product.product', 'search', [[['active','=',False],['default_code','=',pro_code]]])
            
            
            if default_id:
                product_id = default_id[0]
                temp = models.execute_kw(db, u_id, password,'product.template', 'write', [[product_id],{'default_code':pro_code}])
            else:
                print(bill['product_id'][0])
                
        
        # operations_product_ids = False
        # if bill['mrp_bom_operations_product_ids']:
        
        #     operations_product_ids = []
        #     for id in bill['mrp_bom_operations_product_ids']:
                
        #         bom_operations =  sock.execute_kw(dbname, uid, pwd,'mrp.bom.operations.product', 'read', [id])
        #         # ope = models.execute_kw(db, u_id, password,'mrp.routing.workcenter', 'search_read', [[['name','=',bom_operations['operation_id'][1]]]])
                
        #         operations = bom_operations['operation_id'][1] or False
            
        #         workcenter= models.execute_kw(db, u_id, password,'mrp.workcenter', 'search_read', [[['name','=',bom_operations['workcenter_id'][1]]]])
                
        #         #  workcenter = sock.execute_kw(dbname, uid, pwd,'mrp.workcenter', 'read', [bom_operations['workcenter_id'][0]])
        #         ids = workcenter[0]['id'] if workcenter else False
            
        
               
                        
        #         val = {
        #             'name':operations or False,
        #             'workcenter_id':ids,
        #             'time_cycle_manual':bom_operations['hour']
        #         }
        #         line = (0,0, val)
        #         operations_product_ids.append(line)
        # bom_lines =  False
        # if bill['bom_lines']:
            
        #     bom_lines = []
            
        #     bom_compo =  sock.execute_kw(dbname, uid, pwd,'mrp.bom', 'read', [bill['bom_lines']])
            
        #     for bom_co in bom_compo:
            
        #         pro_code = bom_co['product_id'][1]
                
        #         product =  models.execute_kw(db, u_id, password,'product.product', 'search', [[['default_code','=',pro_code]]])
                
        #         uom = models.execute_kw(db, u_id, password,'uom.uom', 'search_read', [[['name','=',bom_co['product_uom'][1]]]])
        #         uom_id = uom[0]['id'] if uom else False
        #         if product:
        #             val = {
        #                         'product_id':product[0],
        #                         'product_uom_id':uom_id,
        #                         'description':bom_co['product_name'],
        #                         'product_qty':bom_co['product_qty'] or False


        #                     }
               
        #         line = (0, 0, val)
        #         bom_lines.append(line)
    
        # value = {
        #         'product_id':product_id,
        #         'code':bill['code'],
        #         'type':bill['type'],
        #         'bom_line_ids':bom_lines,
        #         'operation_ids':operations_product_ids,
        #         'product_tmpl_id':product_id
        #     }
        # print(value)
        # try:
        #     bom = models.execute_kw(db, u_id, password,'mrp.bom', 'create', [value])
        #     count += 1
        #     print("Record :-" ,count ,"created")
        # except BaseException as error:
        
        #         writer = csv.writer(file)
        #         writer.writerow([bill['id'],bill['product_id'], error])
               
        #         print('An exception occurred: {}'.format(error))
        
       
   





    
