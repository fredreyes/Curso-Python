#Import 
#Todos los imports van al inicio de los textos (modulos)
import argparse


variabele1 = 'Hola'
variable2 = 1
variable3 = 2.3

#CONCATENACION

cadena = 'Cadena uno' + 'cadena dos'


#Interpolacion
otra_cadena ='hola {}'.format('Freddy')
otra_cadena1 = 'Hola{0}{1}'.format('Freddy','Reyes')
otra_cadena2 = 'Hola {variable1} {variable2}'.format(variable1 ='Prueba',variable2='XD')




def mi_funcion(val):
    print('dentro de mi funcion') #esto es un comentario
    print(otra_cadena)
    print(otra_cadena2)
    print(otra_cadena2)

if __name__=='__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("Nombre")
	parser.add_argument("Apellido")
	args = parser.parse_args()
	print(args.Nombre)
	print(args.Apellido)

#Argument