''' x - y - z | A1 - A2 - A3 | H1 - H2 - H3
    ---------------------------------------
    2 - 1 - 4 | 2  - 4  - 8  | 4  - 2  - 1
    3 - 7 - 2 | 21 - 14 - 6  | 2  - 3  - 7
    1 - 5 - 3 | 5  - 15 - 3  | 3  - 1  - 5
    4 - 3 - 2 | 12 - 6  - 8  | 2  - 4  - 3
    1 - 9 - 7 | 9  - 63 - 7  | 7  - 1  - 9'''


def calculaAreas(volumen_cajas):
    '''Parámetro que acepta una lista de listas, donde
    cada lista incluye tres elementos. Esos elementos son
    las medidas de las cajas alto x ancho x largo'''
    Areas = {}
    '''Diccionario que guardará las posibles combinaciones
    de las areas de las cajas que tiene cada lista de la
    listas que pasan como parámetro'''
    alturas = []
    '''Lista que guardará las alturas para cada combinación
    de las áreas de las cajas que tiene cada diccionario
    de las areas'''
    for i in range(len(volumen_cajas)):
        '''Recorres cada indice hasta el elemento-1 de
        la listas de listas'''
        A1 = volumen_cajas[i][0] * volumen_cajas[i][1]
        A2 = volumen_cajas[i][1] * volumen_cajas[i][2]
        A3 = volumen_cajas[i][2] * volumen_cajas[i][0]
        '''Se consiguen todas las combinaciones de las
        areas con las medidas que tienes en la listas
        de listas'''
        Areas[i] = [A1, A2, A3]
        '''Almacenas en el diccionario una lista con las combinaciones
        de las areas que se calcularon anteriormente. La lista tiene 
        en su indice el area correspondiente a los indices de la lista
        de las medidas de las cajas'''
        alturas.append([volumen_cajas[i][2], volumen_cajas[i][0], volumen_cajas[i][1]])
        '''Almacenas en la lista de alturas una lista con las alturas. La lista tiene 
                en su indice la altura correspondiente a los indices de la lista
                de las areas de las areas en el diccioanrio'''
    return Areas, alturas


'''Retornas el diccionario que tiene las areas [cada diccionario contiene una lista] 
y la matriz que tiene las alturas para cada medida de las cajas existentes'''


def ordenaAreas(Areas, alturas, volumen_cajas):
    '''Ordena de mayor a menor las areas de las cajas, junto
    con su caja y si altura en una lista de listas. cada elemento
    de la lista tiene en su primer indice el area, en su segundo
    indice la caja a la que pertenece y en ultimo lugar la altura.
    Luego de este método, se necesitan ordenar en torres y posteriormente
    conseguir la mejor configuración'''
    numero_elementos = len(volumen_cajas[1]) * len(volumen_cajas)
    orden = []
    '''Lista que almacena listas con el orden de en como se almacena 
    las areas. la lista mas grande será la más eficiente'''
    for o in range(numero_elementos):
        '''Recorre cada elemento de la matriz de medidas original filas x columnas'''
        Caja = 0
        Valor = 0
        altura = 0
        indice = -1
        for j in range(len(volumen_cajas)):
            '''Recorre cada elemento de la lista de la matriz original, como
            es una lista de listas, recorre cada lista como elemento. 
            Lo que hace es buscar el elemento mayor de todas las cajas.
            Indica las cajas - tomamos las columnas'''
            for k in range(len(Areas[j])):
                '''Recorre la longitud de la lista en el diccionario dado
                bajo la llave j. Tomamos el elemento dado en una casilla
                (x,y)'''
                if (Areas[j][k] > Valor):
                    '''Verdifica si en el diccionario,  en la llave de "j",
                     en el primer valor de la lista asociada a esa llave es 
                     mayor a la variable valor declarda e inicializada en cero'''
                    Caja = j + 1
                    '''Si el valor en esa lista asociada en esa llave es mayor al
                    valor, la variable caja cambia su valor al valor de j + 1.
                    esta suma de j+1 es para mapear las cajas en numeros de 1 a n
                    y no de 0 a n'''
                    Valor = Areas[j][k]
                    '''Si el valor en esa lista asociada en esa llave es mayor al
                    valor, la variable valor cambia su valor al de elemento evaludo
                    en el dicionario actualmente evaluado dado por j'''
                    indice = k
                    '''Se guarda el indice donde se encuentra el area de mayor unidad
                    actualmente, para, en una instrucción más adelante, colocar essa
                    areá en el diccionario de areas en un valor de -1'''
                    altura = alturas[j][k]
                    '''Si el valor en esa lista asociada en esa llave es mayor al
                    valor, la variable altura cambia su valor al de la altura que 
                    esta en la matriz de alturas, mapeado en el mismo indice
                    que el area actualmente evaluada'''
        orden.append([Valor, Caja, altura])
        '''Agrega a la lista de orden el valor, la caja y la altura como elemento'''
        Areas[Caja - 1][indice] = -1
        '''Cambia el valor del área actual a -1, del diccionario Areas, el valor actual
        con el valor de la variable caja, solo que el valor de caja es una unidad mayor 
        al indexado de llaves del diccionario de las areas, por eso se resta. Sabemos que
        area se cambia a -1 pues con el valor de caja-1 encontramos el diccionario(caja)
        donde esta el área actualmente y la variable indice indice guarda el indice exacto 
        del área actual en la caja dada por caja-1'''
    return orden
'''Retorna una lista de listas. Cada elemento es una lista y siempre sera de tres elementos
    
    -En el elemento cero sera el area calculada de ciertas cajas
    -En el elemento uno sera la caja a la cual pertenece esa area
    -En el elemento dos sera la altura que le corresponde a esa area
    
    Los elementos estan guardados de su area mayor a su area menor'''


def creacion_torres(matriz, orden):
    '''Función que se encarga de crear las torres correspondientes, el numero
    de torres será igual al numero de elementos de la lista de orden. Cada torre
    adminte 0 o 1 elemento de la misma caja.'''
    torres = []
    '''Lista de diccionarios. cada diccionario es una torre. cada diccionario
    tiene una key asociado a:
    1-. las areas que guarda la configuración de areas en esa caja
    2-. las cajas que tendra una lista de las cajas, donde si un elemento es cero, 
    entonces no hay elementos  de esa caja, si hay un elemento de 1 a n en algun 
    indice entondes hay un elemento de esa caja
    3-. Las alturas, que llevara la suma de las areas en esa torre
    '''
    num_torre = 1
    '''Variable que lleva el conteo del número de torres creadas, inciada en uno
    pues se creara desde el incio al menos una torre'''
    item = 0
    '''Variable para acceder unicamente primer elemento de la lista de orden'''
    area = 0
    '''Variable para acceder unicamente al primer elemento o area de algun elemento
    de la lista orden. Cada elemento de la lista orden es una lista y en su primer 
    indice de ese elemento siempre guarda el area'''
    caja = 1
    '''Variable para acceder unicamente al segundo elemento o caja de algun elemento
    de la lista orden. Cada elemento de la lista orden es una lista y en su segundo 
    indice de ese elemento siempre guarda la caja'''
    altura = 2
    '''Variable para acceder unicamente al tercer elemento o altura de algun elemento
    de la lista orden. Cada elemento de la lista orden es una lista y en su segundo 
    indice de ese elemento siempre guarda la altura'''

    while len(orden) != 0:
        '''Ciclo que termina hasta que la longitud de la lista orden sea cero'''
        torres.append({'area' + str(num_torre): [],
                       'caja' + str(num_torre): [0] * len(matriz),
                       'altura' + str(num_torre): 0})
        '''Crea una torre (diccionario)en la lista de diccionarios. cada diccionario
        tiene una key asociado a:
        1-. las areas que guarda la configuración de areas en esa caja
        2-. las cajas que tendra una lista de las cajas, donde si un elemento es cero, 
        entonces no hay elementos  de esa caja, si hay un elemento de 1 a n en algun 
        indice entondes hay un elemento de esa caja
        3-. Las alturas, que llevara la suma de las areas en esa torre
        
        las key area, caja y altura siempre eran las mismas, pero diferiran por el numero
        de torre en un momento dado, por lo que area5 hace referencia a la torre 5
        
        Desde que se crea la torre por la instruccion anterior, inmediatamente se ingresa en 
        esa torre creada actualemente el elemento de indice 0 de la lista orden. Sabemos cual
        es la torre actual por la variable num_torre'''
        torres[num_torre - 1]['area' + str(num_torre)].append(orden[item][area])
        '''En la torre creada actualemnte, en la key area de la torre creada actualmente
        se agrega a su lista el area del elemento en el indice cero de la lista orden.
        Sabemos cual es el area por que los elementos de la lista orden guaran listas y
        siempre guardan en el indice cero el area. el indice cero esta dado por la variable
        area'''
        torres[num_torre - 1]['caja' + str(num_torre)][orden[item][caja] - 1] = orden[item][caja]
        '''En la torre creada actualemnte, en la key caja de la torre creada actualmente
        se cambia en la lista asociada a la key, en su indice correspondiente, de 0 al
        numero de la caja a la que corresponde el elemento actual, el numero actual de
        la caja esta dado por el elemento de la lista orden en su indice uno. 
        
        Sabemos cual es la caja  por que los elementos de la lista orden guaran listas y 
        siempre guardan en el indice uno la caja. el indice uno esta dado por la variable caja. 
        
        Solo que como la variable  caja esta una unidad aumentada, le restamos uno para acceder 
        al incdice correcto en la lista asociada a la key caja'''
        torres[num_torre - 1]['altura' + str(num_torre)] += orden[item][altura]
        '''En la torre creada actualemnte, en la key altura de la torre creada actualmente
        se suma a su valor asociado a la key altura, la altura del elemento actual.
        Sabemos cual es la altura por que los elementos de la lista orden guaran listas y
        siempre guardan en el indice dos la altura. el indice dos esta dado por la variable
        altura'''

        for torre_actual in range(len(torres)):
            '''Realizamos un for para verificar cada torre(diccionario) de la lista
            de diccionarios torres. Verifica si es posible ingresar en esa torre dada,
            un elemento con un numero de caja'''
            if torres[torre_actual]['caja' + str(torre_actual + 1)][orden[item][caja] - 1] == 0:
                '''si en la torre actual, en la key caja, verificamos si en su lista asociada
                en su indice buscado es igual a cero. si es igual a cero significa que no existe
                un elemento de esa caja en esa torre.
                
                Sabemos cual es la caja a verificar por que la variable torre_actual lleva el numero
                de torre que se esta verificando, como inicia de 0 a n-1 aumentamos una unidad para
                encontrar la key de la caja.
                
                Sabemos cual es el indice a verificar en la lista asociada a la key caja por que obtenemos
                el indice de n elemento de la lista orden. en su segundo indice guarda la caja y obtenemos
                ese valor por va variable caja. Debe ser restado la unidad pues esta aumentado en uno con
                respecto al indexado de ls lista asociada a la key caja.'''
                torres[torre_actual]['area' + str(torre_actual + 1)].append(orden[item][area])
                '''En la torre evaluada actualmente por el for, en la key area de la torre evaluada 
                actualmente se agrega a su lista el area del elemento en el indice cero de la lista 
                orden. Sabemos cual es el area por que los elementos de la lista orden guaran listas 
                y siempre guardan en el indice cero el area. el indice cero esta dado por la variable
                area'''
                torres[torre_actual]['caja' + str(torre_actual + 1)][orden[item][caja] - 1] = orden[item][caja]
                '''En la torre evaluada actualemnte por el for, en la key caja de la torre evaluada 
                actualmente se cambia en la lista asociada a la key, en su indice correspondiente, 
                de 0 al numero de la caja a la que corresponde el elemento actual, el numero actual 
                de la caja esta dado por el elemento de la lista orden en su indice uno. 

                Sabemos cual es la caja  por que los elementos de la lista orden guaran listas y 
                siempre guardan en el indice uno la caja. el indice uno esta dado por la variable caja. 

                Solo que como la variable  caja esta una unidad aumentada, le restamos uno para acceder 
                al incdice correcto en la lista asociada a la key caja'''
                torres[torre_actual]['altura' + str(torre_actual + 1)] += orden[item][altura]
                '''En la torre evaludad actualemnte por el fro, en la key altura de la torre evaluada 
                actualmente se suma a su valor asociado a la key altura, la altura del elemento actual.
                Sabemos cual es la altura por que los elementos de la lista orden guaran listas y
                siempre guardan en el indice dos la altura. el indice dos esta dado por la variable
                altura'''
        orden.remove(orden[item])
        '''Luego de terminar el ciclo que evalua todo la lista de diccionario, no sercioramos que el
        elemento en su indice cero se ingreso a todas las torres posbiles, por lo que eliminamos el
        elemento en el indice cero. El indice cero esta dado por la varible item'''
        num_torre += 1
        '''Aumentamos en una unidad el numero de torres, esto es, por si vuelve a ingresar en el ciclo
        while, crear otra torre al final de los diccionarios'''
    return torres
'''Retorna la lista de diccionario. cada diccionario es una torre y cada torre almacena la maxima
    configuración posible de areas'''


def mejor_torre(torres):
    '''Ciclo que va a retornar la mejor torre dada su altura y configuración de areas'''
    mejor_torre = -1
    '''Variable que almacenara el indice de la mejor torre'''
    mejor_altura = -1
    '''Variable que almacenara el valor de la mejor altura de una torre'''

    for i in range(len(torres)):
        '''For que recorre cada diccionario(torre) de la lista 
        de diciconario torres'''
        if torres[i]['altura' + str(i + 1)] > mejor_altura:
            '''Si altura de de la torre actual es mayor al valor de la
            variable mejor_altura entonces vamos a guardar en la variable
            mejor_altura la altura de la torre actualmente evaluada y en
            la variable mejor_torre el indice para encontrar la mejor torre de
            la lista de diccionario.
            
            Sabemos cual es la torre actual por la variable i, recorrera el
            indexado de la lista de diccionarios
            
            Como la variable i esta desfasada con el numero de cajas, para
            encontrar la key de altura se concatena aumentando en uno y para
            que sea un string se castea a string esa suma'''
            mejor_altura = torres[i]['altura' + str(i + 1)]
            '''Se alamcena en la variable mejor_altura, el valor de la altura
            actual.'''
            mejor_torre = i
            '''Se almacena en la variable mejor_torre el indice de la mejor 
            torre(diccionario) encontrado en la lista de diccionarios. ese
            indice es la variable i.'''
        elif torres[i]['altura' + str(i + 1)] == mejor_altura:
            '''Si altura de de la torre actual es igual al valor de la
            variable mejor_altura entonces vamos a verificar la longitud
            de la lista de areas actual con la lista de areas de la torre
            que tiene mejor_altura.

            Sabemos cual es la torre actual por la variable i, recorrera el
            indexado de la lista de diccionarios

            Como la variable i esta desfasada con el numero de cajas, para
            encontrar la key de altura se concatena aumentando en uno y para
            que sea un string se castea a string esa suma'''
            longitud_torre_actual = len(torres[i]['area' + str(i + 1)])
            '''Guardamos la altura de la torre anterior. La longitud de la 
            torre actual esta dada por la torre actual, con
            el valor de la altura asociada a su key area. 
            
            Sabemos cual es la torre actual por la variable i, recorrera el
            indexado de la lista de diccionarios

            Como la variable i esta desfasada con el numero de cajas, para
            encontrar la key de altura se concatena aumentando en uno y para
            que sea un string se castea a string esa suma'''
            longitud_torre_anterior = len(torres[int(mejor_torre)]['area' + str(mejor_torre)])
            '''Guardamos la altura de la torre anterior. La longitud de la torre 
            anterior esta dada por la variable, con el valor de la altura asociada 
            a su key area. 

            Sabemos cual es la torre anterior por que la variable mejor_torre 
            guarda el indice de la mejor torre por lo tanto tiene el indice de 
            la torre anterior.

            Como la variable mejor_torre esta a la con el numero de cajas, para
            encontrar la key de altura se usa el valor de la variable mejor_torre'''
            if longitud_torre_actual >= longitud_torre_anterior:
                '''Si la longitud de la altura de la torre actual es mayor o igual
                a la longitud la altura de la torre anterior. Significa que la torre
                actual es mas eficiente, por lo que guardarimos su altura y su indice
                para devolver la torre.
                
                De lo contrario, habria dos torres con el la misma eficiencia y por 
                facilidad nos quedariamos con la torre anterior'''
                mejor_altura = torres[i]['altura' + str(i + 1)]
                '''Se alamcena en la variable mejor_altura, el valor de la altura
                actual.
                
                Sabemos cual es la torre actual por la variable i, recorrera el
                indexado de la lista de diccionarios
            
                Como la variable i esta desfasada con el numero de cajas, para
                encontrar la key de altura se concatena aumentando en uno y para
                que sea un string se castea a string esa suma'''
                mejor_torre = i
                '''Se almacena en la variable mejor_torre el indice de la mejor 
                torre(diccionario) encontrado en la lista de diccionarios. ese
                indice es la variable i.'''
    return torres[mejor_torre]
'''Una vez que la lista orden se quedo vacia, significa que todos las areas y sus
    caracteristicas entraron en la lista de diccionarios. Ahora solo queda devolver la
    mejor torre. Esto se logra gracias a la variable mejor_torre que guardo a lo largo
    del programa el indice del mejor diccionario'''


def problema_de_las_cajas(matriz):
    '''Función que se encarga de llamar a todas las funciones secundarias para
    encontrar la mejor altura dado el calculo de areas de n cajas'''
    areas, alturas = calculaAreas(matriz)
    '''La variable areas almacena un diccionario con las areas. Las key de ese
    diccionario es el numero de cajas.
    
    La variable alturas guarda una lista de listas con las alturas de cada area'''
    orden = ordenaAreas(areas, alturas, matriz)
    '''La variable orden guarda una lista de listas, donde cada elemento es una lista.
    
    -En el elemento cero sera el area calculada de ciertas cajas
    -En el elemento uno sera la caja a la cual pertenece esa area
    -En el elemento dos sera la altura que le corresponde a esa area
    
    Los elementos estan guardados de su area mayor a su area menor
    '''
    torres = creacion_torres(matriz, orden)
    '''Retorna la lista de diccionario. cada diccionario es una torre y cada torre almacena la maxima
    configuración posible de areas. Cada diccionario almacena:
    
     - una key area"n" que tendra una lista con la configuración de areas ene sa torre
     - una key caja"n" que tendra una lista con el valor del numero de cajas de los 
     elementos que contiene la torre
     - una key altura"n" que tendra la sumatoria de las alturas asociadas a las areas'''

    mejor = mejor_torre(torres)
    '''Guardará la mejor torre, con la mejor configuración de areas, el mayor numero de areas
    y la altura más alta de todas las torres'''
    return mejor
    '''Retornará la mejor torre'''


def main():
    matriz = [[2, 1, 4],
              [3, 7, 2],
              [1, 5, 3],
              [4, 3, 2],
              [1, 9, 7]]
    torre = problema_de_las_cajas(matriz)
    print(f'Mejor Torre: {torre}')
main()
