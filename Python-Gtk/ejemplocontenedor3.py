import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):
	def __init__(self, *args, **kwargs):
		super(MiVentana, self).__init__(*args, **kwargs)
		self.set_default_size(500,300)
		self.connect('delete-event', Gtk.main_quit)
		agregar_contenedor()

		def agregar_contenedor(self):
			self.MiVentana = contenedor
			contenedor = Gtk.Grid()
			contenedor.set_column_homogeneous(True)
			contenedor.set_row_homogeneous(False)
			texto = Gtk.Entry()
			#self.Gtk.Entry.set_text('Texto')
			contenedor.attach(texto,0,0,3,1)
			self.MiVentana.add(contenedor)
			

if __name__ == '__main__':
	ventana = MiVentana()
	ventana.show_all()
	Gtk.main()
		