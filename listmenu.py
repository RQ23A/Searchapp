from gi.repository import Gtk
from windows import Window
import json

class ListMenuWindow():

    def __init__(self):

        self.win = Window()
        self.win.set_title("List Options")
        self.win.set_size(400,250)

        table = Gtk.Table(1, 2, False)
        self.win.add_to_win(table)

        button = Gtk.Button("_Close", use_underline=True)
        button.connect("clicked", self.win.hide)

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

        self.win.show_all()

        accGroup = Gtk.AccelGroup()
        key, modifier = Gtk.accelerator_parse('Escape')
        accGroup.connect(key, modifier, Gtk.AccelFlags.VISIBLE, Gtk.main_quit)
        self.win.add_accel_group(accGroup)
