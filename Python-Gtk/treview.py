import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MiVentana(Gtk.Window):
	def __init__(self, *args, **kwargs):
		super(MiVentana, self).__init__(*args, **kwargs)
		self.set_default_size(500,300)
		self.connect('delete-event', Gtk.main_quit)
		
		self.agregar_contendor()
		self.agregar_entrada()
		self.agregar_boton()

	def agregar_contendor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)

	def agregar_entrada(self):
		self.entrada = Gtk.Entry()
		self.contenedor.attach(self.entrada, 0,0,1,1)

	def agregar_boton(self):
		self.boton = Gtk.Button('Agregar')
		self.contenedor.attach_next_to(
			self.boton,
			self.entrada,
			Gtk.PositionType.BOTTOM,
			1,
			1)

	def agregar_Lista(self):
		"""

	 	1 pasos  crear un treview
	 	2 crear el model de datos (Gtk.ListStore(type, type...type))
	 	3 crear el widget que contineneo muestre los datos de modelo treview<model>
	 	4 definir las columnas y su contendio
	 	4.1 crear celda para cada columna de la fila, los cellrenderes son widgedes
	 	que sirven para mostrar contenido dentro de otro 
	 	4.2 crear columna TreeViewColumn del Tree View mostraran los datos usando args. (titulo, cellRenderer,posicion
	 	del modelo de la info a mostar)
	 	4.3 agregar cada TreeViewColumn  al TreeView widget
	 	"""

	 	self.modelo = Gtk.ListStore(str, float)

	 	self.modelo.append(['valor 1', 1.5])

	 	self.lista_activos = Gtk.TreeView(self.modelo)

	 	descripcion = Gtk.CellRendererText()
	 	columna_descripcion = Gtk.TreeViewColumn('descripcion', descripcion, text=0)

	 	monto = Gtk.CellRendererText()
	 	columna_monto = Gtk.TreeViewColumn('Monto', monto, text=1)

	 	self.lista_activos.append_column(columna_descripcion)
	 	self.lista_activos.append_column(columna_monto)

	 	self.contenedor.attach_next_to(
	 		self.lista_activos,
	 		self.boton,
	 		Gtk.PositionType.BOTTOM,
	 		1,
	 		1
	 		)

	 	





if __name__ == '__main__':
	ventana = MiVentana()
	ventana.show_all()
	Gtk.main()
		
