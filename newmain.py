#!/usr/bin/python

from gi.repository import Gtk

class Window():

    def __init__(self):

        self.win = Gtk.Window()
        self.win.set_position(Gtk.WindowPosition.CENTER)
        self.win.connect("destroy", Gtk.main_quit)

    def set_size(self, sizex, sizey):

        self.win.set_default_size(sizex,sizey)

    def set_title(self, title):

        self.win.set_title(title)

    def add_to_win(self, obj):

        self.win.add(obj)

    def show_all(self):

        self.win.show_all()

class MenuBar():

    def __init__(self):

        self.menu = Gtk.MenuBar()

        filemenu = Gtk.Menu()
        filem = Gtk.MenuItem("File")
        filem.set_submenu(filemenu)

        add = Gtk.MenuItem("Add")
        add.connect("activate", Actions().add_menu)
        filemenu.append(add)

        delete = Gtk.MenuItem("Delete")
        delete.connect("activate", Actions().add_menu)
        filemenu.append(delete)

        lst = Gtk.MenuItem("List")
        lst.connect("activate", Actions().add_menu)
        filemenu.append(lst)

        exit = Gtk.MenuItem("Exit")
        exit.connect("activate", Gtk.main_quit)
        filemenu.append(exit)

        self.menu.append(filem)

    def return_menu(self):

        return self.menu

class Actions():

    def add_menu(self, text):

        print "Hola mundo!"

class App():

    def __init__(self):

        self.app = Window()
        self.app.set_size(400,70)
        self.app.set_title("Searchapp")

        self.menuu = MenuBar()
        self.vbox = Gtk.VBox(False, 10)
        self.vbox.pack_start(self.menuu.return_menu, False, False, 0)

        self.textentry = Gtk.Entry()
        self.textentry.connect("activate", Actions().add_menu)

        self.table = Gtk.Table(2, 1, False)
        self.app.add_to_win(self.table)
        self.table.attach(self.vbox, 0, 1, 0, 1)
        self.table.attach(self.textentry, 0, 1, 1, 2, xpadding=10, ypadding=10)

        self.app.show_all()

    def add_menuu(self):

        print "Hola"

# Main loop

def main():
    app = App()
    Gtk.main()
if __name__=="__main__":
    main()
