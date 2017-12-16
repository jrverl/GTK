import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def main():
    win = Gtk.Window()
    box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    listbox = Gtk.ListBox()
    listbox.set_selection_mode(Gtk.SelectionMode.NONE)
    box_outer.pack_start(listbox, True, True, 0)

    row = Gtk.ListBoxRow()
    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
    row.add(hbox)
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    hbox.pack_start(vbox, True, True, 0)

    label1 = Gtk.Label("Automatic Date & Time", xalign=0)
    label2 = Gtk.Label("Requires internet access", xalign=0)
    vbox.pack_start(label1, True, True, 0)
    vbox.pack_start(label2, True, True, 0)

    switch = Gtk.Switch()
    switch.props.valign = Gtk.Align.CENTER
    hbox.pack_start(switch, False, True, 0)

    listbox.add(row)

    row = Gtk.ListBoxRow()
    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
    row.add(hbox)
    label = Gtk.Label("Enable Automatic Update", xalign=0)
    check = Gtk.CheckButton()
    hbox.pack_start(label, True, True, 0)
    hbox.pack_start(check, False, True, 0)

    listbox.add(row)

    row = Gtk.ListBoxRow()
    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
    row.add(hbox)
    label = Gtk.Label("Date Format", xalign=0)
    combo = Gtk.ComboBoxText()
    combo.insert(0, "0", "24-hour")
    combo.insert(1, "1", "AM/PM")
    hbox.pack_start(label, True, True, 0)
    hbox.pack_start(combo, False, True, 0)

    listbox.add(row)    

    win.add(listbox)
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if  __name__ == "__main__":
    main()
