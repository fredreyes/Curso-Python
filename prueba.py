#dado el texto 'esto es una prueba' imprimir una cadena formateada de la siguente manera
#argumento <nombre>
#'esto es una prueba' <nombre>
#imprimir cuantas letras e tiene la cadena
#.capitalizar cadena
#.imprimirlongitud de cadena
#.reemplezar en la cadema de la letra o por 0

texto = 'esto es una prueba'
saludo = "HoLA!"

if __name__=='__main__':
    print(texto)
    print(str.count(texto,'e'))
    #print(texto.count('e'))
    print(str.capitalize(texto))
    print(len(texto))
    print(str.replace(texto,'o','0'))