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
		self.agregar_label_Pasivo()
		self.agregar_entradas_pasivos()
		self.agregar_boton_pasivo()
		self.agregar_lista_Pasivo()


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
		self.contenedor.attach_next_to(self.montoA, self.entradaA, Gtk.PositionType.RIGHT, 1,1)

	def agregar_boton_activo(self):
		self.boton_activo = Gtk.Button('Agregar Activo')
		self.contenedor.attach(self.boton_activo, 1,2,1,1)
		self.boton_activo.connect('clicked', self.agregar_fila_activo)

	def agregar_lista_activos(self):
		self.modeloA = Gtk.ListStore(str, float)
		self.listaA = Gtk.TreeView(self.modeloA)

		descripcionA = Gtk.CellRendererText()
		descripcionA.set_property('editable', True)
		descripcionA.connect('edited', self.texto_editado_activo)
		columna_descripcionA = Gtk.TreeViewColumn('DESCRIPCION', descripcionA, text=0)
		
		montoA = Gtk.CellRendererText()
		montoA.set_property('editable', True)
		montoA.connect('edited', self.monto_editado_activo)

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
	#editar datos del modelo

	def texto_editado_activo(self, widget, path, text):
		self.modeloA[path][0] = text

	def monto_editado_activo(self, widget, path, text):
		self.modeloA[path][1]= float(text)
		
		
	def agregar_fila_activo(self, btn):
		texto = self.entradaA.get_text()
		tmontoA = self.montoA.get_text()
		lista = self.entradaA.get_text()
		if len(lista) >0:
			self.modeloA.append([texto,float(tmontoA)])

			# ***********************************pasivos ****************************************************


	def agregar_label_Pasivo(self):
		self.lpasivo = Gtk.Label('Pasivos')
		self.contenedor.attach_next_to(self.lpasivo, self.listaA, Gtk.PositionType.BOTTOM,1,2)
	
	def agregar_entradas_pasivos(self):
		self.entradaP = Gtk.Entry()
		self.montoP = Gtk.Entry()
		self.contenedor.attach(self.entradaP, 0,6,2,1)
		self.contenedor.attach_next_to(self.montoP, self.entradaP, Gtk.PositionType.RIGHT, 1,1)

	def agregar_boton_pasivo(self):
		self.botonP = Gtk.Button('AGREGAR PASIVOS')
		self.contenedor.attach(self.botonP, 1,7,1,1)
		self.botonP.connect('clicked', self.agregar_fila_pasivo)

	def agregar_lista_Pasivo(self):
		self.modeloP = Gtk.ListStore(str, float)
		self.listaP = Gtk.TreeView(self.modeloP)

		descripcionP = Gtk.CellRendererText()
		descripcionP.set_property('editable', True)
		descripcionP.connect('edited', self.texto_editado_pasivo)

		columna_descripcionP = Gtk.TreeViewColumn('DESCRIPCION', descripcionP, text=0)

		montoPasivo = Gtk.CellRendererText()
		montoPasivo.set_property('editable', True)
		montoPasivo.connect('edited', self.monto_editado_pasivo)
		columna_montoP = Gtk.TreeViewColumn('MONTO PASIVO', montoPasivo, text = 1)

		self.listaP.append_column(columna_descripcionP)
		self.listaP.append_column(columna_montoP)

		self.contenedor.attach_next_to(
			self.listaP,
			self.botonP,
			Gtk.PositionType.BOTTOM,
			1,1)

	def texto_editado_pasivo(self, widget, path, text):
		self.modeloP[path][0] = text

	def monto_editado_pasivo(self, widget, path, text):
		self.modeloP[path][1]= float(text)





	def agregar_fila_pasivo(self, btn):
		textpP = self.entradaP.get_text()
		lmontoP = self.montoP.get_text()
		listaPA = self.entradaP.get_text()
		if  len(listaPA) >0:
			self.modeloP.append([textpP, float(lmontoP)])


if __name__ == '__main__':
	ventana = VentanaBalance()
	ventana.show_all()
	Gtk.main()





