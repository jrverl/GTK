import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ListBoxWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Language Selector")
        self.set_border_width(8)

        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)
        label0 = Gtk.Label("Seleccione Curso",xalign = 3)
        box_outer.pack_start (label0,True, True,0)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Java", xalign=0)
        link = Gtk.LinkButton("https://docs.oracle.com/javase/7/docs/api/","Ir al Sitio Web")
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(link, False, True, 0)

        listbox.add(row)

	row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("C", xalign=0)
        link = Gtk.LinkButton("http://devdocs.io/c/","Ir al Sitio Web")
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(link, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Python", xalign=0)
        link = Gtk.LinkButton("https://www.python.org/doc/","Ir al Sitio Web")
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(link, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("JavaScript", xalign=0)
        link = Gtk.LinkButton("http://usejsdoc.org/","Ir al Sitio Web")
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(link, False, True, 0)

        listbox.add(row)

def main():
    win = ListBoxWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if  __name__ == "__main__":
    main()
        
