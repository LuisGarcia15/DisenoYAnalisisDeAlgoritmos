import numpy as np
def subcadena_mas_larga(filas, columnas):
    coordenada_elemento_mayor= []
    '''Lista para guardar las coordenadas de la celda de mayor numero de
    caracteres similares'''
    valor_mas_grande = 0
    '''Variable para almacenar el numero mayor de caracteres similares'''
    subcadena_mayor = ''
    '''Variable para almacenar la subcadena de caracteres similares'''
    bandera = True
    '''Bandera para almacenar una sola vez el número uno en la variable
    valor_mas_grande'''
    table = np.array([[0]*(len(columnas))]*(len(filas)))#primero van filas luego columnas

    for fila in range(1,len(filas)):
        for columna in range(1, len(columnas)):
            '''Ciclos que permite comparar caracter por caratcer dado su indice
            entre cadenas'''
            if filas[fila] == columnas[columna]:
                '''Verifica si los caracteres entre cadenas son iguales'''
                if table[fila-1][columna-1] != 0:#A
                    '''Verifica si la celda anterior en diagonal es diferente de cero'''
                    table[fila][columna] = (table[fila-1][columna-1] + 1)
                    '''Actualiza la celda actual en el numero de la celda anterior en
                    diagonal mas una unidad'''
                    if table[fila][columna]  >= valor_mas_grande:
                        '''Si el valor actual en la celda actual es mayor o igual al 
                        valor de numeros caracteres repetidos en la variable 
                        valor_mas_grande'''
                        valor_mas_grande = table[fila][columna]
                        '''Actualiza la variable valor_mas_grande al mayor numero de
                        caracteres repetidos que se encuentran en las cadenas'''
                        coordenada_elemento_mayor.remove(coordenada_elemento_mayor[0])
                        '''Remueve las coordenadas del ultimo elemento mayor más grande'''
                        coordenada_elemento_mayor.remove(coordenada_elemento_mayor[0])

                        coordenada_elemento_mayor = [fila, columna]
                        '''Actualiza las coordenadas de la celda de mayor numero de
                        caracteres repetidos en las cadenas'''
                else:
                    '''Si la celda actual es cero y los caracteres a comparar actualmente son
                    iguales'''
                    table[fila][columna] = 1
                    '''La celda actual se actualiza a un numero uno'''
                    if table[fila][columna] == 1 and bandera:
                        '''Si la tabla actual es un numero uno y la variable booleana es True.
                        Que sea True significa que solo puede almacenar en la variable
                        valor_mas_grande un uno una sola vez y solo puede almacenar una vez
                        una coordenada cuyo valor sea uno una vez'''
                        valor_mas_grande = table[fila][columna]
                        '''Alamcena el valor uno en la variable'''
                        coordenada_elemento_mayor = [fila, columna]
                        '''Almacena la coordenada de valor uno'''
                        bandera = False
                        '''Cambia a False la variable booleana para no
                        verificar varias veces un uno y almacenarlo varias veces'''

    '''Como tenemos en este momento almacenado la coordenada de la celda de mayor numero de
    caracteres repeditos, en una varriable restamos a la coordenada de las filas donde ese
    numero representa el indice hasta donde se repiten los caracteres en una cadena (la variable
    filas es una de las cadenas) restamos el valor_mas_grande de caracteres que existen en las 
    dos cadenas y aumentamos uno para coincidir con los indices correctos y asi obtener el indice
    de inicio donde se empiezan a repetir los caracteres'''
    x = (coordenada_elemento_mayor[0]-valor_mas_grande)+1
    '''Como tenemos en este momento almacenado la coordenada de la celda de mayor numero de
        caracteres repeditos, en una varriable obtenemos la coordenada de las filas, donde ese
        numero representa el indice de inicio donde se repiten los caracteres en una cadena(la variable
        filas es una de las cadenas) y aumentamos uno para coincidir con los indices correctos'''
    y = (coordenada_elemento_mayor[0])+1

    for item in range(x,y):
        '''Realizamos un for entre el rango de las variables anteriormente descrita
        para obtener los indices donde se encuentran las subcadenas más largas en una
        de las cadenas pasadas como parámetro'''
        subcadena_mayor += filas[item]
        '''Concatenamos en la variable subcadena_mayor el caracter dado su indice de la
        variable filas(filas es una de las cadenas pasadas como parámetro)'''
    return subcadena_mayor
    '''Retornamos la subcadena'''


def main():
    cadena_uno = 'asdfrhj'
    cadena_dos = 'qwefrtyu'
    print(subcadena_mas_larga(cadena_dos, cadena_uno))
    print(subcadena_mas_larga(cadena_uno, cadena_dos))

main()