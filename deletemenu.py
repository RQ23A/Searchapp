from gi.repository import Gtk
import json
import sys

class DeleteMenuWindow():

	def __init__(self):

		win = Gtk.Window()
		win.set_title("Delete Menu")
		win.set_default_size(200,150)
		win.set_position(Gtk.WindowPosition.CENTER)
		win.connect("destroy", self.close_win)

		button1 = Gtk.Button("Delete")
		button1.connect("clicked", self.delete_menu)
		button2 = Gtk.Button("Close")
		button2.connect("clicked", self.close_win)

		table1 = Gtk.Table(1, 3, False)
		win.add(table1)
		table2 = Gtk.Table(2, 1, False)
		table1.attach(table2, 0, 1, 2, 3, xpadding=10, ypadding=10)
		table2.attach(button1, 0, 1, 0, 1, xpadding=10, ypadding=10)
		table2.attach(button2, 1, 2, 0, 1, xpadding=10, ypadding=10)

		label = Gtk.Label("Type the full name of what you want to delete. (Should be exactly as it is in the List option")
		self.to_delete = Gtk.Entry()
		table1.attach(label, 0, 1, 0, 1, xpadding=10, ypadding=10)
		table1.attach(self.to_delete, 0, 1, 1, 2, xpadding=10, ypadding=10)

		win.show_all()

	def close_win(self, win):

		Gtk.main_quit()

	def delete_menu(self, win):
		
		count = 0
		with open('config.json') as json_file:
			jsonfile = json.load(json_file)
		for i in jsonfile['all']:
			if i['name'] == self.to_delete.get_text():
				print i
				print count
				del jsonfile['all'][count]
				print "delete"
				break
			count += 1
		with open('config.json', 'w') as json_file:
			json.dump(jsonfile, json_file)
		sys.exit()
