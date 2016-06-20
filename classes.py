from gi.repository import Gtk
import webbrowser
import json
import sys

class StuffDoer:

    def search_default(self, text):

        with open('config.json', 'rb') as json_file:
            data = json.load(json_file)
            alldata = data['all']
            commandsdata = data['commands']
            webbrowser.open(commandsdata[0]['url'] + text)
            sys.exit()

    def set_default(self, key):

        with open('config.json', 'r+') as json_file:
            data = json.load(json_file)
            alldata = data['all']
            commandsdata = data['commands']
            for item in alldata:
                if key == item['val']:
                    url = item['url']
            commandsdata[0]['val'] = 'true'
            commandsdata[0]['key'] = key
            commandsdata[0]['url'] = url
            json_file.seek(0, 0)
            json.dump(data, json_file, indent=4, sort_keys=True)
            json_file.truncate()
            sys.exit()

    def set_default_none(self):

        with open('config.json', 'r+') as json_file:
            data = json.load(json_file)
            commandsdata = data['commands']
            commandsdata[0]['val'] = 'false'
            commandsdata[0]['key'] = ''
            commandsdata[0]['url'] = ''
            json_file.seek(0, 0)
            json.dump(data, json_file, indent=4, sort_keys=True)
            json_file.truncate()
            sys.exit()

    def search_common(self, key, search):

        with open('config.json', 'rb') as json_file:
            data = json.load(json_file)
            alldata = data['all']
            for item in alldata:
                if key == item['val']:
                    url = self.replace_string(item['url'], search)
                    webbrowser.open(url)
                    sys.exit()
            else:
                dialog2 = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Error")
                dialog2.format_secondary_text("Doesn't work that way. See 'How to' on the Menu.")
                dialog2.run()
                dialog2.destroy()
 
    def replace_string(self, string, search):

        return string.replace("<searchapp>", search)
