from  xmlrpc import client
import xmlrpc.client
import csv
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
parent_records = sock.execute_kw(dbname, uid, pwd, 'res.partner', 'search',[[['id','in',[8441,8514,2348,3688,3766,3761,3700,3603,3534,3759,7807]],['customer','=',True]]])

print(len(parent_records))



    
