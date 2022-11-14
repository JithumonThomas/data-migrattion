
from  xmlrpc import client
import xmlrpc.client
import csv


url = 'http://3.109.84.120:5079'
db = 'Adamson15-Base-test-migrate'
user = 'admin'
password = '@Ad@m$0n*#135'
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
u_id = common.authenticate(db, user, password, {})
version = common.version()
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

test = models.execute_kw(db, u_id, password,'product.product', 'search_read', [[['id', '=',825]]])
print(test)