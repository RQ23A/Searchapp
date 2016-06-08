#!/usr/bin/python

from gi.repository import Gtk
from windows import Window, SecondWindows
from menubar import MenuBar

class App():

    def __init__(self):

        self.app = Window()
        self.app.set_size(400,70)
        self.app.set_title("Searchapp")

        self.menuu = MenuBar()
        self.vbox = Gtk.VBox(False, 10)
        self.vbox.pack_start(self.menuu.return_menu(), False, False, 0)

        self.textentry = Gtk.Entry()
        self.textentry.connect("activate", self.write)

        self.table = Gtk.Table(2, 1, False)
        self.app.add_to_win(self.table)
        self.table.attach(self.vbox, 0, 1, 0, 1)
        self.table.attach(self.textentry, 0, 1, 1, 2, xpadding=10, ypadding=10)

        accGroup = Gtk.AccelGroup()
        key, modifier = Gtk.accelerator_parse('Escape')
        accGroup.connect(key, modifier, Gtk.AccelFlags.VISIBLE, Gtk.main_quit)
        self.app.add_accel_group(accGroup)

        self.app.show_all()

    def write(self, text):

        print "Hola mundo!"

# Main loop

def main():
    app = App()
    Gtk.main()
if __name__=="__main__":
    main()
