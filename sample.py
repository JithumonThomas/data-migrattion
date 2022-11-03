    # records = sock.execute_kw(dbname, uid, pwd,'res.partner', 'read', [customer_record],{'fields':fields})
    # print(records)
       
    # else:
    #     val = ['partner_id','title','function']
    #     te =  sock.execute_kw(dbname, uid, pwd,'res.partner', 'read', [customer_record],{'fields':['partner_id']})
        
    #     fields.extend(val)
    #     print(fields)
    #     records = sock.execute_kw(dbname, uid, pwd,'res.partner', 'read', [customer_record],{'fields':fields})
    #     print("------------>",records)
    #     exit()
    
   
# suppliers_records = sock.execute_kw(dbname, uid, pwd, 'res.partner', 'search',[[['customer','=',False]]])
# print(customer_records)
# print(len(suppliers_records))
# customers_records = sock.execute_kw(dbname, uid, pwd, 'res.partner', '',[[['customer','=',True]]])
# print(customers_records)

# suppliers_records = sock.execute_kw(dbname, uid, pwd, 'mrp.bom', 'search_read', [[]],{'fields':['donation','salutation']})

# products_including_suppliers = sock.execute_kw(dbname, uid, pwd, 'mrp.bom', 'search_read', [[]],{'fields':['donation','salutation']})
# # print(len(migration_import_records))
# for givingsg_import_record in givingsg_import_records:
#     if givingsg_import_record['donation'] and givingsg_import_record['salutation']:
       
#         donation_record = sock.execute_kw(dbname, uid, pwd, 'donation', 'search_read', [[['id','=',givingsg_import_record['donation'][0]],['partner_id','!=',False]]],
#                                                   {'fields': ['partner_id']})
#         partner_id = donation_record[0]['partner_id'][0]
       
#         if givingsg_import_record['salutation']:
           
#             salutation_record =  sock.execute_kw(dbname, uid, pwd, 'salutation', 'search_read', [[['name','=',givingsg_import_record['salutation']]]],
#             {'fields': ['title']}) 
#             if salutation_record:
                
#                 if salutation_record[0]['title']:
#                     salutation = salutation_record[0]['title'][0]
                    
#                     print("------",salutation) 
#                     sock.execute_kw(dbname, uid, pwd,  'res.partner', 'write',
#                                 [[partner_id], {'title':salutation}])
    




# if cate['parent_id']:
#             cate_parent_name = models.execute_kw(db, u_id, password,'res.partner.category', 'search_read', [[['name', '=', cate['parent_id'][1]]]])
#             val = {
#                 'name':cate['name'],
#                 'active':cate['active']
#             }
#             print(val)
#             exit()
#             cate_parent_id =  models.execute_kw(db, u_id, password,'res.partner.category', 'create', [val])
#             print(cate_parent_id)
#         else:
                
#             read_cat_parent = sock.execute_kw(dbname, uid, pwd,'res.partner.category', 'read', [category_old])[0]
#             cate_parent_id = models.execute_kw(db, u_id, password,'res.partner.category', 'search_read', [[['name', '=', data['country_id'][1]]]])
#             category_ = sock.execute_kw(dbname, uid, pwd,'res.partner.category', 'search', [[['id', '=', data['category_id']]]])
#             val = {
#                 'name':cate['name'],
#                 'active':cate['active']
#             }
#             partner_category = models.execute_kw(db, u_id, password,'res.partner.category', 'create', [val])
#             print("->partner_category",partner_category)
#         exit()









[{'ean13': False, 'property_account_position': [2, 'Tax Exempt'], 'signup_valid': False, 'ref_companies': [], 'sale_order_count': 0, 'commission_rules_ids': [], 'purchase_order_count': 0, 'workitem_ids': [], 'contact_address': 'ITM Instruments Inc\n20800 Boul Industriel\n\nSte-Anne-De-Bellevue  H9X 0A1\nCanada', 'property_stock_customer': [9, 'Partner Locations / Customers'], 'property_product_pricelist': [1, 'Public (CAD)'], 'signup_url': False, 'message_summary': ' ', 'move_ids': [], 'stock_customer_rentals': False, 'display_name': 'ITM Instruments Inc, IP-V6 (3768)', 'opt_out': False, 'title': False, 'phone_ext': False, 'company_id': [1, 'Adamson Systems Engineering'], 'parent_id': [7798, 'ITM Instruments Inc'], 'last_reconciliation_date': False, 'home_phone': False, 'employee': False, 'latest_followup_level_id': False, 'department_id': False, 'fax': False, 'service_ids': [], 'partner_receivable_ids': [], 'child_ids': [], 'user_ids': [], 'facebook': False, 'unreconciled_aml_ids': [], 'sales_representative_id': False, 'image_medium': False, 'name': 'IP-V6 (3768)', 'debit_limit': 0.0, 'warning_id': False, 'property_account_receivable': [671, '11010-00-00 AR-CDN'], 'payment_earliest_due_date': False, 'partner_invoice_ids': [], 'payment_amount_overdue': 0.0, 'property_stock_outsourcing': False, 'pst_number': False, 'msds_required': False, 'commercial_partner_id': [7798, 'ITM Instruments Inc'], 'message_follower_ids': [34, 38, 3], 'twitter': False, 'phone': False, 'sex': False, 'street': '20800 Boul Industriel', 'signup_token': False, 'highrise_id': 0, 'task_ids': [], 'is_contract': False, 'bank_ids': [], 'attachment_ids': [], 'industry_id': False, 'country_id': [39, 'Canada'], 'tz_offset': '+0000', 'notification_email_send': 'comment', 'debit': 0, 'supplier': False, 'ref': False, 'email': False, 'territory_id': False, 'contract_ids': [], 'picking_warn': 'no-message', 'website': False, 'latest_followup_date': False, 'supp_name': False, 'phone2': False, 'street2': False, 'street3': False, 'opportunity_ids': [], 'payment_amount_due': 0.0, 'active': True, 'tz': False, 'signup_expiration': False, 'certs_required': False, 'territories_ids': [], 'message_is_follower': True, 'property_product_pricelist_purchase': [2, 'Default Purchase Pricelist (CAD)'], 'property_account_payable': [808, '20010-00-00 AP-CDN'], 'country': [39, 'Canada'], 'credit': 0, 'carrier': False, 'payment_next_action': False, 'message_unread': False, 'payment_note': False, 'comment': False, 'sale_warn': 'no-message', 'purchase_warn': 'no-message', 'color': 0, 'image': False, 'invoice_ids': [], 'commission_frequency_type': False, 'vat_number': False, 'property_invoice_type': False, 'city': 'Ste-Anne-De-Bellevue', 'phonecall_ids': [], 'opportunity_count': 0, 'user_id': [1, 'Administrator'], 'zip': 'H9X 0A1', 'event_registration_ids': [], 'event_ids': [], 'type': 'default', 'vat': False, 'function': False, 'picking_warn_msg': False, 'door': False, 'latest_followup_level_id_without_lit': False, 'claims_ids': [], 'commission_frequency': 0, 'gst_number': False, 'payment_responsible_id': False, 'customer': True, 'rent_pricelist': False, 'client_since': 2017, 'activity_ids': [], 'insurance_amount': 0.0, 'sale_order_ids': [], 'image_small': False, 'property_delivery_carrier': False, 'birthdate': False, 'purchase_order_ids': [], 'has_image': False, 'state_id': False, 'invoice_warn_msg': False, 'receiving_person_id': False, 'payment_next_action_date': False, 'pin': False, 'linkedin': False, 'use_parent_address': False, 'skype': False, 'signup_type': False, 'id': 7801, 'meeting_ids': [], 'partner_payable_ids': [], 'invoice_warn': 'no-message', 'message_ids': [932404], 'note': False, 'tin': False, 'speaker': False, 'property_stock_supplier': [8, 'Partner Locations / Customers / Suppliers'], 'sale_ids': [], 'create_uid': [1, 'Administrator'], 'is_company': False, 'packing_ids': [], 'vat_subjected': False, 'section_id': False, 'property_payment_term': [1, 'Immediate Payment'], 'property_supplier_payment_term': False, 'date': False, 'mobile_ext': False, 'lead_ids': [], 'category_id': [], 'lang': 'en_US', 'credit_limit': 0.0, 'meeting_count': 0, 'purchase_warn_msg': False, 'mobile': False, 'ship_method_ids': [], 'commission_product_id': False, 'fax_ext': False, 'source_id': False, 'sale_warn_msg': False, 'phone2_ext': False}]




{'comment': False, 'receiving_person_id': False, 'purchase_warn': 'no-message', 'sale_warn': 'no-message', 'invoice_warn': 'no-message', 'image': False, 'active': True, 'street': '15 Richard Daley Dr', 'property_stock_customer': [9, 'Partner Locations / Customers'], 'vat_number': False, 'property_product_pricelist': [1, 'Public (CAD)'], 'id': 2492, 'city': 'Stouffville', 'stock_customer_rentals': False, 'user_id': [1, 'Administrator'], 'opt_out': False, 'zip': 'L4A 0S9', 'title': False, 'function': False, 'country_id': [39, 'Canada'], 'property_account_payable': [808, '20010-00-00 AP-CDN'], 'parent_id': False, 'notification_email_send': 'comment', 'picking_warn': 'no-message', 'supplier': True, 'type': 'default', 'email': False, 'is_company': True, 'website': False, 'customer': False, 'fax': False, 'bank_ids': [], 'supp_name': '1606', 'phone2': False, 'street2': False, 'child_ids': [3239], 'section_id': False, 'phone': False, 'date': False, 'unreconciled_aml_ids': [], 'payment_responsible_id': False, 'lang': 'en_US', 'rent_pricelist': False, 'property_stock_supplier': [8, 'Partner Locations / Customers / Suppliers'], 'name': 'Aumtronics Inc', 'property_product_pricelist_purchase': [2, 'Default Purchase Pricelist (CAD)'], 'insurance_amount': 0.0, 'mobile': False, 'ref': False, 'ship_method_ids': [], 'property_account_receivable': [671, '11010-00-00 AR-CDN'], 'carrier': False, 'payment_next_action': False, 'property_stock_outsourcing': False, 'state_id': [52, 'Ontario'], 'category_id': []}
{'image_1920': False, 'child_ids': False, 'user_id': 2, 'is_company': True, 'customer_rank': 0, 'supplier_rank': 1, 'name': 'Aumtronics Inc', 'type': False, 'street': '15 Richard Daley Dr', 'street2': False, 'city': 'Stouffville', 'zip': 'L4A 0S9', 'state_id': 541, 'country_id': 38, 'vat': False, 'category_id': False, 'phone': False, 'mobile': False, 'email': False, 'website': False, 'lang': 'en_US', 'ref': False, 'sale_warn': 'no-message', 'purchase_warn': 'no-message', 'picking_warn': 'no-message', 'invoice_warn': 'no-message', 'comment': False, 'function': False, 'title': False, 'parent_id': False}

{'image_1920': False, 'child_ids': [(0, 0, [4636])], 'user_id': False, 'is_company': True, 'customer_rank': 0, 'supplier_rank': 1, 'name': 'Automated CAD Solutions', 'type': False, 'street': '242 Fleetwood Rd', 'street2': False, 'city': 'Janetville', 'zip': 'L0B 1K0', 'state_id': 541, 'country_id': False, 'vat': False, 'category_id': False, 'phone': '905-809-3279', 'mobile': False, 'email': False, 'website': False, 'lang': 'en_US', 'ref': False, 'sale_warn': 'no-message', 'purchase_warn': 'no-message', 'picking_warn': 'no-message', 'invoice_warn': 'no-message', 'comment': False, 'function': False, 'title': False, 'parent_id': False}