"""2. Crear un script para:
   Recibir un nombre y verificar si existe en el diccionario dado.
   'La llave <nombre> existe en el diccionario generado.' o
   'La llave <nombre> no existe en el diccionario'
"""
def recibirnombre():
	name = raw_input('Ingrese un nombre de llave :')
	nombres ={
	    'names ' : 'pedro'
	}
	if nombres.has_key(name):
		print(' la llave  existe')
	else:
		print('no existe')

if __name__ == '__main__':
	print 'Empecemos'
	recibirnombre()
	
