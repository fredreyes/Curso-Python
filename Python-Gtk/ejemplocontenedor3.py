import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk



class MiVentana(Gtk.Window):
	def __init__(self, *args, **kwargs):
		super(MiVentana, self).__init__(*args, **kwargs)
		self.set_default_size(500,300)
		self.connect('delete-event', Gtk.main_quit)
		self.agregar_contenedor()
		self.agregartexto()
		self.agregarboton()
		self.agregarLabel()
	
	

	def agregar_contenedor(self):
		
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
		self.contenedor.set_row_homogeneous(False)
		self.add(self.contenedor)

	def agregartexto(self):
		self.texto = Gtk.Entry()
		self.contenedor.attach(self.texto, 0,0,1,1)
	

	def agregarboton(self):
		self.boton = Gtk.Button('Boton 1 ')
		self.boton.connect('clicked', self.cambiar)
		self.contenedor.attach(self.boton, 0,1,1,1)
		

	def agregarLabel(self):
		self.label = Gtk.Label('Texto a Pasar')
		self.contenedor.attach(self.label, 0,2,1,1)

	def cambiar(self, boton):
	    change = self.texto.get_text()
	    self.label.set_markup(change) 


if __name__ == '__main__':
	ventana = MiVentana()
	ventana.show_all()
	Gtk.main()
		


