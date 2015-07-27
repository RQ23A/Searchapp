from gi.repository import Gtk
import sys
import webbrowser
import json

class AddMenuWindow():
	
	def __init__(self):
		                
                win2 = Gtk.Window()
                win2.set_title("Add url")
                win2.set_default_size(400,250)
                win2.set_position(Gtk.WindowPosition.CENTER)
                win2.connect("destroy", self.close_win)

                table2 = Gtk.Table(4, 2, False)
                win2.add(table2)
                table3 = Gtk.Table(1, 2, False)

                self.name_textentry = Gtk.Entry()
                self.key_textentry = Gtk.Entry()
                self.url_textentry = Gtk.Entry()


                name_label = Gtk.Label("Name")
                key_label = Gtk.Label("Key")
                url_label = Gtk.Label("URL")

                button1 = Gtk.Button("_Close", use_underline=True)
                button1.connect("clicked", self.close_win)
                button2 = Gtk.Button("Ok")
                button2.connect("clicked", self.add_to_json)

                table2.attach(self.name_textentry, 1, 2, 0, 1, xpadding=10, ypadding=10)
                table2.attach(self.key_textentry, 1, 2, 1, 2, xpadding=10, ypadding=10)
                table2.attach(self.url_textentry, 1, 2, 2, 3, xpadding=10, ypadding=10)
                table2.attach(name_label, 0, 1, 0, 1, xpadding=5, ypadding=10)
                table2.attach(key_label, 0, 1, 1, 2, xpadding=5, ypadding=10)
                table2.attach(url_label, 0, 1, 2, 3, xpadding=5, ypadding=10)
                table2.attach(table3, 1, 2, 3, 4)
                table3.attach(button2, 0, 1, 0, 1, xpadding=5, ypadding=10)
                table3.attach(button1, 1, 2, 0, 1, xpadding=5, ypadding=10)
                win2.show_all()

        def close_win(self, win):

                Gtk.main_quit()

        def add_to_json(self, widget):

                name_textentry_text = self.name_textentry.get_text()
                key_textentry_text = self.key_textentry.get_text()
                url_textentry_text = self.url_textentry.get_text()
                new = {"name": name_textentry_text, "val": key_textentry_text, "url": url_textentry_text}
                with open('config.json') as json_file:
                    jsonfile = json.load(json_file)
                jsonfile['all'].append(new)
                with open('config.json', 'w') as json_file:
                    json.dump(jsonfile, json_file)
                Gtk.main_quit()

class Searchapp():

	def __init__(self):

		""" The constructor has all the windows' generators and menus. """

		win = Gtk.Window() # Generates empty window
		win.set_title("Searchapp") # Sets title
		win.set_default_size(400,70) # Sets size (x,y)
		win.set_position(Gtk.WindowPosition.CENTER) # Sets position
		win.connect("destroy", self.closeWin) # Close button action

		menu = Gtk.MenuBar() #Generates empty menu bar

		filemenu = Gtk.Menu() # Generates button on menu
		filem = Gtk.MenuItem("File") # Create name for button on menu
		filem.set_submenu(filemenu) # Attach "File" to button

		add = Gtk.MenuItem("Add") # Creates submenu
		add.connect("activate", self.add_menu) # Creates close action
		filemenu.append(add) # Append

		exit = Gtk.MenuItem("Exit") # Creates submenu
		exit.connect("activate", Gtk.main_quit) # Creates close action
		filemenu.append(exit) # Append


		helpmenu = Gtk.Menu()
		helpm = Gtk.MenuItem("Help")
		helpm.set_submenu(helpmenu)

		howto = Gtk.MenuItem("How to")
		howto.connect("activate", self.how_to_menu)
		helpmenu.append(howto)

		about = Gtk.MenuItem("About")
		about.connect("activate", self.about_menu)
		helpmenu.append(about)

		menu.append(filem) # Append the menus to the menu bar
		menu.append(helpm)

		vbox = Gtk.VBox(False, 10) # Orginize child widgets into a column (homogeneous,spacing between widgets)
		vbox.pack_start(menu, False, False, 0) # pack at top (child, expand, fill, padding)

		textentry = Gtk.Entry() # Create text box
		textentry.connect("activate", self.do_stuff) # Create action

		table = Gtk.Table(2, 1, False) # Create table to locate the widgets (rows, cols, homogeneous)
		win.add(table)

		table.attach(vbox,0,1,0,1) # Attach to talbe (widget, from x, to x, from y, to y)
		table.attach(textentry,0,1,1,2, xpadding=10,ypadding=10) # (xpadding, ypadding)

		win.show_all() # Display Window

	def closeWin(self, win):

		"""Function to close main window."""

		Gtk.main_quit()

	def how_to_menu(self, widget):

		"""Generates a dialog with the 'How to' instructions."""

		dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "How to use Searchapp")
		dialog.format_secondary_text("g = Google    y = Youtube    w = Wikipedia")
		dialog.run()

		dialog.destroy()

	def about_menu(self, widget):

		"""Generates an About Dialog. Can uncomment 'website'. Trying to fix the logo."""

		about = Gtk.AboutDialog()
		about.set_program_name("Searchapp")
		about.set_version("0.1")
		about.set_copyright("(c) 2015, RQ23A")
		about.set_comments("A quicker way to find your stuff.")
		about.set_logo_icon_name(None)
#		about.set_website("")
#		about.set_logo_icon_name(Gtk.gdk.pixbuf_new_from_file("search.png"))
		about.run()
		about.destroy()

	def add_menu(self, window):

		sub = AddMenuWindow()

	def do_stuff(self, widget):

		"""This function does the searches and pops up a windows for incorrect input."""

		text = widget.get_text() # Gets text from widget
		parsed = text.split(" ", 1) # Splits until the first space
		with open('config.json', 'rb') as json_file:
			for item in json.load(json_file)['all']:
				if parsed[0] == item['val']:
					webbrowser.open(item['url'] + parsed[1])
					sys.exit()
			else:
				dialog2 = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Error")
                        	dialog2.format_secondary_text("Doesn't work that way. See 'How to' on the Menu.")
                        	dialog2.run()
                        	dialog2.destroy()

# Main loop.
def main():
	app = Searchapp()
	Gtk.main()
if __name__ == "__main__":
	main()
