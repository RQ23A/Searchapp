from gi.repository import Gtk
import json

class ListMenuWindow():

	def __init__(self):

		win = Gtk.Window()
		win.set_title("List Options")
		win.set_default_size(400,250)
		win.set_position(Gtk.WindowPosition.CENTER)
		win.connect("destroy", self.close_win)
		
		table = Gtk.Table(1, 2, False)
		win.add(table)
		
		button = Gtk.Button("_Close", use_underline=True)
		button.connect("clicked", self.close_win)

		table.attach(button, 0, 1, 1, 2, xpadding=10, ypadding=10)
		check_button = Gtk.CheckButton

		with open('config.json') as json_file:
			jsonfile = json.load(json_file)

		count = len(jsonfile['all'])
		table2 = Gtk.Table(1, count, False)
		table.attach(table2, 0, 1, 0, 1, xpadding=10, ypadding=10)
		poss = 0
		for label in jsonfile['all']:
			label_text = Gtk.Label(label['name'])
			table2.attach(label_text, 0, 1, poss, poss+1, xpadding=10, ypadding=10)
			poss += 1

		win.show_all()

	def close_win(self, win):

		Gtk.main_quit()
