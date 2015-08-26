from gi.repository import Gtk
import sys
import webbrowser
import json
from addmenu import AddMenuWindow
from classes import StuffDoer

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
			data = json.load(json_file)
			alldata = data['all']
			commandsdata = data['commands']
			if parsed[0] == '!default' and parsed[1] == 'none':
				StuffDoer().set_default_none()
			if parsed[0] == '!default' and parsed[1] != 'none':
				StuffDoer().set_default(parsed[1])
			if commandsdata[0]['val'] == 'true':
				StuffDoer().search_default(text)
			if commandsdata[0]['val'] == 'false':
				StuffDoer().search_common(parsed[0], parsed[1])
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
