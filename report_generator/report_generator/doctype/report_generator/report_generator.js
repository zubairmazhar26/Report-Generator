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
		frm.save()
	},

	fetch_record: function(frm) {
		
		if (frm.doc.select_doctype == "Sales Invoice") {
			frm.call("getinvoice")
		} else{
			frm.call("getpinvoice")
		}
		frm.save()
		
		
	},
	te: function(frm) {
		frm.save()
	},
	s_status: function(frm) {
		frm.save()
	},
	serial_no: function(frm) {
		frm.save()
	},
	item_code: function(frm) {
		frm.save()
	}
});
