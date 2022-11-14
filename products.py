from  xmlrpc import client
import xmlrpc.client
import csv
username = 'admin'
pwd = '@Adamson#ERP'
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

def create_vendor_product(data):
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
        
 
    
    if not data['seller_ids']:
        
       
        value = {
            # 'price':data['price'] or False,
            'qty_available':data['qty_available'] or False,
            'uom_po_id':uom_po_id or False,
            'uom_id':uom_id or False,
            'categ_id':categ_id,
            'image_1920':data['image_medium'],
            'default_code':data['default_code'],
            'name':data['name'],
            'purchase_ok':data['purchase_ok'],
            'can_be_rent':data['can_be_rent'],
            'outsourcing_ok':data['outsourcing_ok'],
            'detailed_type':data['type'],
            'description_purchase':data['description_purchase']
            

        }
       
        try:
            pro = models.execute_kw(db, u_id, password,'product.product', 'create', [value])
            print(pro)
        except BaseException as error:
                print(data)
                writer = csv.writer(file)
                writer.writerow([data['id'],data['name'], error])
                print(data['id'],data['name'])
                
                print('An exception occurred: {}'.format(error))
    exit()
        

    
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
    for pro in products:
        products = sock.execute_kw(dbname, uid, pwd,'product.product', 'read', [pro],{'fields': pro_fields})
        create_vendor_product(products)
    
    