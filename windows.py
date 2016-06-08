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

    def close_win(self, window):

        Gtk.main_quit()

    def add_accel_group(self, group):

        self.win.add_accel_group(group)

    def hide(self, widget):

        self.win.hide()

    def show_all(self):

        self.win.show_all()


class SecondWindows():

    def how_to_menu(self, widget):

        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "How to use Searchapp")
        dialog.format_secondary_text("g = Google    y = Youtube     w = Wikipedia")
        dialog.run()
        dialog.destroy()

    def about_menu(self, widget):

        about = Gtk.AboutDialog()
        about.set_program_name("Searchapp")
        about.set_version("1.2")
        about.set_copyright("(c) 2016, RQ23A")
        about.set_logo_icon_name(None)
        about.run()
        about.destroy()


