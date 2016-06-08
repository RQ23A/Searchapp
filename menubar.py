#!/usr/bin/python

from gi.repository import Gtk
from addmenu import AddMenuWindow
from windows import SecondWindows

class MenuBar():

    def __init__(self):

        self.menu = Gtk.MenuBar()

        filemenu = Gtk.Menu()
        filem = Gtk.MenuItem("File")
        filem.set_submenu(filemenu)

        add = Gtk.MenuItem("Add")
        add.connect("activate", self.add_menu)
        filemenu.append(add)

#        delete = Gtk.MenuItem("Delete")
#        delete.connect("activate", Actions().add_menu)
#        filemenu.append(delete)

#        lst = Gtk.MenuItem("List")
#        lst.connect("activate", Actions().add_menu)
#        filemenu.append(lst)

        exit = Gtk.MenuItem("Exit")
        exit.connect("activate", Gtk.main_quit)
        filemenu.append(exit)

        helpmenu = Gtk.Menu()
        helpm = Gtk.MenuItem("Help")
        helpm.set_submenu(helpmenu)

        howto = Gtk.MenuItem("How to")
        howto.connect("activate", SecondWindows().how_to_menu)
        helpmenu.append(howto)

        about = Gtk.MenuItem("About")
        about.connect("activate", SecondWindows().about_menu)
        helpmenu.append(about)

        self.menu.append(filem)
        self.menu.append(helpm)

    def return_menu(self):

        return self.menu

    def add_menu(self, window):

        addmenu = AddMenuWindow()
