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




def create_product(da):
    
    count = 0
    for data in da:
        count +=1
        
        uom_po_id = False
        if data['uom_po_id']:
        
            uom_po = models.execute_kw(db, u_id, password,'uom.uom', 'search_read', [[['name','=',data['uom_po_id'][1]]]])
            uom_po_id = uom_po[0]['id']

        uom_id = False
        if data['uom_id']:
        
            uom = models.execute_kw(db, u_id, password,'uom.uom', 'search_read', [[['name','=',data['uom_id'][1]]]])
            uom_id = uom[0]['id']
        
        categ_id = False

        if data['categ_id']: 
            cat = sock.execute_kw(dbname, uid, pwd,'product.category', 'read', [data['categ_id'][0]])
        
            pro_cat = models.execute_kw(db, u_id, password,'product.category', 'search_read', [[['name', '=', cat['name']]]])
            categ_id = pro_cat[0]['id'] if pro_cat else False
            
        seller_ids = False
        
        if data['seller_ids']:
            
            seller_ids = []
            
            for id in data['seller_ids']:
                
                # product_id = models.execute_kw(db, u_id, password,'product.product', 'search_read', [[['name', '=', data['name']]]])
                # product_name= product_id[0]['name'] if product_id else False
                sup_info =  sock.execute_kw(dbname, uid, pwd,'product.supplierinfo', 'read', [id])
                
                vendor = models.execute_kw(db, u_id, password,'res.partner', 'search_read', [[['name', '=', sup_info['name'][1]]]])
                
                
                vendor_id = vendor[0]['id'] if vendor else False
                
                if vendor_id:
                
                    val = {
                        'name':vendor_id,
                        'product_name':vendor[0]['name'],
                        'min_qty':sup_info['min_qty'],


                    }
                    seller = (0, 0, val)
                    seller_ids.append(seller)
        
        value = {
                # 'price':data['price'] or False,
                'active':data['active'],
                'qty_available':data['qty_available'] or False,
                'uom_po_id':uom_po_id or False,
                'uom_id':uom_id or False,
                'categ_id':categ_id,
                'image_1920':data['image_medium'],
                'default_code':data['default_code'],
                'name':data['name'],
                'purchase_ok':data['purchase_ok'],
                'sale_ok':data['sale_ok'],
                'can_be_rent':data['can_be_rent'],
                'outsourcing_ok':data['outsourcing_ok'],
                'detailed_type':data['type'],
                'description_purchase':data['description_purchase'],
                'seller_ids': seller_ids if seller_ids else False

            }
        # print(value)
        try:
            pro = models.execute_kw(db, u_id, password,'product.product', 'create', [value])
            print(count)
            exit()
        except BaseException as error:
                print(data)
                writer = csv.writer(file)
                writer.writerow([data['id'],data['name'], error])
                print(data['id'],data['name'])
                
                print('An exception occurred: {}'.format(error))
        

    
# ---------------------------------------products_including_suppliers---------------------------------------
pro_fields = [
    'image_medium','categ_id','default_code','name','sale_ok','purchase_ok','can_be_rent','outsourcing_ok','id',
    'type','uom_id','country_of_origin_id','sug_supplier_last_price','sug_supplier_last_price_currency_id','current_month_use',
    'last_month_use','last_average_use','description','active','procure_method','supply_method','use_underpoint',
    'op_location_id','ddrmp_type','cost_method','standard_price','real_standard_price','last_standard_price',
    'date_standard_price','date_real_standard_price','fixed_by','date_last_standard_price','uom_po_id',
    'seller_ids','description_purchase','qty_available','incoming_qty','outgoing_qty','procurement_qty',
    'loc_type_id','loc_row_id','loc_section_id','property_stock_procurement','property_stock_wip','property_stock_inventory','serial_sequence','unique_production_number','autogenerate',
    'autogenerate_purchase','track_production'
]
with open('archived_product_error.csv', 'w', newline='') as file:
    # rec = [24026,24028,17830,17821,24025,18017,28264,18026,18025,18030,23800,24799,24949,26002,18055,18052,18096,18094,18069,18057,18097,18061,18068,18054,18050,18056,18095,18076,18058,18059,18079,18091,18088,18087,18090,18089,18074,18070,18067,18065,18064,18062,18053,18093,18092,18083,18078,18081,18086,18060,18066,18099,18063,18045,18098,20340,20343,20344,18104,22944,26519,28278,25820,28265,25420,25421,19683,26509,18176,18195,18184,18220,18221,18219,18214,18215,18218,18217,18216,18257,18276,18297,18299,18319,18322,19379,26473,18343,18342,28279,24324,18414,18418,18412,18419,18417,18413,18409,18415,18411,18410,18416,18408,22934,18444,18448,18447,18456,26295,18480,26510,26606,26608,26609,27537,28269,18547,26514,18584,18581,18585,18594,23433,18640,18637,27177,27181,27176,27180,27271,27204,27170,27179,27500,27175,27174,28215,26724,28170,24958,25080,28180,28164,28168,28125,28126,28162,28178,25826,28194,28195,28183,28182,24818,27583,27584,27585,27582,27581,27580,27574,27575,27576,27577,27578,27579,27489,27438,27420,27462,27473,27483,27424,27467,27387,28192,27449,27493,27486,27427,27470,27459,27496,27476,27423,27466,27455,27494,27410,28172,28174,28176,28177,18812,18813,18815,18825,18828,18840,18829,18838,18857,26611,27625,27626,27627,27628,18884,27440,27393,27388,27433,27436,27630,27395,27629,27631,27632,27633,27634,18937,28283,27471,27480,27481,27447,27441,27474,27482,27450,27484,27567,27490,27570,27477,27446,27487,27454,27464,27659,27460,27469,27569,27571,27572,27573,18954,27511,18964,18973,18974,23399,23400,18999,24012,28294,19015,24121,26953,26890,26891,26892,26894,26931,27723,27654,27652,27656,27650,27648,27507,27518,27504,27519,27515,27516,27517,26548,28271,27215,27216,27218,27219,27208,27211,27220,27360,27316,27224,27217,27209,27210,27859,27862,27884,19054,19061,19060,27497,27498,27848,27861,28275,19069,19076,19083,19086,23768,19098,19108,19109,19396,23484,23485,19127,19115,19133,19131,19134,19128,19135,19126,19130,19124,27526,27527,27524,27525,27532,27533,27534,27535,27520,27521,27522,27523,27530,27531,27528,27529,27365,27330,27276,27364,27377,27378,27346,27376,27362,27370,27371,27343,27379,27380,27381,27288,27375,27368,27369,27321,27367,19136,19138,19137,19139,19145,19144,19163,19155,27658,27509,27510,27505,27502,27508,27501,28284,27233,27197,27275,27234,27198,27192,27195,27230,27186,27190,27182,27199,27235,27317,27200,27272,27188,27201,27237,27203,27405,27071,28357,19255,19257,23803,27661,27667,28169,27683,28133,19269,24589,27685,28202,28191,28193,28181,28179,28175,28184,28161,27681,27682,28171,28173,19331,19330,19341,23316,27269,24714,19369,19466,27303,26580,27358,28311,27206]
    
    pro = sock.execute_kw(dbname, uid, pwd, 'product.product', 'search',[[['active','=',False]]])
    active_false_products = sock.execute_kw(dbname, uid, pwd,'product.product', 'read', [pro],{'fields': pro_fields})
   
    create_product(active_false_products)
    
    
    