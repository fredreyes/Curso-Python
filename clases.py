#el object es donde va la herencia 
class MiClase(object):
	"""docstring for ClassName"""

	#aqui van los atributos

	#y funciones


	#el init  es invocado al instanciar la clases 
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		