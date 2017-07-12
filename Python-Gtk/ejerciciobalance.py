import gi 
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk




class VentanaBalance(Gtk.Window):
	
	def __init__(self, *args, **kwargs):
		super(VentanaBalance, self).__init__(*args, **kwargs)
		self.set_default_size(800, 400)
		self.connect('delete-event', Gtk.main_quit)
		self.agregar_contenedor_activo()
		self.agregar_label_activo()
		self.agregar_entradas_activos()
		self.agregar_boton_activo()
		self.agregar_lista_activos()



	def agregar_contenedor_activo(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)

		self.add(self.contenedor)

	def agregar_label_activo(self):
		self.lactivo = Gtk.Label('ACTIVOS')
		self.contenedor.attach(self.lactivo, 1,0,1,1)

	def agregar_entradas_activos(self):
		self.entradaA = Gtk.Entry()
		self.montoA = Gtk.Entry()
		self.contenedor.attach(self.entradaA, 0,1,2,1)
		self.contenedor.attach(self.montoA, 3,1,1,1)

	def agregar_boton_activo(self):
		self.boton_activo = Gtk.Button('Agregar Activo')
		self.contenedor.attach(self.boton_activo, 1,2,1,1)

	def agregar_lista_activos(self):
		self.modeloA = Gtk.ListStore(str, float)
		self.listaA = Gtk.TreeView(self.modeloA)

		descripcionA = Gtk.CellRendererText()
		columna_descripcionA = Gtk.TreeViewColumn('DESCRIPCION', descripcionA, text=0)

		montoA = Gtk.CellRendererText()
		columna_montoA = Gtk.TreeViewColumn('MONTO ACTIVO', montoA, text=1)

		self.listaA.append_column(columna_descripcionA)
		self.listaA.append_column(columna_montoA)

		self.contenedor.attach_next_to(
			self.listaA,
			self.boton_activo,
			Gtk.PositionType.BOTTOM,
			1,
			1
			)
		




if __name__ == '__main__':
	ventana = VentanaBalance()
	ventana.show_all()
	Gtk.main()





