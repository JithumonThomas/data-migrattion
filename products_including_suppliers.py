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

products_including_suppliers = sock.execute_kw(dbname, uid, pwd, 'product.product', 'search',[[]])

def create_vendor_product(data):
    pro_cate = False
    if data['categ_id']:
        print(data['categ_id'])
        
    seller_ids = False
    if data['seller_ids']:
        seller_ids = []
        for id in data['seller_ids']:
            
            vendor_old = sock.execute_kw(dbname, uid, pwd,'res.partner', 'search', [[['id', '=', id]]])
            
            vendor_old_id = sock.execute_kw(dbname, uid, pwd,'res.partner', 'read', [vendor_old])
           
            if vendor_old_id:
                product_vendor = models.execute_kw(db, u_id, password,'res.partner', 'search_read', [[['name', '=', vendor_old_id[0]['name']]]])
                
                vendor_ids = product_vendor[0]['id'] if product_vendor else False
                if vendor_ids:
                   
                    seller_ids.append(vendor_ids)
                   
    value = {
        'image_1920':data['image_medium'],
        'default_code':data['default_code'],
        'name':data['name'],
        'purchase_ok':data['purchase_ok'],
        'can_be_rent':data['can_be_rent'],
        'outsourcing_ok':data['outsourcing_ok'],
        'detailed_type':data['type'],
        'description_purchase':data['description_purchase'],
        'seller_ids':seller_ids if seller_ids else False

    }
    print(value)
    
        

    
# ---------------------------------------products_including_suppliers---------------------------------------
pro_fields = [
    'image_medium','categ_id','default_code','name','sale_ok','purchase_ok','can_be_rent','outsourcing_ok',
    'type','uom_id','country_of_origin_id','sug_supplier_last_price','sug_supplier_last_price_currency_id','current_month_use',
    'last_month_use','last_average_use','description','active','procure_method','supply_method','use_underpoint',
    'op_location_id','ddrmp_type','cost_method','standard_price','real_standard_price','last_standard_price',
    'date_standard_price','date_real_standard_price','fixed_by','date_last_standard_price','uom_po_id',
    'seller_ids','description_purchase','qty_available','incoming_qty','outgoing_qty','procurement_qty',
    'loc_type_id','loc_row_id','loc_section_id','property_stock_procurement','property_stock_wip','property_stock_inventory','serial_sequence','unique_production_number','autogenerate',
    'autogenerate_purchase','track_production'
]

for products_suppliers in products_including_suppliers:
    products = sock.execute_kw(dbname, uid, pwd,'product.product', 'read', [products_suppliers],{'fields': pro_fields})
    create_vendor_product(products)
    
        