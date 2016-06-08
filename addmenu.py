from gi.repository import Gtk
from windows import Window
import sys
import json

class AddMenuWindow():
    
    def __init__(self):
                        
        self.win = Window()
        self.win.set_title("Add url")
        self.win.set_size(400,250)

        table2 = Gtk.Table(4, 2, False)
        self.win.add_to_win(table2)
        table3 = Gtk.Table(1, 2, False)

        self.name_textentry = Gtk.Entry()
        self.key_textentry = Gtk.Entry()
        self.url_textentry = Gtk.Entry()


        name_label = Gtk.Label("Name")
        key_label = Gtk.Label("Key")
        url_label = Gtk.Label("URL")

        button1 = Gtk.Button("_Close", use_underline=True)
        button1.connect("clicked", self.win.hide)
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
        self.win.show_all()

        accGroup = Gtk.AccelGroup()
        key, modifier = Gtk.accelerator_parse('Escape')
        accGroup.connect(key, modifier, Gtk.AccelFlags.VISIBLE, Gtk.main_quit)
        self.win.add_accel_group(accGroup)

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
        sys.exit()


