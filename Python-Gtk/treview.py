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
		self.agregar_entrada_monto()
		self.agregar_boton()
		self.agregar_lista()

	#contenedor.attach(
	#boton, #elemento
	#0, #columna
	#0, #fila
	#3, #no columnas a usar
	#1, # no filas a usar
	#)

	def agregar_contendor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)

	def agregar_entrada(self):
		self.entrada = Gtk.Entry()
		self.contenedor.attach(self.entrada, 0,0,2,1)

	def agregar_entrada_monto(self):
		self.entrada_monto = Gtk.Entry()
		self.contenedor.attach(self.entrada_monto, 2,0,1,1)

	def agregar_boton(self):
		self.boton = Gtk.Button('Agregar')
		self.contenedor.attach_next_to(
			self.boton,
			self.entrada,
			Gtk.PositionType.BOTTOM,
			3,
			1)
		self.boton.connect('clicked', self.agregar_fila)

	def agregar_lista(self):
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

	 	self.modelo = Gtk.ListStore(str, float, str)
	 	#self.modelo.append(['valor 1', 1.5, 'Cancelado'])

	 	self.lista_activos = Gtk.TreeView(self.modelo)

	 	descripcion = Gtk.CellRendererText()
	 	columna_descripcion = Gtk.TreeViewColumn('descripcion', descripcion, text=0)
	 	Gtk.TreeViewColumn.get_resizable(columna_descripcion)

	 	monto = Gtk.CellRendererText()
	 	columna_monto = Gtk.TreeViewColumn('Monto', monto, text=1)

	 	estado = Gtk.CellRendererText()
	 	columna_estado = Gtk.TreeViewColumn('Estado', estado, text=2)

	 	self.lista_activos.append_column(columna_descripcion)
	 	self.lista_activos.append_column(columna_monto)
	 	self.lista_activos.append_column(columna_estado)

	 	self.contenedor.attach_next_to(
	 		self.lista_activos,
	 		self.boton,
	 		Gtk.PositionType.BOTTOM,
	 		1,
	 		1
	 		)
	def agregar_fila(self, btn):
	  	texto = self.entrada.get_text()
	  	tmonto = self.entrada_monto.get_text()
	  	m =  float(tmonto)
	  	lista = self.entrada.get_text()
		if len(lista) >0:
			self.modelo.append([texto,m, 'Activo'])
		
		

if __name__ == '__main__':
	ventana = MiVentana()
	ventana.show_all()
	Gtk.main()
		
