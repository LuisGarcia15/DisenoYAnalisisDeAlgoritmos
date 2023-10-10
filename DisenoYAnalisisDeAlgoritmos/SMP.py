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
    ''''''
    mujeres_unidas = list(map(lambda i: 0, aux_solteros))
    hombres_unidos = list(map(lambda i: 0, aux_solteros))
    num_solteros = 0

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
            #solteros.remove(solteros[i])
            '''Eliminamos el Hombre evaluado de la lista de solteros, pues
            ya no estaría soltero'''
            mujeres_unidas[pareja_hombre] = 'K'+str(pareja_hombre+1)
            hombres_unidos[pareja_mujer] = 'N'+str(pareja_mujer+1)
            num_solteros += 1
            #aux_rankingsN.remove(aux_rankingsN[i])
    return parejas,solteros, aux_rankingsN, rankingsK, mujeres_unidas, hombres_unidos

def fases(parejas, solteros, rankingsN, rankingsK, mujeres_unidas, hombres_unidos):
    aux_solteros = solteros.copy()
    proposicion = 1
    contador = 0
    while contador < len(rankingsN) * (len(rankingsN[0]) - 1):
        for i in range(len(aux_solteros)):
            if aux_solteros[i] in hombres_unidos:
                continue
            else:
                hombre = int(aux_solteros[i].replace("N", "")) - 1
                mujer = int(rankingsN[hombre][proposicion].replace("K", "")) - 1
                if 'K'+str(mujer + 1) not in mujeres_unidas:
                    parejas['K'+str(mujer + 1)] = 'N'+str(hombre + 1)
                    mujeres_unidas[mujer] = 'K'+str(mujer + 1)
                    hombres_unidos[hombre] = 'N'+str(hombre + 1)
                elif 'K'+str(mujer + 1) in mujeres_unidas:
                    hombre_opcion_uno = parejas['K'+str(mujer + 1)]
                    hombre_opcion_dos = 'N'+str(hombre + 1)
                    opcionUno = 0
                    opcionDos = 0
                    for ranking in range(len(rankingsK[mujer])):
                        if rankingsK[mujer][ranking] == hombre_opcion_uno:
                            opcionUno = ranking
                        elif rankingsK[mujer][ranking] == hombre_opcion_dos:
                            opcionDos = ranking
                    if opcionDos < opcionUno:
                        parejas['K'+str(mujer + 1)] = hombre_opcion_dos
                        hombres_unidos[int(hombre_opcion_uno.replace("N", "")) - 1] = 0
                        hombres_unidos[int(hombre_opcion_dos.replace("N", "")) - 1] = hombre_opcion_dos
            #if i == len(aux_solteros) - 1:
        proposicion += 1
        contador += 1
    return parejas

def emparejamiento_estable(solteros, rankingsN, rankingsK):
    parejas, solteros, aux_rankingsN, aux_rankingsK, mujeres_unidas, hombres_unidos = fase1(solteros, rankingsN,
                                                                                            rankingsK)
    resultado = f'Mejor configuracion: ' \
                f'{fases(parejas, solteros, aux_rankingsN, aux_rankingsK, mujeres_unidas,hombres_unidos)}'

    return resultado


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

    '''parejas, solteros, aux_rankingsN, aux_rankingsK, mujeres_unidas, hombres_unidos = fase1(solteros, rankingsN, rankingsK)
    print(f'Parejas: {parejas}, Solteros: {solteros}\nrankingsN: {aux_rankingsN},\nrankingsK: {aux_rankingsK}'
          f',\n mujeres_unidas: {mujeres_unidas}, \n hombres_unidos: {hombres_unidos}')
    fin = fases(parejas, solteros, aux_rankingsN, aux_rankingsK, mujeres_unidas, hombres_unidos)
    print(fin)'''

    print(emparejamiento_estable(solteros, rankingsN, rankingsK))

main()