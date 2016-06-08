#!/usr/bin/python

from gi.repository import Gtk
from windows import Window, SecondWindows
from menubar import MenuBar
from classes import StuffDoer
import json

class App():

    def __init__(self):

        self.app = Window()
        self.app.set_size(400,70)
        self.app.set_title("Searchapp")

        self.menuu = MenuBar()
        self.vbox = Gtk.VBox(False, 10)
        self.vbox.pack_start(self.menuu.return_menu(), False, False, 0)

        self.textentry = Gtk.Entry()
        self.textentry.connect("activate", self.do_stuff)

        self.table = Gtk.Table(2, 1, False)
        self.app.add_to_win(self.table)
        self.table.attach(self.vbox, 0, 1, 0, 1)
        self.table.attach(self.textentry, 0, 1, 1, 2, xpadding=10, ypadding=10)

        accGroup = Gtk.AccelGroup()
        key, modifier = Gtk.accelerator_parse('Escape')
        accGroup.connect(key, modifier, Gtk.AccelFlags.VISIBLE, Gtk.main_quit)
        self.app.add_accel_group(accGroup)

        self.app.show_all()

    def do_stuff(self, widget):

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
            if commandsdata[0]['val'] == 'false' and len(parsed) > 1:
                StuffDoer().search_common(parsed[0], parsed[1])
            else:
                dialog2 = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Error")
                dialog2.format_secondary_text("Doesn't work that way. See 'How to' on the Menu.")
                dialog2.run()
                dialog2.destroy()

# Main loop

def main():
    app = App()
    Gtk.main()
if __name__=="__main__":
    main()
