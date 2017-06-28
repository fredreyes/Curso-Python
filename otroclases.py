#mascota
#perro
#gato
#



class ClaseMascota(object):

	def __init__(self, nombre, comida):
		nombre = raw_input('Ingrese Nombre de Mascota :')
		comida = raw_input('Ingrese comida :')
		self.nombre = nombre
		self.comida = comida
	def obtenernombre(self):
		
		return 'El Nombre de es Mascota : ' +self.nombre
	def obtenercomida(self):
		return 'La Comida de Mascota es : ' + self.comida

class CPerro(ClaseMascota):
	def __init__(self, raza, nombre, comida):
		super(CPerro, self).__init__(nombre, comida)
		#CPerro.__init__(self, nombre) la usare solo cuando herede mas de una clase para ser explicito
		raza = raw_input('Ingrese la Raza del Perro :')
		self.raza = raza
	def obtenerrraza(self):
		return  'La raza del Perro es : ' + self.raza


if __name__ == '__main__':
	 
	 p = CPerro('','' ,'')
	 print p.obtenernombre()
	 print p.obtenercomida()
	 print p.obtenerrraza()

	