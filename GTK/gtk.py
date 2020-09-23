import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

win = Gtk.Window()

label = Gtk.Label()
label.set_text("I am a window")
label.set_size_request(200,200)

combo = Gtk.ComboBox()
combo.set_size_request(150,60)

win.add(label)
win.add(combo)

win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()