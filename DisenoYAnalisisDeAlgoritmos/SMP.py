def fase1(solteros, rankingsN, rankingsK):
    '''Funcion encargado de realizar el mejor match en su
    primera opcion (de ser posible) para cada pareja

    solteros: Lista que tendra, en String, los Hombres
    solteros

    rankingN: Lista que tendrda listas, casa lista es
    un ranking para cada Hombre

    rankingK: Lista que tendrda listas, casa lista es
    un ranking para cada Mujer
    '''

    parejas = {}
    '''Diccionario que guarda las parejas'''
    aux_solteros=solteros.copy()
    '''Copia la lista de solteros para no modificar
    la lista de solteros original'''
    aux_rankingsN = rankingsN.copy()
    '''Copia los rankings de los Hombres'''
    mujeres_unidas = list(map(lambda i: 0, aux_solteros))
    '''Transforma la lista de aux_solteros, en una lista de ceros y
    lo almacena en la lista llamada mujeres_unidas, ya que almacena
    las mujeres que se comprometieron en un momento dado'''
    hombres_unidos = list(map(lambda i: 0, aux_solteros))
    '''Transforma la lista de aux_solteros, en una lista de ceros y
        lo almacena en la lista llamada hombres, ya que almacena
        los hombres que se comprometieron en un momento dado'''

    for i in range(len(aux_solteros)):
        '''Recorre la lista de solteros'''
        pareja_hombre = int(rankingsN[i][0].replace("K", ""))-1
        '''Busca el primer match de cada Hombre en la lista de ranking
        de los hombres y elimina el caracter de K. Esto para conseguir 
        el número de la mujer según su primera opción. Conviertes ese
        número a entero y restas -1 ya que se utiliza la variable 
        pareja para acceder al indice en el ranking de los mujeres y
        conseguir la Mujer para el hombre evaluado actualmente'''
        if(rankingsK[pareja_hombre][0] == aux_solteros[i]):
            pareja_mujer = int(aux_solteros[i].replace("N", ""))-1
            '''Buscamos la Mujer evaluado según el Hombre evaluado
            actualmente y verificamos si, al igual que en el Hombre,
            para la Mujer tambien es su primera opción el hombre evaluado'''
            parejas['K'+str(pareja_hombre+1)] = 'N'+str(pareja_mujer+1)
            '''Si lo es, agregamos una key al diccionario de parejas, esa
            key tendra el numero de la Mujer que es la mejor opción para
            el Hombre que se esta evaluando y su valor asociado sera el
            número del Hombre evaluado'''
            mujeres_unidas[pareja_hombre] = 'K'+str(pareja_hombre+1)
            '''En la lista mujeres_unidas, bajo el indice n asociado al N(n)
            , almacena a la mujer que se asocio a ese hombre N(n)'''
            hombres_unidos[pareja_mujer] = 'N'+str(pareja_mujer+1)
            '''En la lista hombres_unidoss, bajo el indice n asociado al K(n)
            , almacena al hombre que se asocio a esa mujer K(n)'''
    return parejas,solteros, aux_rankingsN, rankingsK, mujeres_unidas, hombres_unidos

def fases(parejas, solteros, rankingsN, rankingsK, mujeres_unidas, hombres_unidos):
    aux_solteros = solteros.copy()
    '''Copia la lista de solteros para no modificar
    la lista de solteros original'''
    proposicion = 1
    '''Variable que permite acceder a los ranking, apartir
    del inidice 1, en los rankings de la mujer. esto pues la
    en este método empieza a emparejar apartir del sujeto en
    el lugar número dos del ranking. El ranking en cada iteración
    un índice mayor'''
    contador = 0
    '''Variable que permite recorrer todos los elementos del ranking
    de los hombres'''
    while contador < len(rankingsN) * (len(rankingsN[0]) - 1):
        '''Variable que permite recorrer todos los elementos del ranking
            de los hombres a partir del lugar 1 en el ranking, por ello
            la resta pues se esta omitiendo la primera fila'''
        for i in range(len(aux_solteros)):
            '''Recorre cada indice de la lista aux_solteros'''
            if aux_solteros[i] in hombres_unidos:
                '''Si con el indice, obtenemos un elemnto de la
                lista aux_solteros y ese elemento esta en la lista
                hombres_unidos, significa que ese hombre ya esta 
                comprometido temporalmente, por lo que iteramos para
                obtener el siguiente soltero'''
                continue
            else:
                '''Si con el indice, obtenemos un elemnto de la
                lista aux_solteros y ese elemento NO esta en la lista
                hombres_unidos, significa que debe comprometerse'''
                hombre = int(aux_solteros[i].replace("N", "")) - 1
                '''Obtenemos el índice del hombre actual con el índice
                del for, remplazamos "N" por un espacio vacio para obtener
                ese hombre de la lista de solteros'''
                mujer = int(rankingsN[hombre][proposicion].replace("K", "")) - 1
                '''Con el índice del hombre, obtenemos del ranking de los hombres,
                primero ubicando al hombre correspondiente con la variable "hombre"
                y con la varible proposición obtenemos la el indice de la mujer de ese
                hombre. Proposición inica en 1 pues el ranking en esta función inicia
                a evaluar a partir de indice 1'''
                if 'K'+str(mujer + 1) not in mujeres_unidas:
                    '''al indice que se obtuvo de la mujer en el ranking del hombre
                    que se esta evaluando actualmete, le sumamos la unidad y la concatemos
                     la letra K para saber si esa mujer NO se encuentra en la lista mujeres
                     unidas. Si esa mujer actualmente evaluada NO se encuentra en la lista
                     de mujeres_unidas (quiere decir que no esta comprometida actualmente),
                     ingresa al código del if para comprometerla con el hombre actualmente
                     evaluada'''
                    parejas['K'+str(mujer + 1)] = 'N'+str(hombre + 1)
                    '''En el diccionario parejas, con la mujer actual (que es la llave),
                    asociamos al hombre actualmete evaluado'''
                    mujeres_unidas[mujer] = 'K'+str(mujer + 1)
                    '''En la lista de mujeres_unidas, con la variable mujer que tiene 
                    el indice de la mujer actualmente evaluda. colocamos a la mujer
                    actualmente evaluada'''
                    hombres_unidos[hombre] = 'N'+str(hombre + 1)
                    '''En la lista de hombres_unidos, con la variable hombre que tiene 
                    el indice del hombre actualmente evaludo. colocamos al hombre
                    actualmente evaluado'''
                elif 'K'+str(mujer + 1) in mujeres_unidas:
                    '''al indice que se obtuvo de la mujer en el ranking del hombre
                    que se esta evaluando actualmete, le sumamos la unidad y la concatemos
                    la letra K para saber si esa mujer se encuentra en la lista mujeres_unidas.
                    Si esa mujer actualmente evaluada Se encuentra en la lista
                    de mujeres_unidas (quiere decir que esta comprometida actualmente),
                    ingresa al código del elif, para verificar si tiene comprometida a su
                    mejor opción'''
                    hombre_opcion_uno = parejas['K'+str(mujer + 1)]
                    '''Obtenemos el hombre (indice) que esta compromedito actualmente con
                    la mujer evaluada actualmente a partir del diccionario parejas'''
                    hombre_opcion_dos = 'N'+str(hombre + 1)
                    '''Almacenamos al hombre (indice) actualmente evaluado'''
                    opcionUno = 0
                    '''Variable para almacenar el valor del indice en el
                    ranking del para la opción uno'''
                    opcionDos = 0
                    '''Variable para almacenar el valor del indice en el
                    ranking del hombre para la opción dos'''
                    for ranking in range(len(rankingsK[mujer])):
                        '''recorremos el ranking de la mujer actualmete
                        evaluada, gracias a la variable mujer. La variabke
                        ranking alamcena el indice que va recorriendo en
                        la lista del ranking bajo la variable ranking'''
                        if rankingsK[mujer][ranking] == hombre_opcion_uno:
                            '''si el indice actualmente evaluado es igual al
                             indice de la variable hombre_opcion_uno, almacenamos
                             en la variable opcionUno, el indice actualmente evaluado'''
                            opcionUno = ranking
                        elif rankingsK[mujer][ranking] == hombre_opcion_dos:
                            '''si el indice actualmente evaluado es igual al
                            indice de la variable hombre_opcion_dos, almacenamos
                            en la variable opcionDos, el indice actualmente evaluado'''
                            opcionDos = ranking
                    if opcionDos < opcionUno:
                        '''Si el indice de la variable opcionDos es menor al indice
                        de la variable opcionUno, comprometemos con el hombre actualmente
                        evaluado a la mujer actuaomente evaluada y rompemos su anterior
                        pareja. Esto e spor que el indice de menor valor esta antes en una
                        lista y si opcionUno guarda el indice del hombre con el que estaba
                        comprometido la mujer actual, forzosamente opcionDos debe ser menor'''
                        parejas['K'+str(mujer + 1)] = hombre_opcion_dos
                        '''En el diccionario parejas, con la mujer actual (que es la llave), 
                        le cambiamos su valor por el hombre de la opción dos pues es la mejor
                        opción de la mujer actual'''
                        hombres_unidos[int(hombre_opcion_uno.replace("N", "")) - 1] = 0
                        '''de la lista hombres_unidos, con el indice que se obtiene de hombre_opcion_uno,
                        cambiamos el valor del hombre en ese indice por cero'''
                        hombres_unidos[int(hombre_opcion_dos.replace("N", "")) - 1] = hombre_opcion_dos
                        '''de la lista hombres_unidos, con el indice que se obtiene de hombre_opcion_dos,
                        cambiamos el valor de cero por el hombre almacenado en la variable
                        hombre_opcion_dos'''
        proposicion += 1
        '''Aumentamos en uno la variable proposición para continuar con la siguiente evaluación en el ranking
        de los hombres'''
        contador += 1
        '''Aumentamos en uno la variable contador para continuar recorriendo toda la metriz
        de rankigs de los hombres'''
    return parejas
    '''Retornamos el diccionario de parejas que tendra la mejor configuración de las parejas'''

def emparejamiento_estable(solteros, rankingsN, rankingsK):
    '''Método para llamar las fases y emparejar con la mejor configuracón dos
    conjuntos de hombres y mujeres. necesita una lista de los hombres solteros,
    una lista de rankings de hombres y una lista de rankings de mujeres'''
    parejas, solteros, aux_rankingsN, aux_rankingsK, mujeres_unidas, hombres_unidos = fase1(solteros, rankingsN,
    rankingsK)
    '''Llama al método fase1() para completar la primera fase de emparejamiento'''
    resultado = f'Mejor configuracion: ' \
                f'{fases(parejas, solteros, aux_rankingsN, aux_rankingsK, mujeres_unidas,hombres_unidos)}'
    '''Llama al método fases() que completa el emparejamiento con las mejores parejas posibles,
    almacena un dicicionario con dicha configuración'''
    return resultado
    '''Retorna la mejor configuración de un emparejamoento de parejas'''


def main():
    N = ["N1", "N2", "N3", "N4", "N5"]
    '''Conjunto de Hombres'''
    K = ["K1", "K2", "K3", "K4", "K5"]
    '''Conjunto de Mujeres'''

    N1 = ["K3", "K2", "K5", "K1", "K4"]
    N2 = ["K2", "K1", "K3", "K5", "K4"]
    N3 = ["K4", "K2", "K1", "K3", "K5"]
    N4 = ["K5", "K3", "K2", "K4", "K1"]
    N5 = ["K3", "K2", "K1", "K4", "K5"]
    '''Conjunto de ranking de los Hombres'''

    K1 = ["N2", "N5", "N4", "N1", "N3"]
    K2 = ["N1", "N3", "N5", "N2", "N4"]
    K3 = ["N1", "N4", "N5", "N3", "N2"]
    K4 = ["N4", "N3", "N5", "N1", "N2"]
    K5 = ["N3", "N1", "N5", "N2", "N4"]
    '''Conjunto de ranking de los Mujeres'''

    solteros = ["N1", "N2", "N3", "N4", "N5"]

    rankingsN = [N1, N2, N3, N4, N5]
    '''Matriz con el ranking de N. Donde cada
    columna es una "persona" y su celda el ranking"'''
    rankingsK = [K1, K2, K3, K4, K5]
    '''Matriz con el ranking de K. Donde cada
    columna es una "persona" y su celda el ranking"'''

    print(emparejamiento_estable(solteros, rankingsN, rankingsK))

main()