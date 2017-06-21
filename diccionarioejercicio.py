"""
1. Crear un script para
 - Recibir args ‘nombre’, ‘edad’, ‘clase’ y
   crear un diccionario de la forma:
       estudiante = {
           'nombre': <nombre>,
           'edad': <edad>,
           'curso': <curso>
       }

estudiante ={  
    'Nombre' : nombre,
    'Edad' : edad,
    'Curso' : curso
}   
"""
 
def buscar(nombre):
	return nombre in estudiante

def obtener_argumentos():

    nombre = raw_input('INGRESE NOMBRE: ')
    edad = raw_input('INGRESE EDAD : ')
    curso = raw_input('INGRESE CURSO :')

    if buscar(nombre):
    	print 'El nombre {nombre} existe como llave'.format(nombre=nombre)
	
 	
if __name__ == '__main__':
	print(Estudiante)

	obtener_argumentos()

	
