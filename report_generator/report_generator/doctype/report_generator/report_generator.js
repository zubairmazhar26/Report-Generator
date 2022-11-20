// Copyright (c) 2022, zubairmazhar23@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Report Generator', {
	refresh: function(frm) {
		frm.add_custom_button(__("Print"), function () {
			var w = window.open("/printview?doctype=Report Generator&name=" + cur_frm.doc.name + "&trigger_print=1&format=Serial Report&no_letterhead=0&_lang=en");

			if (!w) {
				frappe.msgprint(__("Please enable pop-ups")); return;
			}
		})
		frm.doc.check = "0"
	},
	select_doctype: function(frm) {
		frm.doc.sales_document_no = ""
		frm.save()
	},

	fetch_record: function (frm) {

		if (frm.doc.select_doctype == "Serial No") {
			frm.call("getrecord")
		}
		else if (frm.doc.select_doctype == "Sales Invoice") {
			frm.call("getinvoice")
		} else if (frm.doc.select_doctype == "Purchase Invoice") {
			frm.call("getpinvoice")
		} else { }
		frm.save()


	},

	fetch_record_pi: function (frm) {

		if (frm.doc.select_doctype == "Serial No") {
			frm.call("getrecord")
		}
		else if (frm.doc.select_doctype == "Sales Invoice") {
			frm.call("getinvoice")
		} else if (frm.doc.select_doctype == "Purchase Invoice") {
			frm.call("getpinvoice")
		} else { }
		frm.save()


	},
	fetch_record_sn: function (frm) {

		if (frm.doc.select_doctype == "Serial No") {
			frm.call("getrecord")
		}
		else if (frm.doc.select_doctype == "Sales Invoice") {
			frm.call("getinvoice")
		} else if (frm.doc.select_doctype == "Purchase Invoice") {
			frm.call("getpinvoice")
		} else { }
		frm.save()


	},
	te: function(frm) {
		frm.save()
	},
	s_status: function(frm) {
		frm.save()
	},
	ser_status: function(frm) {
		frm.save()
	},
	serial_no: function(frm) {
		frm.save()
	},
	item_code: function(frm) {
		frm.save()
	},


	sales_date: function(frm) {
		frm.save()
	},

	sales_document_no: function(frm) {
		frm.save()
	},
	supplier: function(frm) {
		frm.save()
	},
	creation_document_no: function(frm) {
		frm.save()
	},
	barcode: function(frm) {
		frm.save()
	},
	serial_no: function(frm) {
		frm.save()
	},
	serial_no: function(frm) {
		frm.save()
	},
});
