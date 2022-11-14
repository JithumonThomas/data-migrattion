
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

parent_records = sock.execute_kw(dbname, uid, pwd, 'res.partner', 'search',[[['id','in',[8441,8514,2348,3688,3766,3761,3700,3603,3534,3759,7807]],['customer','=',True]]])
print(len(parent_records))
# def create_vendor_product(data):
  
#     for da in data:
       
#         value = {
#             'sale_ok':da['sale_ok'],
#         }
#         print()
        
#         product = models.execute_kw(db, u_id, password,'product.product', 'search', [[['default_code','=',da['default_code']]]])
#         # print(product)
#         # exit()
#         product_id = product[0]
        
#         try:
#             id = models.execute_kw(db, u_id, password,'product.product','write', [[product_id],value])
#             print(id)
#         except BaseException as error:
#                 writer = csv.writer(file)
#                 writer.writerow([da['id'],da['name'], error])
            
#                 print(da['id'],da['name'])
        

    
# # ---------------------------------------products_including_suppliers sale write---------------------------------------
# pro_fields = [
#    'default_code','name','sale_ok','purchase_ok','can_be_rent''id',
# ]
# with open('product_error.csv', 'w', newline='') as file:
#     can_be_sold = sock.execute_kw(dbname, uid, pwd, 'product.product', 'read', [products_sale_ok],
#                                {'fields': pro_fields})
   
#     create_vendor_product(can_be_sold)
    
    