import random

NOMBRES = [
    'Ana',
    'Pedro',
    'Pablo',
    'Ernesto',
    'Ariel',
    'Carlos',
    'Luis',
    'Oscar',
    'Alicia',
    'Maria',
    'Brenda'
]

CIUDADES = [
    'Managua',
    'Masaya',
    'Matagalpa',
    'Chinandega',
    'Somoto',
    'Rivas'
]


def generar_diccionario_estudiantes():
    estudiantes = {}

    for nombre in NOMBRES:
        estudiantes[nombre] = {
            'edad': random.randrange(16, 30),
            'anio': random.randrange(1, 5),
            'cuidad': random.choice(CIUDADES)
        }      	
    return estudiantes

def imprimirestudiante():
	dic = generar_diccionario_estudiantes()
	for llave, valor in dic.iteritems():
            print 'El alumno {alumno} es de la edad de {edad} ciudad de {cuidad} y cursa el anio{anio}'.format(alumno=llave , edad=valor['edad'], cuidad=valor['cuidad'], anio=valor['anio'])
            

def estudianteManagua():
    archivo = open('ww.txt', 'w')
    dic = generar_diccionario_estudiantes()
    for llave, valor in dic.iteritems():
        if 'Managua' == valor['cuidad']:
            linea = ('EL Alumno {alumno} de la edad de {edad}, '
                'es de la ciudad de {cuidad} y cursa el anio {anio} '
                'en la Universidad \n')
            linea_formateada = linea.format(
                alumno=llave,
                edad=valor['edad'],
                cuidad=valor['cuidad'],
                anio=valor['anio']
            )

            archivo.write(linea_formateada)
            print '=========', linea_formateada
    archivo.close()


def  estudiantesMasayaprimeranio():
    dic = generar_diccionario_estudiantes()
    x = 1
    for llave, valor in dic.iteritems():
        if 'Masaya' == valor['cuidad'] and x == valor['anio']:
            print 'El alumno {estudiante} de la edad de {ed}, es de la ciudad de {ciudad} y cursa el anio {anio} en la universidad \n'.format(estudiante=llave, ed=valor['edad'], ciudad=valor['cuidad'], anio=valor['anio'])

def estudiantemenode21():
    dic = generar_diccionario_estudiantes()
    
    for llave, valor in dic.iteritems():
        if valor['edad'] < 21:
            print '***EL alumno {estudiante} de la edad de {ed}, es de la ciudad de {ciudad} y cursa el anio {anio} en la Universidad'.format(
                estudiante=llave,
                ed=valor['edad'],
                ciudad=valor['cuidad'],
                anio=valor['anio'] )

if __name__ == '__main__':
    print 'TODOS'
    imprimirestudiante()
    print 'SOLO MANAGUA'
    estudianteManagua()
    print 'SOLO MASAYA DE PRIMER ANIO'
    estudiantesMasayaprimeranio()
    print 'SOLO MENORES DE 21 ANIOS'
    estudiantemenode21()

  
    

 
# - Crear un script que genere el diccionario de estudiantes
#   usando "generar_diccionario_estudiantes"

# - Imprimir todos las llaves del diccionario generado de la forma:
#   "El <nombre_estudiante> de <edad>, es de la ciudad de <ciudad> y
#   cursa <anio> en la universidad

# - Del diccionario de estudiantes creado imprimir los estudiantes
#   de la ciudad de 'Managua' de la forma:
#   "El <nombre_estudiante> de <edad>, es de la ciudad de <ciudad> y cursa <anio> en la universidad"

# - Del diccionario de estudiantes creado imprimir los estudiantes de 'Masaya' que cursen 1er anio de universidad.
#   de la forma:
#   "El <nombre_estudiante> de <edad>, es de la ciudad de <ciudad> y cursa <anio> en la universidad"

# - Del diccioanrio de estudiantes creado imprimir los estudiantes que sean menor de 21 anios
#   de la forma:
#   "El <nombre_estudiante> de <edad>, es de la ciudad de <ciudad> y cursa <anio> en la universidad" 