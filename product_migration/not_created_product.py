from  xmlrpc import client
import xmlrpc.client
import csv
pwd = '@Ad@m$0n*#135'
username = 'admin'
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

products = sock.execute_kw(dbname, uid, pwd, 'product.product', 'search',[[['seller_ids','=',False]]])

def create_vendor_product(da):
   for data in da:
        print(data['default_code'])
        pro_active = models.execute_kw(db, u_id, password,'product.product', 'search', [[['default_code','=',data['default_code']]]])
        pro_inactive = models.execute_kw(db, u_id, password,'product.product', 'search', [[['active','=',False],['default_code','=',data['default_code']]]])
        if pro_active or pro_inactive:
            print(pro_active or pro_inactive)
       
    # if data['product_id']:
    #     print(data['product_id'])
    #     exit()
    #     uom_po = models.execute_kw(db, u_id, password,'uom.uom', 'search_read', [[['name','=',data['uom_po_id'][1]]]])
    #     uom_po_id = uom_po[0]['id']

    

    
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
with open('all_product_error.csv', 'w', newline='') as file:
    rec = [28264,18026,18025,18055,18052,18096,18094,18069,18057,18097,18061,18068,18054,18050,18056,18095,18076,18058,18059,18079,18091,18088,18087,18090,18089,18074,18070,18067,18065,18064,18062,18053,18093,18092,18083,18078,18081,18086,18060,18066,18099,18063,18045,18098,20340,20343,20344,18104,22944,26519,28278,28265,19683,26509,18176,18195,18184,18220,18221,18219,18214,18215,18218,18217,18216,18297,18319,18322,26473,18343,18342,28279,18414,18418,18412,18419,18417,18413,18409,18415,18411,18410,18416,18408,22934,26295,26510,27537]
    
    products = sock.execute_kw(dbname, uid, pwd,'product.product', 'read', [rec],{'fields': pro_fields})
    create_vendor_product(products)
    
    