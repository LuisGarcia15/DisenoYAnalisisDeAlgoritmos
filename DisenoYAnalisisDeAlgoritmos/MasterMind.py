import random

def mastermind():
    print('+'*10 + '| MASTERMIND |' + '+'*10)
    numero_pc = str(random.randrange(1000,9999,1))
    '''Obtiene un número de 4 dígitos'''
    lista_num_correcto = []
    '''Lista que almacena el indice de los números
    que se colocan en un lugar correcto'''
    lista_pos_incorrecta = []
    '''Lista que almacena los indices de los números
    que están en el número aleatorio, pero en una
    posición incorrecta'''
    num_correctos = 0
    '''Variable para llevar la cuenta de cuantos
    números en la posición correcta se colocaron'''
    poscision_incorrecta = 0
    '''Variable para llevar la cuenta de cuantos
    números son correctos, pero no están en la
    posición correcta'''
    intentos = 8
    '''Variable que lleva la cuenta de cuantos
    intentos quedan'''
    bandera = True
    '''Bandera para ciclar o no el ciclo
    principal'''
    while intentos >= 0 or bandera:
        '''Cicla while mientras aún se tenga intentos
        o si la bandera es True'''
        print('#' * 60)
        print(f'Número aleatorio: {numero_pc}')
        '''Imprime el número aleatorio simplemente para
        probar el algoritmo, pues no es necesario'''
        numero_persona = input('Introduce un número de 4 cífras: ')
        '''Obtiene el número del usuario'''
        if len(numero_persona) != 4:
            '''Si la longitud del número que ingreo la persona,
            entonces informa acerca de que el número es equivocado'''
            intentos -= 1
            '''Resta un intento'''
            print('X' * 60)
            print(f'Número equivocado: {numero_persona}')
            print(f'Cantidad de números correctos: {num_correctos}')
            print(f'Cantidad de poscisiones incorrectas: {poscision_incorrecta}')
            print(f'QUEDAN {intentos} INTENTOS')
            print('X' * 60)
            lista_num_correcto.clear()
            lista_pos_incorrecta.clear()
            '''Limpia las variables de las listas que lleva el conteo de indices
            para números correctos y posiciones correctas, además de colocar
            en cero las variables que llevan el conteo de números correctos
            y posciciones correctas pues para evaluar el siguien número que
            ingresa el usario, las variables deben estar sin datos'''
            num_correctos = 0
            poscision_incorrecta = 0
            '''Continua a otro ciclo de while'''
            continue
        for caracter in range(len(numero_pc)):
            '''For para ciclar cada numero del número que ingreo
            el usuairo en su posición con el otro indice del
            número aleaotorio, esto significa que va comparar los
            números en los indices 0 - 0, 1- 1, 2 - 2, 3 - 3'''
            if numero_persona[caracter] == numero_pc[caracter]:
                '''Si los números en el indice actual del número 
                ingresado por el usuario es igual el número en el
                indice actual del número aleatorio'''
                num_correctos += 1
                '''Aumentamos el conteo de la variable, numeros
                correctos'''
                lista_num_correcto.append(caracter)
                '''Agregamos el indice a la lista número correcto'''
        if num_correctos == 4:
                '''Si la variable de números correctos es igual a 4, significa
                que se adivino el número aleatorio. Se le informa al usuairo
                y rompe el ciclo principal'''
                print('$' * 60)
                print('FELICIDADES, ENCONTRASTE EL NÚMERO')
                print(f'Número ingresado: {numero_persona}')
                print(f'Número aleatorio: {numero_pc}')
                print(f'Número de intentos restantes: {intentos} intentos')
                print('$' * 60)
                bandera = False
                '''Se coloca en False a la variable bandera y rompe
                el ciclo while principal'''
                break
        else:
            '''Si la variable numeros correctos no es igual a cuatro,
            entonces compara cada numero del numero ingresado por
            el usuario con cada número del número aleatorio, esto
            para encontrar aquellos numeros que se eligiron correctamente
            pero no están en la poscisión correcta'''
            for caracter_persona in range(len(numero_persona)):
                '''Ciclos para comparar cada número del numero de usuario
                con cada número del número aleatorio por sus indices.
                La variable caracter_persona almacena el indice del número
                de usuario que se evalua actualmente y la variable caracter_pc
                alamcena el indice del número aleatorio que se evalua actualmente'''
                for caracter_pc in range(len(numero_pc)):
                    if caracter_pc in lista_num_correcto and \
                            numero_pc[caracter_pc] == numero_persona[caracter_persona] and\
                            caracter_pc == caracter_persona:
                        '''Si el caracter_pc ya se encuentra en la lista de número correctos
                        y, con el indice caracter_pc se obtiene el número de ese indice del
                        número_pc y este es igual al número del número del usuairo con el indice
                        del caracter_persona y el indice en la variable caracter_pc
                        es igual al indice en la variable caracter_persona. Significa que el
                        número actaulemnte evaluados estan en el mismo indice y son iguales.
                        Esos números ya los comparamos en un ciclo anterior por lo que rompe
                        el ciclo interno'''
                        break
                    elif caracter_pc in lista_num_correcto and \
                            numero_pc[caracter_pc] == numero_persona[caracter_persona]:
                        '''Si el caracter_pc ya se encuentra en la lista de número correctos
                        y, con el indice caracter_pc se obtiene el número de ese indice del
                        número_pc y este es igual al número del número del usuairo con el indice
                        del caracter_persona. Significa que el número con el indice de caratcer_pc
                        del número aleatorio ya tiene un número en su posición correcta y continua
                        el ciclo. Como ejemplo el número aleatorio es 1123 y el número de usuario 
                        es 1145, si compara el inice del número de usuario (1) con el indice del
                        número aleatorio (0) realmente el indice del número aleatorio (0) ya esta
                        la lista numeros correctos pues ya se comparo anteriormente el indice del 
                        número aleatorio (0) con el indice (0) del número del usuario y como son 
                        iguales, solo continua el ciclo a comparar el indice (1) del número aleatorio 
                        con el indice (1) del número del usuario'''
                        continue
                    elif caracter_pc not in lista_num_correcto and \
                            caracter_pc not in lista_pos_incorrecta and \
                            numero_pc[caracter_pc] == numero_persona[caracter_persona]:
                        '''Si el caracter_pc no se encuentra en la lista de número correctos
                        y si el catacter_pc no se encuentra en la lista de números en la
                        posición incorrecta y el indice en la variable caracter_pc
                        es igual al indice en la variable caracter_persona y, con el indice 
                        caracter_pc se obtiene el número de ese indice del número_pc y este 
                        es igual al número del número del usuario con el indice del caracter_persona.
                        Significa que se encontro un número que no tiene "asignado" un número
                        en la poscición correcta y no tiene "asignado" un número en la
                        posición incorrecta pero son iguales a los números comparados, por lo
                        que posiblemente se encontró un número en la poscisión incorrecta'''
                        if numero_persona[caracter_persona] == numero_pc[caracter_persona]:
                            '''Antes de confirmar que se encontró un número en la posición incorrecta,
                            se compara los números con el mismo indice de carcter_persona en el
                            número aleatorio y el número del usuario, si son iguales, entonces no
                            encontró un número en la poscición incorrecta pues realmente si tiene
                            "asignado" un número en la poscición correcta y continus el ciclo'''
                            continue
                        else:
                            '''Aumenta la variable posición incorrecta pues se encontró una número
                            en la posición incorrecta y añade el indice de caracter pc a la lista 
                            de posición incorrecta. rompe el ciclo para continuar a comparar el siguiente
                            número del usuario'''
                            poscision_incorrecta += 1
                            lista_pos_incorrecta.append(caracter_pc)
                            break
        intentos -= 1
        '''Restamos una unidad a los intentos'''
        if intentos < 1:
            '''Si los intentos son menores a 1, entonces 
            informa al usuario que el juego termino'''
            print('*' * 60)
            print('FIN DEL JUEGO')
            print(f'Número equivocado: {numero_persona}')
            print(f'Número aleatorio: {numero_pc}')
            print(f'Cantidad de números correctos: {num_correctos}')
            print(f'Cantidad de poscisiones incorrectas: {poscision_incorrecta}')
            print(f'Quedan {intentos} intentos')
            print('*' * 60)
            lista_num_correcto.clear()
            lista_pos_incorrecta.clear()
            '''Limpia las variables de las listas que lleva el conteo de indices
            para números correctos y posiciones correctas, además de colocar
            en cero las variables que llevan el conteo de números correctos
            y posciciones correctas.'''
            num_correctos = 0
            poscision_incorrecta = 0
            break
        else:
            '''Si los intentos no son menores a 1, entonces 
            informa al usuario cuantos números estan en la posición
            correcta y cuantos estan en la posición incorrecta'''
            print('*' * 60)
            print(f'Número equivocado: {numero_persona}')
            print(f'Cantidad de números correctos: {num_correctos}')
            print(f'Cantidad de poscisiones incorrectas: {poscision_incorrecta}')
            print(f'QUEDAN {intentos} INTENTOS')
            print('*' * 60)
            lista_num_correcto.clear()
            lista_pos_incorrecta.clear()
            '''Limpia las variables de las listas que lleva el conteo de indices
            para números correctos y posiciones correctas, además de colocar
            en cero las variables que llevan el conteo de números correctos
            y posciciones correctas pues para evaluar el siguien número que
            ingresa el usario, las variables deben estar sin datos'''
            num_correctos = 0
            poscision_incorrecta = 0


def main():
    mastermind()
main()
