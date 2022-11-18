# Copyright (c) 2022, zubairmazhar23@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ReportGenerator(Document):
	def validate(self):
		pass
	@frappe.whitelist(allow_guest=True)
	def getrecord(self):
		self.report_record_details = ""
		value = {}
		conditions = " "
		if (self.te and self.item_code):
			doc = frappe.db.sql(""" select item_code,item_name,warehouse,batch_no,status,upload_image,name,company from `tabSerial No` where status=%s and item_code=%s """,(self.te, self.item_code))
			value = doc
		elif (self.te):
			doc = frappe.db.sql(""" select item_code,item_name,warehouse,batch_no,status,upload_image,name,company from `tabSerial No` where status=%s """,(self.te))
			value = doc
		elif (self.item_code):
			doc = frappe.db.sql(""" select item_code,item_name,warehouse,batch_no,status,upload_image,name,company from `tabSerial No` where item_code=%s """,(self.item_code))
			value = doc
		elif (self.serial_no):
			doc = frappe.db.sql(""" select item_code,item_name,warehouse,batch_no,status,upload_image,name,company from `tabSerial No` where serial_no=%s """,(self.serial_no))
			value = doc
		else:
			doc = frappe.db.sql(""" select item_code,item_name,warehouse,batch_no,status,upload_image,name,company from `tabSerial No` """)
			value = doc
		for a in value:
			row = self.append("report_record_details", {})
			row.item_code = a[0]
			row.item_name = a[1]
			row.warehouse = a[2]
			row.batch_no = a[3]
			row.status = a[4]
			row.upload_image = a[5]
			row.serial_no = a[6]
			row.company = a[7]
	@frappe.whitelist(allow_guest=True)
	def getpinvoice(self):
		self.report_record_details = ""
		value = {}
		conditions = " "
		if (self.item_code and self.te):
			doc = frappe.db.sql(""" select si.serial_no,si.item_code,si.item_name,si.qty,si.image,si.warehouse,si.qty,si.rate,si.precious_stone,si.semi_precious_stone,\
			si.material_use_abbv,si.stone_size,si.cz,si.diamond_size,si.weight,si.price_list_rate,i.posting_date,i.name from `tabPurchase Invoice Item` as si left join `tabPurchase Invoice` as i  ON si.parent=i.name where si.item_code=%s and i.status=%s""",(self.item_code, self.te))
			value = doc
		elif(self.te):
			doc = frappe.db.sql(""" select si.serial_no,si.item_code,si.item_name,si.qty,si.image,si.warehouse,si.qty,si.rate,si.precious_stone,si.semi_precious_stone,\
			si.material_use_abbv,si.stone_size,si.cz,si.diamond_size,si.weight,si.price_list_rate,i.posting_date,i.name from `tabPurchase Invoice Item` as si left join `tabPurchase Invoice` as i  ON si.parent=i.name where i.status=%s""",(self.te))
			value = doc
		elif(self.item_code):
			doc = frappe.db.sql(""" select si.serial_no,si.item_code,si.item_name,si.qty,si.image,si.warehouse,si.qty,si.rate,si.precious_stone,si.semi_precious_stone,\
			si.material_use_abbv,si.stone_size,si.cz,si.diamond_size,si.weight,si.price_list_rate,i.posting_date,i.name from `tabPurchase Invoice Item` as si left join `tabPurchase Invoice` as i  ON si.parent=i.name where si.item_code=%s """,(self.item_code))
			value = doc
		elif (self.serial_no):
			doc = frappe.db.sql(""" select si.serial_no,si.item_code,si.item_name,si.qty,si.image,si.warehouse,si.qty,si.rate,si.precious_stone,si.semi_precious_stone,\
			si.material_use_abbv,si.stone_size,si.cz,si.diamond_size,si.weight,si.price_list_rate,i.posting_date,i.name from `tabPurchase Invoice Item` as si left join `tabPurchase Invoice` as i  ON si.parent=i.name where si.serial_no=%s""",(self.serial_no))
			value = doc
		else:
			doc = frappe.db.sql(""" select si.serial_no,si.item_code,si.item_name,si.qty,si.image,si.warehouse,si.qty,si.rate,si.precious_stone,si.semi_precious_stone,\
			si.material_use_abbv,si.stone_size,si.cz,si.diamond_size,si.weight,si.price_list_rate,i.posting_date,i.name from `tabPurchase Invoice Item` as si left join `tabPurchase Invoice` as i  ON si.parent=i.name where i.status=%s""",(self.te))
			value = doc
		for v in value:
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
			row.status = self.te
	@frappe.whitelist(allow_guest=True)
	def getinvoice(self):
		self.report_record_details = ""
		value = {}
		conditions = " "
		if (self.s_status=="Delivered"):
			n_status = "Paid"
			s_status = "Delivered"
		else:
			n_status = self.s_status
			s_status = self.s_status
		if (self.item_code and self.s_status):
			doc = frappe.db.sql(""" select si.serial_no,si.item_code,si.item_name,si.delivered_qty,si.image,si.warehouse,si.qty,si.rate,si.precious_stone,si.semi_precious_stone,\
			si.material_use_abbv,si.stone_size,si.cz,si.diamond_size,si.weight,si.price_list_rate,i.posting_date,i.name from `tabSales Invoice Item` as si left join `tabSales Invoice` as i  ON si.parent=i.name where si.item_code=%s and i.status=%s""",(self.item_code, n_status))
			value = doc
		elif(self.s_status):
			doc = frappe.db.sql(""" select si.serial_no,si.item_code,si.item_name,si.delivered_qty,si.image,si.warehouse,si.qty,si.rate,si.precious_stone,si.semi_precious_stone,\
			si.material_use_abbv,si.stone_size,si.cz,si.diamond_size,si.weight,si.price_list_rate,i.posting_date,i.name from `tabSales Invoice Item` as si left join `tabSales Invoice` as i  ON si.parent=i.name where i.status=%s""",(n_status))
			value = doc
		elif(self.item_code):
			doc = frappe.db.sql(""" select si.serial_no,si.item_code,si.item_name,si.delivered_qty,si.image,si.warehouse,si.qty,si.rate,si.precious_stone,si.semi_precious_stone,\
			si.material_use_abbv,si.stone_size,si.cz,si.diamond_size,si.weight,si.price_list_rate,i.posting_date,i.name from `tabSales Invoice Item` as si left join `tabSales Invoice` as i  ON si.parent=i.name where si.item_code=%s """,(self.item_code))
			value = doc
		elif (self.serial_no):
			doc = frappe.db.sql(""" select si.serial_no,si.item_code,si.item_name,si.delivered_qty,si.image,si.warehouse,si.qty,si.rate,si.precious_stone,si.semi_precious_stone,\
			si.material_use_abbv,si.stone_size,si.cz,si.diamond_size,si.weight,si.price_list_rate,i.posting_date,i.name from `tabSales Invoice Item` as si left join `tabSales Invoice` as i  ON si.parent=i.name where si.serial_no=%s""",(self.serial_no))
			value = doc
		else:
			doc = frappe.db.sql(""" select si.serial_no,si.item_code,si.item_name,si.delivered_qty,si.image,si.warehouse,si.qty,si.rate,si.precious_stone,si.semi_precious_stone,\
			si.material_use_abbv,si.stone_size,si.cz,si.diamond_size,si.weight,si.price_list_rate,i.posting_date,i.name from `tabSales Invoice Item` as si left join `tabSales Invoice` as i  ON si.parent=i.name where i.status='Paid'""")
			value = doc
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
				row.status = s_status
			else:
				pass