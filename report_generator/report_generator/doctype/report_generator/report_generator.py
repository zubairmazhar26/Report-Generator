# Copyright (c) 2022, zubairmazhar23@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ReportGenerator(Document):
	def validate(self):
		self.total_rate = 0
		self.total_qty = 0
		self.grand_total = 0
		for d in self.report_record_details:
			self.total_rate += int(d.price_list_rate)
			self.total_qty += int(d.qty)
			self.grand_total += int(d.qty) * int(d.rate)
	@frappe.whitelist(allow_guest=True)
	def getserialrecord(self):
		self.report_record_details = ""
		value = {}
		conditions = ""
		if (self.item_code and self.ser_status and self.serial_no and self.creation_document_no and self.s_from_date and self.s_to_date and self.ser_supplier and self.sales_document_type and self.ser_sales_document_no):
			conditions +=f"""where item_code='{self.item_code}' and status='{self.ser_status}' and serial_no='{self.serial_no}' and creation_document_no='{self.creation_document_no}' and supplier='{self.ser_supplier}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_type='{self.sales_document_type}' and delivery_document_no='{self.ser_sales_document_no}' """
		elif (self.item_code and self.ser_status and self.s_from_date and self.s_to_date and self.ser_supplier and self.sales_document_type and self.ser_sales_document_no):
			conditions +=f"""where item_code='{self.item_code}' and status='{self.ser_status}' and supplier='{self.ser_supplier}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_type='{self.sales_document_type}' and delivery_document_no='{self.ser_sales_document_no}' """
		elif (self.item_code and self.ser_status and self.s_from_date and self.s_to_date and self.ser_supplier and self.sales_document_type):
			conditions +=f"""where item_code='{self.item_code}' and status='{self.ser_status}' and supplier='{self.ser_supplier}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_type='{self.sales_document_type}' """
		elif (self.item_code and self.ser_status and self.s_from_date and self.s_to_date and self.ser_supplier and self.ser_sales_document_no):
			conditions +=f"""where item_code='{self.item_code}' and status='{self.ser_status}' and supplier='{self.ser_supplier}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_no='{self.ser_sales_document_no}' """
		# a
		elif (self.item_code and self.ser_status and self.s_from_date and self.s_to_date and self.sales_document_type and self.ser_sales_document_no):
			conditions +=f"""where item_code='{self.item_code}' and status='{self.ser_status}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_type='{self.sales_document_type}' and delivery_document_no='{self.ser_sales_document_no}' """
		elif (self.item_code and self.ser_status and self.s_from_date and self.s_to_date and self.sales_document_type ):
			conditions +=f"""where item_code='{self.item_code}' and status='{self.ser_status}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_type='{self.sales_document_type}'"""
		elif (self.item_code and self.ser_status and self.s_from_date and self.s_to_date and self.ser_sales_document_no):
			conditions +=f"""where item_code='{self.item_code}' and status='{self.ser_status}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_no='{self.ser_sales_document_no}' """
		# a
		elif (self.item_code and self.ser_status and self.serial_no and self.creation_document_no and self.s_from_date and self.s_to_date and self.ser_supplier and self.sales_document_type):
			conditions +=f"""where item_code='{self.item_code}' and status='{self.ser_status}' and serial_no='{self.serial_no}' and creation_document_no='{self.creation_document_no}' and supplier='{self.ser_supplier}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_type='{self.sales_document_type}'"""
		elif (self.item_code and self.ser_status and self.serial_no and self.creation_document_no and self.s_from_date and self.s_to_date and self.ser_supplier and self.ser_sales_document_no):
			conditions +=f"""where item_code='{self.item_code}' and status='{self.ser_status}' and serial_no='{self.serial_no}' and creation_document_no='{self.creation_document_no}' and supplier='{self.ser_supplier}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_no='{self.ser_sales_document_no}' """
		elif (self.item_code and self.ser_status and self.serial_no and self.creation_document_no and self.s_from_date and self.s_to_date and self.ser_supplier):
			conditions +=f"""where item_code='{self.item_code}' and status='{self.ser_status}' and serial_no='{self.serial_no}' and creation_document_no='{self.creation_document_no}' and supplier='{self.ser_supplier}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}'"""
		# a
		elif (self.item_code and self.ser_status and self.serial_no and self.ser_supplier):
			conditions +=f"""where item_code='{self.item_code}' and status='{self.ser_status}' and serial_no='{self.serial_no}' and supplier='{self.ser_supplier}' """
		elif (self.item_code and self.ser_status and self.serial_no and self.ser_supplier):
			conditions +=f"""where item_code='{self.item_code}' and status='{self.ser_status}' and supplier='{self.ser_supplier}' and serial_no='{self.serial_no}' """
		# a
		elif (self.item_code and self.ser_status and self.creation_document_no and self.ser_supplier):
			conditions +=f"""where item_code='{self.item_code}' and status='{self.ser_status}' and creation_document_no='{self.creation_document_no}' and supplier='{self.ser_supplier}'"""
		elif (self.item_code and self.ser_status and self.creation_document_no):
			conditions +=f"""where item_code='{self.item_code}' and status='{self.ser_status}' and creation_document_no='{self.creation_document_no}'"""
		elif (self.item_code and self.ser_status and self.ser_supplier):
			conditions +=f"""where item_code='{self.item_code}' and status='{self.ser_status}' and supplier='{self.ser_supplier}'"""
		elif (self.item_code and self.ser_status):
			conditions +=f"""where item_code='{self.item_code}' and status='{self.ser_status}'"""
		# a
		elif (self.ser_status and self.serial_no and self.s_from_date and self.s_to_date and self.sales_document_type and self.ser_sales_document_no):
			conditions +=f"""where status='{self.ser_status}' and serial_no='{self.serial_no}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_type='{self.sales_document_type}' and delivery_document_no='{self.ser_sales_document_no}' """
		elif (self.ser_status and self.serial_no and self.s_from_date and self.s_to_date and self.sales_document_type):
			conditions +=f"""where status='{self.ser_status}' and serial_no='{self.serial_no}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_type='{self.sales_document_type}' """
		elif (self.ser_status and self.serial_no and self.s_from_date and self.s_to_date and self.ser_sales_document_no):
			conditions +=f"""where status='{self.ser_status}' and serial_no='{self.serial_no}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_no='{self.ser_sales_document_no}' """
		elif (self.ser_status and self.serial_no and self.s_from_date and self.s_to_date and self.ser_supplier and self.sales_document_type):
			conditions +=f"""where status='{self.ser_status}' and serial_no='{self.serial_no}' and supplier='{self.ser_supplier}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_type='{self.sales_document_type}'"""
		elif (self.ser_status and self.serial_no and self.s_from_date and self.s_to_date and self.ser_supplier and self.ser_sales_document_no):
			conditions +=f"""where status='{self.ser_status}' and serial_no='{self.serial_no}' and supplier='{self.ser_supplier}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_no='{self.ser_sales_document_no}' """
		elif (self.ser_status and self.serial_no and self.s_from_date and self.s_to_date and self.sales_document_type and self.ser_sales_document_no):
			conditions +=f"""where status='{self.ser_status}' and serial_no='{self.serial_no}'  and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_type='{self.sales_document_type}'"""
		elif (self.ser_status and self.serial_no and self.s_from_date and self.s_to_date and self.ser_supplier and self.ser_sales_document_no):
			conditions +=f"""where status='{self.ser_status}' and serial_no='{self.serial_no}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_no='{self.ser_sales_document_no}' """
		elif (self.ser_status and self.s_from_date and self.s_to_date and self.ser_supplier and self.sales_document_type and self.ser_sales_document_no):
			conditions +=f"""where status='{self.ser_status}' and supplier='{self.ser_supplier}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_type='{self.sales_document_type}' and delivery_document_no='{self.ser_sales_document_no}'"""
		elif (self.ser_status and self.s_from_date and self.s_to_date and self.ser_supplier and self.sales_document_type):
			conditions +=f"""where status='{self.ser_status}' and supplier='{self.ser_supplier}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_type='{self.sales_document_type}'"""
		elif (self.ser_status and self.s_from_date and self.s_to_date and self.ser_supplier and self.ser_sales_document_no):
			conditions +=f"""where status='{self.ser_status}' and supplier='{self.ser_supplier}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_no='{self.ser_sales_document_no}'"""
		elif (self.ser_status and self.s_from_date and self.s_to_date and self.sales_document_type and self.ser_sales_document_no):
			conditions +=f"""where status='{self.ser_status}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_type='{self.sales_document_type}' and delivery_document_no='{self.ser_sales_document_no}'"""
		elif (self.ser_status and self.s_from_date and self.s_to_date and self.sales_document_type):
			conditions +=f"""where status='{self.ser_status}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_type='{self.sales_document_type}'"""
		elif (self.ser_status and self.s_from_date and self.s_to_date and self.sales_document_no):
			conditions +=f"""where status='{self.ser_status}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_no='{self.ser_sales_document_no}'"""
		elif (self.s_from_date and self.s_to_date and self.sales_document_type and self.ser_sales_document_no):
			conditions +=f"""where delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_type='{self.sales_document_type}' and delivery_document_no='{self.ser_sales_document_no}'"""
		elif (self.s_from_date and self.s_to_date and self.sales_document_type ):
			conditions +=f"""where delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_type='{self.sales_document_type}'"""
		elif (self.s_from_date and self.s_to_date and self.sales_document_no):
			conditions +=f"""where delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_no='{self.ser_sales_document_no}'"""
		elif (self.ser_status and self.creation_document_no):
			conditions +=f"""where status='{self.ser_status}' and creation_document_no='{self.creation_document_no}'"""
		elif (self.ser_status and self.s_from_date and self.s_to_date and self.sales_document_type and self.ser_sales_document_no):
			conditions +=f"""where status='{self.ser_status}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_type='{self.sales_document_type}' and delivery_document_no='{self.ser_sales_document_no}' """
		elif (self.s_from_date and self.s_to_date and self.sales_document_type and self.ser_sales_document_no):
			conditions +=f"""where delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and delivery_document_type='{self.sales_document_type}' and delivery_document_no='{self.ser_sales_document_no}'"""
		elif (self.ser_status and self.ser_supplier and self.sales_document_type and self.ser_sales_document_no):
			conditions +=f"""where status='{self.ser_status}' and supplier='{self.ser_supplier}' and delivery_document_type='{self.sales_document_type}' and delivery_document_no='{self.ser_sales_document_no}'"""
		elif (self.ser_status and self.ser_supplier):
			conditions +=f"""where status='{self.ser_status}' and supplier='{self.ser_supplier}'"""
		elif (self.ser_status and self.sales_document_type and self.ser_sales_document_no):
			conditions +=f"""where status='{self.ser_status}' and delivery_document_type='{self.sales_document_type}' and delivery_document_no='{self.ser_sales_document_no}' """
		elif (self.ser_status and self.sales_document_type):
			conditions +=f"""where status='{self.ser_status}' and delivery_document_type='{self.sales_document_type}' """
		elif (self.ser_status and self.ser_sales_document_no):
			conditions +=f"""where status='{self.ser_status}' and delivery_document_no='{self.ser_sales_document_no}' """
		elif (self.ser_status and self.s_from_date and self.s_to_date and self.item_group):
			conditions +=f"""where status='{self.ser_status}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and item_group='{self.item_group}' """
		elif (self.ser_status and self.s_from_date and self.s_to_date):
			conditions +=f"""where status='{self.ser_status}' and delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' """
		elif (self.s_from_date and self.s_to_date and self.item_group):
			conditions +=f"""where delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' and item_group='{self.item_group}' """
		elif (self.s_from_date and self.s_to_date):
			conditions +=f"""where delivery_date>='{self.s_from_date}' and delivery_date<='{self.s_to_date}' """
		elif (self.ser_status and self.item_group):
			conditions +=f"""where status='{self.ser_status}' and item_group='{self.item_group}' """
		elif (self.ser_status):
			conditions +=f"""where status='{self.ser_status}' """
		elif (self.item_code):
			conditions +=f"""where item_code='{self.item_code}'"""
		elif (self.creation_document_no):
			conditions +=f"""where creation_document_no='{self.creation_document_no}'"""
		elif (self.ser_supplier):
			conditions +=f"""where supplier='{self.ser_supplier}' """
		elif (self.serial_no):
			conditions +=f"""where serial_no='{self.serial_no}' """
		elif (self.sales_document_type and self.ser_sales_document_no):
			conditions +=f"""where delivery_document_type='{self.sales_document_type}' and delivery_document_no='{self.ser_sales_document_no}' """
		elif (self.sales_document_type):
			conditions +=f"""where delivery_document_type='{self.sales_document_type}' """
		elif (self.ser_sales_document_no):
			conditions +=f"""where delivery_document_no='{self.ser_sales_document_no}' """
		else:
			doc = frappe.db.sql(""" select item_code,item_name,warehouse,batch_no,status,name,company,precious_stone,stone_size,material_use,material_use_abbv,weight,\
			diamond_size,cz,standard_rate,image,serial_ctr,supplier,purchase_rate,delivery_date,delivery_document_type,delivery_document_no,item_group from `tabSerial No` """)
			value = doc
		doc = frappe.db.sql(""" select item_code,item_name,warehouse,batch_no,status,name,company,precious_stone,stone_size,material_use,material_use_abbv,weight,\
		diamond_size,cz,standard_rate,image,serial_ctr,supplier,purchase_rate,delivery_date,delivery_document_type,delivery_document_no,item_group from `tabSerial No` %s"""%conditions)
		value = doc
		self.total_rate = 0
		self.total_qty = 0
		self.grand_total = 0
		for a in value:
			row = self.append("report_record_details", {})
			row.item_code = a[0]
			row.item_name = a[1]
			row.warehouse = a[2]
			row.batch_no = a[3]
			row.status = a[4]
			row.serial_no = a[5]
			row.company = a[6]
			row.precious_stone =a[7]
			row.material_use_abbv = a[10]
			row.stone_size = a[8]
			row.cz = a[13]
			row.diamond_size = a[12]
			row.weight = a[11]
			row.upload_image = a[15]
			row.qty = a[16]
			row.supplier = a[17]
			row.rate = a[14]
			row.sales_date = a[19]
			row.price_list_rate = a[18]
			row.sales_document_type = a[20]
			row.sales_document_no = a[21]
			row.item_group = a[22]
			self.total_rate += a[18]
			self.total_qty += a[16]
			self.grand_total += a[16] * a[14]
	@frappe.whitelist(allow_guest=True)
	def getpinvoice(self):
		self.report_record_details = ""
		value = {}
		conditions = ""
		if (self.item_code and self.te and self.serial_no and self.supplier and self.sales_document_no and self.p_from_date and self.p_to_date and self.supplier_dell_note):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{self.te}' and si.serial_no='{self.serial_no}' and i.supplier='{self.supplier}' and i.name='{self.sales_document_no}' and i.posting_date>='{self.p_from_date}' and i.posting_date<='{self.p_to_date}' and i.bill_no='{self.supplier_dell_note}' """
		elif (self.item_code and self.te and self.serial_no and self.supplier and self.sales_document_no and self.p_from_date and self.p_to_date):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{self.te}' and si.serial_no='{self.serial_no}' and i.supplier='{self.supplier}' and i.name='{self.sales_document_no}' and i.posting_date>='{self.p_from_date}' and i.posting_date<='{self.p_to_date}' """
		elif (self.item_code and self.te and self.serial_no and self.supplier and self.p_from_date and self.p_to_date and self.supplier_dell_note):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{self.te}' and si.serial_no='{self.serial_no}' and i.supplier='{self.supplier}' and i.posting_date>='{self.p_from_date}' and i.posting_date<='{self.p_to_date}' and i.bill_no='{self.supplier_dell_note}'"""
		elif (self.item_code and self.te and self.serial_no and self.supplier and self.p_from_date and self.p_to_date):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{self.te}' and si.serial_no='{self.serial_no}' and i.supplier='{self.supplier}' and i.posting_date>='{self.p_from_date}' and i.posting_date<='{self.p_to_date}'"""
		elif (self.item_code and self.te and self.serial_no and self.sales_document_no and self.supplier_dell_note):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{self.te}' and si.serial_no='{self.serial_no}' and i.name='{self.sales_document_no}' and i.bill_no='{self.supplier_dell_note}'"""
		elif (self.item_code and self.te and self.serial_no and self.sales_document_no):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{self.te}' and si.serial_no='{self.serial_no}' and i.name='{self.sales_document_no}'"""
		elif (self.item_code and self.te and self.supplier and self.sales_document_no and self.supplier_dell_note):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{self.te}' and i.supplier='{self.supplier}' and i.name='{self.sales_document_no}' and i.bill_no='{self.supplier_dell_note}'"""
		elif (self.item_code and self.te and self.supplier and self.sales_document_no):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{self.te}' and i.supplier='{self.supplier}' and i.name='{self.sales_document_no}'"""
		elif (self.item_code and self.te and self.serial_no and self.supplier_dell_note):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{self.te}' and si.serial_no='{self.serial_no}' and i.bill_no='{self.supplier_dell_note}' """
		elif (self.item_code and self.te and self.serial_no):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{self.te}' and si.serial_no='{self.serial_no}' """
		elif (self.item_code and self.te and self.p_from_date and self.p_to_date and self.supplier_dell_note and self.sales_document_no):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{self.te}' and i.posting_date>='{self.p_from_date}' and i.posting_date<='{self.p_to_date}' and i.bill_no='{self.supplier_dell_note}' and i.name='{self.sales_document_no}' """
		elif (self.item_code and self.te and self.p_from_date and self.p_to_date and self.supplier_dell_note):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{self.te}' and i.posting_date>='{self.p_from_date}' and i.posting_date<='{self.p_to_date}' and i.bill_no='{self.supplier_dell_note}' """
		elif (self.item_code and self.te and self.sales_document_no and self.supplier_dell_note):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{self.te}' and i.name='{self.sales_document_no}' and i.bill_no='{self.supplier_dell_note}' """
		elif (self.item_code and self.te and self.sales_document_no and self.supplier_dell_note):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{self.te}' and i.name='{self.sales_document_no}' """
		elif (self.item_code and self.te and self.supplier and self.supplier_dell_note):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{self.te}' and i.supplier='{self.supplier}' and i.bill_no='{self.supplier_dell_note}' """
		elif (self.item_code and self.te and self.supplier):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{self.te}' and i.supplier='{self.supplier}' """
		# z
		elif (self.te and self.supplier and self.p_from_date and self.p_to_date and self.supplier_dell_note):
			conditions +=f"""where i.status='{self.te}' and i.supplier='{self.supplier}' and i.posting_date>='{self.p_from_date}' and i.posting_date<='{self.p_to_date}' and i.bill_no='{self.supplier_dell_note}' """
		elif (self.te and self.p_from_date and self.p_to_date and self.supplier_dell_note):
			conditions +=f"""where i.status='{self.te}' and i.posting_date>='{self.p_from_date}' and i.posting_date<='{self.p_to_date}' and i.bill_no='{self.supplier_dell_note}' """
		elif (self.te and self.supplier and self.p_from_date and self.p_to_date):
			conditions +=f"""where i.status='{self.te}' and i.supplier='{self.supplier}' and i.posting_date>='{self.p_from_date}' and i.posting_date<='{self.p_to_date}' """
		elif (self.te and self.serial_no and self.supplier_dell_note):
			conditions +=f"""where i.status='{self.te}' and si.serial_no='{self.serial_no}' and i.bill_no='{self.supplier_dell_note}' """
		elif (self.te and self.supplier and self.supplier_dell_note):
			conditions +=f"""where i.status='{self.te}' and i.supplier='{self.supplier}' and i.bill_no='{self.supplier_dell_note}'"""
		elif (self.te and self.supplier):
			conditions +=f"""where i.status='{self.te}' and i.supplier='{self.supplier}' """
		elif (self.te and self.p_from_date and self.p_to_date and self.supplier_dell_note):
			conditions +=f"""where i.status='{self.te}' and i.posting_date>='{self.p_from_date}' and i.posting_date<='{self.p_to_date}' and i.bill_no='{self.supplier_dell_note}' """
		elif (self.te and self.p_from_date and self.p_to_date):
			conditions +=f"""where i.status='{self.te}' and i.posting_date>='{self.p_from_date}' and i.posting_date<='{self.p_to_date}' """
		elif (self.te and self.sales_document_no and self.supplier_dell_note):
			conditions +=f"""where i.status='{self.te}' and i.name='{self.sales_document_no}' and i.bill_no='{self.supplier_dell_note}' """
		elif (self.te and self.sales_document_no and self.supplier_dell_note):
			conditions +=f"""where i.status='{self.te}' and i.name='{self.sales_document_no}' """
		elif (self.te and self.serial_no):
			conditions +=f"""where i.status='{self.te}' and si.serial_no='{self.serial_no}' """
		elif (self.item_code and self.te and self.supplier_dell_note):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{self.te}' and i.bill_no='{self.supplier_dell_note}' """
		# z
		elif (self.p_from_date and self.p_to_date and self.supplier_dell_note):
			conditions +=f"""where i.posting_date>='{self.p_from_date}' and i.posting_date<='{self.p_to_date}' and i.bill_no='{self.supplier_dell_note}' """
		elif (self.item_code and self.te):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{self.te}' """
		elif (self.item_code and self.supplier and self.supplier_dell_note):
			conditions +=f"""where si.item_code='{self.item_code}' and i.supplier='{self.supplier}' and i.bill_no='{self.supplier_dell_note}'"""
		elif (self.item_code and self.supplier):
			conditions +=f"""where si.item_code='{self.item_code}' and i.supplier='{self.supplier}' """
		elif (self.te and self.supplier_dell_note):
			conditions +=f"""where i.status='{self.te}' and i.bill_no='{self.supplier_dell_note}' """
		elif (self.supplier_dell_note):
			conditions +=f"""where i.bill_no='{self.supplier_dell_note}' """
		elif(self.te):
			conditions +=f"""where i.status='{self.te}' """
		elif(self.item_code):
			conditions +=f"""where si.item_code='{self.item_code}' """
		elif (self.serial_no):
			conditions +=f"""where si.serial_no='{self.serial_no}' """
		elif (self.supplier):
			conditions +=f"""where i.supplier='{self.supplier}' """
		elif (self.sales_document_no):
			conditions +=f"""where i.name='{self.sales_document_no}' """
		elif (self.p_from_date and self.p_to_date):
			conditions +=f"""where i.posting_date>='{self.p_from_date}' and i.posting_date<='{self.p_to_date}' """
		else:
			doc = frappe.db.sql(""" select si.serial_no,si.item_code,si.item_name,si.qty,si.image,si.warehouse,si.qty,si.standard_rate,si.precious_stone,si.semi_precious_stone,\
			si.material_use_abbv,si.stone_size,si.cz,si.diamond_size,si.weight,si.rate,i.posting_date,i.name,i.supplier,i.bill_no,i.status from `tabPurchase Invoice Item` as si left join `tabPurchase Invoice` as i  ON si.parent=i.name where i.status=%s""",(self.te))
			value = doc
		doc = frappe.db.sql(""" select si.serial_no,si.item_code,si.item_name,si.qty,si.image,si.warehouse,si.qty,si.standard_rate,si.precious_stone,si.semi_precious_stone,\
		si.material_use_abbv,si.stone_size,si.cz,si.diamond_size,si.weight,si.rate,i.posting_date,i.name,i.supplier,i.bill_no,i.status from `tabPurchase Invoice Item` as si left join `tabPurchase Invoice` as i  ON si.parent=i.name %s"""%conditions)
		value = doc
		self.total_rate = 0
		self.total_qty = 0
		self.grand_total = 0
		for v in value:
			if v[0]:
				row = self.append("report_record_details", {})
				row.serial_no = v[0]
				row.item_code = v[1]
				row.item_name = v[2]
				row.delivered_qty = v[3]
				row.upload_image = v[4]
				row.warehouse = v[5]
				row.qty = v[6]
				row.rate = v[7]
				row.precious_stone = v[8]
				row.semi_precious_stone = v[9]
				row.material_use_abbv = v[10]
				row.stone_size = v[11]
				row.cz = v[12]
				row.diamond_size = v[13]
				row.weight = v[14]
				row.price_list_rate = v[15]
				row.sales_date = v[16]
				row.supplier = v[18]
				row.bill_no = v[19]
				if self.te:
					row.status = self.te
				else:
					row.status = v[20]
				self.total_rate += v[15]
				self.total_qty += v[6]
				self.grand_total += v[6] * v[7]
			else:
				pass
	@frappe.whitelist(allow_guest=True)
	def getinvoice(self):
		self.report_record_details = ""
		value = {}
		conditions = ""
		if (self.s_status=="Delivered"):
			n_status = "Paid"
			s_status = "Delivered"
		else:
			n_status = self.s_status
			s_status = self.s_status
		if (self.item_code and self.s_status and self.serial_no and self.barcode and self.sales_date and self.to_date and self.sales_document_no and self.mop):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{n_status}' and si.serial_no='{self.serial_no}' and si.barcode='{self.barcode}' and i.posting_date>='{self.sales_date}' and i.posting_date<='{self.to_date}' and i.name='{self.sales_document_no}' and i.mop='{self.mop}' """
		elif (self.item_code and self.s_status and self.serial_no and self.barcode and self.sales_date and self.to_date and self.sales_document_no):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{n_status}' and si.serial_no='{self.serial_no}' and si.barcode='{self.barcode}' and i.posting_date>='{self.sales_date}' and i.posting_date<='{self.to_date}' and i.name='{self.sales_document_no}' """
		elif (self.item_code and self.s_status and self.serial_no and self.sales_date and self.to_date and self.mop):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{n_status}' and si.serial_no='{self.serial_no}' and i.posting_date>='{self.sales_date}' and i.posting_date<='{self.to_date}' and i.mop='{self.mop}' """
		elif (self.item_code and self.s_status and self.serial_no and self.sales_date and self.to_date):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{n_status}' and si.serial_no='{self.serial_no}' and i.posting_date>='{self.sales_date}' and i.posting_date<='{self.to_date}' """
		elif (self.item_code and self.s_status and self.serial_no and self.sales_document_no and self.to_date and self.mop):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{n_status}' and si.serial_no='{self.serial_no}' and i.name='{self.sales_document_no}' and i.mop='{self.mop}'"""
		elif (self.item_code and self.s_status and self.serial_no and self.sales_document_no and self.to_date):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{n_status}' and si.serial_no='{self.serial_no}' and i.name='{self.sales_document_no}'  """
		elif (self.item_code and self.s_status and self.serial_no and self.sales_document_no and self.mop):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{n_status}' and si.serial_no='{self.serial_no}' and i.name='{self.sales_document_no}' and i.mop='{self.mop}'"""
		elif (self.item_code and self.s_status and self.serial_no and self.sales_document_no):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{n_status}' and si.serial_no='{self.serial_no}' and i.name='{self.sales_document_no}' """
		elif (self.item_code and self.s_status and self.sales_document_no and self.sales_date and self.to_date and self.mop):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{n_status}' and i.name='{self.sales_document_no}' and i.posting_date>='{self.sales_date}' and i.posting_date<='{self.to_date}' and i.mop='{self.mop}'"""
		elif (self.item_code and self.s_status and self.sales_document_no and self.sales_date and self.to_date):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{n_status}' and i.name='{self.sales_document_no}' and i.posting_date>='{self.sales_date}' and i.posting_date<='{self.to_date}' """
		elif (self.item_code and self.s_status and self.barcode and self.sales_date and self.to_date and self.mop):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{n_status}' and si.barcode='{self.barcode}' and i.posting_date>='{self.sales_date}' and i.posting_date<='{self.to_date}' and i.mop='{self.mop}'"""
		elif (self.item_code and self.s_status and self.barcode and self.sales_date and self.to_date):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{n_status}' and si.barcode='{self.barcode}' and i.posting_date>='{self.sales_date}' and i.posting_date<='{self.to_date}' """
		elif (self.item_code and self.s_status and self.sales_date and self.to_date and self.mop):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{n_status}' and i.posting_date>='{self.sales_date}' and i.posting_date<='{self.to_date}' and i.mop='{self.mop}'"""
		elif (self.item_code and self.s_status and self.sales_date and self.to_date):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{n_status}' and i.posting_date>='{self.sales_date}' and i.posting_date<='{self.to_date}' """
		elif (self.item_code and self.s_status and self.serial_no and self.mop):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{n_status}' and si.serial_no='{self.serial_no}' and i.mop='{self.mop}' """
		elif (self.item_code and self.s_status and self.serial_no):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{n_status}' and si.serial_no='{self.serial_no}' """
		elif (self.item_code and self.s_status and self.barcode and self.mop):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{n_status}' and si.barcode='{self.barcode}' and i.mop='{self.mop}' """
		elif (self.item_code and self.s_status and self.barcode):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{n_status}' and si.barcode='{self.barcode}' """
		# item_code		
		elif (self.s_status and self.sales_date and self.to_date and self.sales_document_no and self.mop):
			conditions +=f"""where i.status='{n_status}' and i.posting_date>='{self.sales_date}' and i.posting_date<='{self.to_date}' and i.name='{self.sales_document_no}' and i.mop='{self.mop}' """
		elif (self.s_status and self.sales_date and self.to_date and self.sales_document_no):
			conditions +=f"""where i.status='{n_status}' and i.posting_date>='{self.sales_date}' and i.posting_date<='{self.to_date}' and i.name='{self.sales_document_no}' """
		elif (self.s_status and self.serial_no and self.mop):
			conditions +=f"""where i.status='{n_status}' and si.serial_no='{self.serial_no}' and i.mop='{self.mop}' """
		elif (self.s_status and self.sales_date and self.to_date and self.mop):
			conditions +=f"""where i.status='{n_status}' and i.posting_date>='{self.sales_date}' and i.posting_date<='{self.to_date}' and i.mop='{self.mop}' """
		elif (self.s_status and self.serial_no and self.sales_date and self.to_date):
			conditions +=f"""where i.status='{n_status}' and si.serial_no='{self.serial_no}' and i.posting_date>='{self.sales_date}' and i.posting_date<='{self.to_date}' """
		elif (self.s_status and self.sales_date and self.to_date):
			conditions +=f"""where i.status='{n_status}' and i.posting_date>='{self.sales_date}' and i.posting_date<='{self.to_date}' """
		elif (self.serial_no and self.sales_date and self.to_date):
			conditions +=f"""where si.serial_no='{self.serial_no}' and i.posting_date>='{self.sales_date}' and i.posting_date<='{self.to_date}' """
		elif (self.s_status and self.barcode and self.mop):
			conditions +=f"""where i.status='{n_status}' and si.barcode='{self.barcode}' and i.mop='{self.mop}' """
		elif (self.s_status and self.barcode):
			conditions +=f"""where i.status='{n_status}' and si.barcode='{self.barcode}' """
		elif (self.s_status and self.sales_document_no and self.mop):
			conditions +=f"""where i.status='{n_status}' and i.name='{self.sales_document_no}' and i.mop='{self.mop}' """
		elif (self.s_status and self.sales_document_no):
			conditions +=f"""where i.status='{n_status}' and i.name='{self.sales_document_no}' """
		elif (self.item_code and self.s_status and self.mop):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{n_status}' and i.mop='{self.mop}' """
		elif (self.item_code and self.s_status):
			conditions +=f"""where si.item_code='{self.item_code}' and i.status='{n_status}' """
		elif (self.s_status and self.serial_no):
			conditions +=f"""where i.status='{n_status}' and si.serial_no='{self.serial_no}' """
		elif (self.sales_date and self.to_date):
			conditions +=f"""where i.posting_date>='{self.sales_date}' and i.posting_date<='{self.to_date}' """
		elif(self.s_status):
			conditions +=f"""where i.status='{n_status}' """
		elif(self.item_code):
			conditions +=f"""where si.item_code='{self.item_code}' """
		elif (self.serial_no):
			conditions +=f"""where si.serial_no='{self.serial_no}' """
		elif (self.barcode):
			conditions +=f"""where si.barcode='{self.barcode}' """
		elif (self.mop):
			conditions +=f"""where i.mop='{self.mop}' """
		else:
			doc = frappe.db.sql(""" select si.serial_no,si.item_code,si.item_name,si.delivered_qty,si.image,si.warehouse,si.qty,si.rate,si.precious_stone,si.semi_precious_stone,\
			si.material_use_abbv,si.stone_size,si.cz,si.diamond_size,si.weight,si.valuation_rate,i.posting_date,i.name,i.mop,i.status from `tabSales Invoice Item` as si left join `tabSales Invoice` as i  ON si.parent=i.name where i.status='Paid'""")
			value = doc
		doc = frappe.db.sql(""" select si.serial_no,si.item_code,si.item_name,si.delivered_qty,si.image,si.warehouse,si.qty,si.rate,si.precious_stone,si.semi_precious_stone,\
		si.material_use_abbv,si.stone_size,si.cz,si.diamond_size,si.weight,si.valuation_rate,i.posting_date,i.name,i.mop,i.status from `tabSales Invoice Item` as si left join `tabSales Invoice` as i  ON si.parent=i.name %s"""%conditions)
		value = doc
		self.total_rate = 0
		self.total_qty = 0
		self.grand_total = 0
		for v in value:
			if v[0]:
				row = self.append("report_record_details", {})
				row.serial_no = v[0]
				row.item_code = v[1]
				row.item_name = v[2]
				row.delivered_qty = v[3]
				row.upload_image = v[4]
				row.warehouse = v[5]
				row.qty = v[6]
				row.rate = v[7]
				row.precious_stone = v[8]
				row.semi_precious_stone = v[9]
				row.material_use_abbv = v[10]
				row.stone_size = v[11]
				row.cz = v[12]
				row.diamond_size = v[13]
				row.weight = v[14]
				row.price_list_rate = v[15]
				row.sales_date = v[16]
				row.mop = v[18]
				if self.s_status:
					row.status = s_status
				else:
					row.status = v[19]
				self.total_rate += v[15]
				self.total_qty += v[6]
				self.grand_total += v[6] * v[7]
			else:
				pass