import random

# Variables
pozo_jugador = 0


def bienvenido():
    print('♠ ' * 25, 'BlackJack', '♠ ' * 25)

    nombre = input('Ingrese su nombre: ')

    monto = int(input('Ingrese un monto a su pozo para inciar la partida: '))

    if nombre == " ":
        nombre = input('Ingrese su nombre ¡Correctamente!!: ')

    if not (monto > 0 and monto < 100000):
        monto = int(input('Ingrese un monto a su pozo para inciar la partida: '))
    else:
        monto = monto

    # Retornamos el valor de nombre, y el monto del pozo en una tupla
    return nombre, monto


# En esta funcion mostraremos el menu de opciones, luego le solicitamos al usuario que ingrese su eleccion, y returnamos el valor a la funcion
def leer_opciones():
    print('-> Menú de opciones')
    print('1 -> Apostar')
    print('2 -> Jugar una Mano')
    print('3 -> Salir')

    opcion = int(input('Ingrese su opcion: '))
    return opcion


# Funcion de apuesta, recibe como parametro una variable que corresponde con el pozo del jugador, y el cual sera modificado segun la cantidad de dinero que quiera añadir el jugador
def apostar():
    # El jugador ingresa la apuesta que desea añadir a su pozo
    apuesta = int(input('Ingrese la apuesta, para añadir al pozo: '))
    while apuesta < 0 and apuesta == 0:
        apuesta = int(input('Ingrese la apuesta, para añadir al pozo: '))

    return apuesta


# Generamos la carta
def gen_card():
    # 3 Tuplas, con las 'figuras', sus respectivos valores, y el palo a generar

    nombres = ('AS', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    valores = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)

    palos = ('diamante', 'corazon', 'trebol', 'pica')

    ind = random.randint(0, 12)

    # Generar la carta a partir de acceder a un indice aleatorio, generado en la variable ind

    carta = (nombres[ind], valores[ind], random.choice(palos))

    return carta


def apuesta_en_juego(pozo):
    # Solicitar apuesta a jugar en la mano al jugador
    apuesta_juego = int(input('-' * 8 + '>Ingrese el monto a apostar por la mano: '))
    if apuesta_juego > pozo and not (apuesta_juego % 5 == 0):
        apuesta_juego = int(
            input('Ingrese el monto a apostar por la mano siendo menor a su pozo inicial, y multiplo de 5: '))

    return apuesta_juego


# Validar si puede recibir nuevas cartas le jugador, hacemos una funcion que reciba como parametro una puntuacion, y el input de la S o N,y verificar si estahabilitado a recibir nuevas cartas
def nueva_carta_q(preg, puntuacion):
    if preg == 'S' and puntuacion <= 21:
        # Retornamos un boolean para poder evaluar luego la generacion o no de la tercera carta
        return True
    else:
        print('No se puede generar una nueva carta')
        return False


# Calculo Porcentaje de victorias:
def porcen_vict(cant_partidos, cant_victorias):
    porcentaje_victorias_jug = (cant_victorias * 100) // cant_partidos
    return porcentaje_victorias_jug


def loop_principal():
    # En esta linea llamamos a la funcion bienvenido, que retorna el valor del nombre, y el monto, y se lo asignamos a las variables llamadas de igual manera
    player, monto = bienvenido()

    monto_inicial_pozo = monto

    # print('El nombre es: ', player, 'cuyo monto es: ', monto)

    # Variables -> Para Opcion 3

    cant_victorias_jugador = 0

    cant_victorias_croupier = 0
    cant_partidos = 0

    acumula_racha = 0
    racha_croupier = False

    manos_bn = 0

    mayor = 0

    acum_pozo = 0

    mayor_apuesta = 0
    perdida = False

    cont_apuestas = 0
    opcion = None

    while opcion != 3:

        print()
        print()

        opcion = leer_opciones()

        print()
        print()

        if opcion == 1:
            print('Se eligio la primer opcion')

            apuesta_a_agregar_pozo = apostar()
            print('*' * 21, 'Usted Agrega', apuesta_a_agregar_pozo, '$ a su pozo', '*' * 21)
            monto += apuesta_a_agregar_pozo
            print('*' * 21, 'Su pozo actual es de', monto, '$', '*' * 21)

        elif opcion == 2:
            cant_partidos += 1
            print('Se eligio la segunda opcion')

            puntuacion_jugador = 0
            puntuacion_croupier = 0

            cant_cartas_jugador = 2
            cant_cartas_croupier = 1

            band_black_nat = False
            band_black_nat_croup = False

            # Definir el monto a apostar
            print('-' * 8 + '>', 'Pozo del jugador es', monto, '$')

            apuesta_juego = apuesta_en_juego(monto)

            # Acumular las apuestas para poder ver el monto promedio que dispuso para realizar apuestas
            acum_pozo += apuesta_juego
            # Contador para las veces de la apuesta
            cont_apuestas += 1

            # Estado Actual del monto Luego de la apuesta
            monto -= apuesta_juego
            print('-' * 8 + '>', 'El Pozo del jugador es', monto, '$')
            print()

            print('♢ ' * 25, 'Generando Primera Carta Jugador', '♢ ' * 25)
            print()

            # Generamos las primeras Cartas para ambos jugadores, croupier, y player
            carta_jugador = gen_card()

            # Mostramos la primera carta del jugador, con su palo
            print('La carta de', player, 'es el ', carta_jugador[0], 'cuyo palo es', carta_jugador[2])

            print('♢ ' * 25, 'Generando Segunda Carta Jugador', '♢ ' * 25)
            print()

            segunda_carta_jugador = gen_card()

            # Mostramos la segunda carta del jugador con su palo
            print('La Segunda carta de', player, 'es el ', segunda_carta_jugador[0], 'cuyo palo es',
                  segunda_carta_jugador[2])

            # Generamos la carta del croupier
            carta_croupier = gen_card()

            # Mostramos la carta del croupier con su palo
            print('Carta Croupier: ', carta_croupier[0], 'cuyo palo es', carta_croupier[2])

            # Calculamos el puntaje final del jugador

            puntuacion_jugador = carta_jugador[1] + segunda_carta_jugador[1]

            # Verificamos que el puntaje no se pase de 21 en caso de haber sumado dos ases seguidos

            if puntuacion_jugador > 21 and segunda_carta_jugador[0] == 'AS':
                print('Salieron DOS ASES SEGUIDOS, y se excedio en la puntuacion')
                puntuacion_jugador = carta_jugador[1] + 1
            else:
                puntuacion_jugador = carta_jugador[1] + segunda_carta_jugador[1]

            puntuacion_croupier = carta_croupier[1]

            print('- ' * 25, 'El puntaje total de', player, 'es de:', puntuacion_jugador, 'puntos', '- ' * 25)

            print()

            # Detectar si es blackjack natural:
            if puntuacion_jugador == 21:
                band_black_nat = True

            print('- ' * 25, 'El puntaje total del croupier es de:', puntuacion_croupier, 'puntos', '- ' * 25)
            print()
            print()
            if puntuacion_jugador < 21:
                # Preguntar si desea una nueva carta el jugador
                question = input('Desea seguir recibiendo cartas (S/N): ')

                # Creo un bucle while para controlar la generacion de la carta
                while question != "N" and puntuacion_jugador < 21:
                    carta_jugador_extra = gen_card()

                    # Guardo La puntuacion previa a la suma para poder modificar en caso de que salga AS y se pase de 21
                    puntuacion_jugador_resplado = puntuacion_jugador

                    print('La carta de', player, 'es el ', carta_jugador_extra[0], 'cuyo palo es',
                          carta_jugador_extra[2])
                    puntuacion_jugador += carta_jugador_extra[1]
                    if carta_jugador_extra[0] == 'AS' and puntuacion_jugador > 21:
                        print('La carta de', player, 'es el ', carta_jugador_extra[0], 'cuyo palo es',
                              carta_jugador_extra[2], ' y su valor es 1 dado que se ha pasado de 21')
                        puntuacion_jugador_resplado += 1
                        puntuacion_jugador = puntuacion_jugador_resplado
                    # puntuacion_jugador += carta_jugador_extra[1]
                    print('- ' * 25, 'El puntaje total de', player, 'es de:', puntuacion_jugador, 'puntos', '- ' * 25)

                    # Acumulo la cantidad de cartas Generadas para el jugador:
                    cant_cartas_jugador += 1

                    if not (puntuacion_jugador > 21):
                        question = input('Desea seguir recibiendo cartas (S/N): ')
                else:
                    print('- ' * 25, 'El puntaje FINAL de', player, 'es de:', puntuacion_jugador, 'puntos', '- ' * 25)

            # Una vez que el jugador acabo de jugar puedo generar las cartas del croupier

            print('♢ ' * 25, 'Generando Segunda Carta Croupier', '♢ ' * 25)
            print()

            segunda_carta_croupier = gen_card()

            # Mostramos la segunda carta del croupier con su palo
            print('Carta Croupier: ', segunda_carta_croupier[0], 'cuyo palo es', segunda_carta_croupier[2])

            # Puntaje Croupier

            puntuacion_croupier = carta_croupier[1] + segunda_carta_croupier[1]

            print('-' * 25, 'La puntuacion del croupier es de:', puntuacion_croupier, 'puntos', '-' * 25)

            # Verifico si es un BlackJack Natural Del Croupier;
            if puntuacion_croupier == 21:
                band_black_nat_croup = True

            # Croupier Pide Cartas Mientras tenga 16 o menos y [16,17)

            print('♢ ' * 25, 'Cartas Croupier', '♢ ' * 25)
            print()

            while puntuacion_croupier <= 16:
                # Verifico Primero que la puntuacion del croupier sea menor a 17
                if puntuacion_croupier >= 17:
                    print('-' * 25, 'El puntaje total del croupier es de:', puntuacion_croupier, 'puntos', '-' * 25)
                else:
                    carta_croupier_extra = gen_card()

                    # Guardo La puntuacion previa a la suma para poder modificar en caso de que salga AS y se pase de 21
                    puntuacion_croupier_respaldo = puntuacion_croupier

                    print('Carta Croupier: ', carta_croupier_extra[0], 'cuyo palo es', carta_croupier_extra[2])
                    puntuacion_croupier += carta_croupier_extra[1]

                    if carta_croupier_extra[0] == 'AS' and puntuacion_croupier > 21:
                        puntuacion_croupier_respaldo += 1
                        puntuacion_croupier = puntuacion_croupier_respaldo
                    print('-' * 25, 'El puntaje total del croupier es de:', puntuacion_croupier, 'puntos', '-' * 25)

                    # Acumulo la cantidad de cartas generadas para el croupier
                    cant_cartas_croupier += 1

            # Concluimos en la busqueda del ganador
            print('♠ ' * 21, 'Resultados', '♠ ' * 21)
            print()
            print()

            print('-' * 25, 'El puntaje total de', player, 'es de:', puntuacion_jugador, 'puntos', '-' * 25)

            print()

            print('-' * 25, 'El puntaje total del croupier es de:', puntuacion_croupier, 'puntos', '-' * 25)

            print()
            print()

            # Verifico la racha_croupier
            if racha_croupier:
                acumula_racha = cant_victorias_croupier
                acumula_racha += 1
            else:
                acumula_racha = 0

            empate = False
            distancia_player = abs(21 - puntuacion_jugador)

            distancia_croupier = abs(21 - puntuacion_croupier)

            # Verifico si hay blackJack
            if band_black_nat and (cant_cartas_croupier >= 3 and puntuacion_croupier == 21):

                print('♠' * 21, 'BLACKJACK NATURAL', player, ' Ganaste!!!!', '♠' * 21)
                ganancias = apuesta_juego * 2
                monto += ganancias
                print('-' * 21, 'Sus ganancias son: ', ganancias, '$', '-' * 21)
                print('-' * 21, 'Su Monto Actual es de:', monto, '$', '-' * 21)
                cant_victorias_jugador += 1
                racha_croupier = False
                manos_bn += 1

            elif band_black_nat_croup and (cant_cartas_jugador >= 3 and puntuacion_jugador == 21):

                print('-' * 21, 'BLACKJACK NATURAL, Intenta Nuevamente el ganador es el Croupier!!!!', '-' * 21)
                ganancias_croupier = apuesta_juego
                print('-' * 21, 'Su Monto Actual es de:', monto, '$', '-' * 21)
                print('-' * 21, 'Ganancias Del Croupier: ', ganancias_croupier, '$', '-' * 21)
                cant_victorias_croupier += 1
                racha_croupier = True
                manos_bn += 1
                perdida = True

            else:

                # El jugador tiene mayor puntuacion pero menor o igual a 21
                if (puntuacion_jugador > puntuacion_croupier) and puntuacion_jugador <= 21:

                    print('♠' * 21, 'Felicidades', player, ' Ganaste!!!!', '♠' * 21)
                    ganancias = apuesta_juego * 2
                    monto += ganancias
                    print('-' * 21, 'Sus ganancias son: ', ganancias, '$', '-' * 21)
                    print('-' * 21, 'Su Monto Actual es de:', monto, '$', '-' * 21)
                    cant_victorias_jugador += 1
                    racha_croupier = False

                # El croupier tiene mayor puntuacion pero menor o igual a 21
                elif (puntuacion_croupier > puntuacion_jugador) and puntuacion_croupier <= 21:

                    print('-' * 21, 'Intenta Nuevamente el ganador es el Croupier!!!!', '-' * 21)
                    ganancias_croupier = apuesta_juego
                    print('-' * 21, 'Su Monto Actual es de:', monto, '$', '-' * 21)
                    print('-' * 21, 'Ganancias Del Croupier: ', ganancias_croupier, '$', '-' * 21)
                    cant_victorias_croupier += 1
                    racha_croupier = True
                    perdida = True

                elif puntuacion_jugador > 21 and puntuacion_croupier > 21:

                    print('-' * 21, 'Ambos Se fueron mas de 21 puntos, vuelve a jugar!!', '-' * 21)
                    ganancias = apuesta_juego
                    monto += apuesta_juego
                    print('-' * 21, 'Su apuesta es:', apuesta_juego, '$', '-' * 21)
                    print('-' * 21, 'Sus ganancias son:', ganancias, '$', '-' * 21)
                    print('-' * 21, 'Su Monto Actual es de:', monto, '$', '-' * 21)
                    racha_croupier = False

                #El jugador tiene mayr puntuacion pero es mayor a 21
                elif (puntuacion_jugador > puntuacion_croupier) and puntuacion_jugador > 21:
                    print('-' * 21, 'Intenta Nuevamente el ganador es el Croupier!!!!', '-' * 21)
                    ganancias_croupier = apuesta_juego
                    print('-' * 21, 'Su Monto Actual es de:', monto, '$', '-' * 21)
                    print('-' * 21, 'Ganancias Del Croupier: ', ganancias_croupier, '$', '-' * 21)
                    cant_victorias_croupier += 1
                    racha_croupier = True
                    perdida = True

                elif (puntuacion_croupier > puntuacion_jugador) and puntuacion_croupier > 21:
                    print('♠' * 21, 'Felicidades', player, ' Ganaste!!!!', '♠' * 21)
                    ganancias = apuesta_juego * 2
                    monto += ganancias
                    print('-' * 21, 'Sus ganancias son: ', ganancias, '$', '-' * 21)
                    print('-' * 21, 'Su Monto Actual es de:', monto, '$', '-' * 21)
                    cant_victorias_jugador += 1
                    racha_croupier = False



                # Veo si hay empate
                elif puntuacion_jugador == puntuacion_croupier:
                    print('-' * 21, 'Ambos Obtuvieron el mismo Puntaje, vuelve a jugar!!', '-' * 21)
                    monto += apuesta_juego
                    print('-' * 21, 'Su Monto Actual es de:', monto, '$', '-' * 21)
                    racha_croupier = False

                elif puntuacion_jugador > 21 and puntuacion_croupier > 21:

                    print('-' * 21, 'Ambos Se fueron mas de 21 puntos, vuelve a jugar!!', '-' * 21)
                    ganancias = apuesta_juego
                    monto += apuesta_juego
                    print('-' * 21, 'Sus ganancias son: ', ganancias, '$', '-' * 21)
                    print('-' * 21, 'Su Monto Actual es de:', monto, '$', '-' * 21)
                    racha_croupier = False

                # Pozo Mayor:
                if monto > mayor:
                    mayor = monto

                # Monto Promedio de todas las apuestas
                if cont_apuestas != 0:
                    promedio = (acum_pozo / cont_apuestas)
                else:
                    promedio = 0

                # Ver la pérdida mas grande del jugador si existio
                if perdida:
                    if apuesta_juego > mayor_apuesta:
                        mayor_apuesta = apuesta_juego
                else:
                    # Hago que mayor apuesta sea cero dado que seria en caso la apuesta mas grande de las perdidas, y como si el jugador apostase 2000 y no perdiera su mayor apuesta perdida seria cero
                    mayor_apuesta = 0

                # Muestro Por Pantalla
                print('\t', '-' * 11, '>Resultados:')
                print('\t', '-' * 15, '>Monto Inicial del pozo:', monto_inicial_pozo, '$')
                print('\t', '-' * 15, '>Monto de la apuesta:', apuesta_juego, '$')
                print('\t', '-' * 15, '>Monto actualizado del pozo:', monto, '$')



        elif opcion == 3:
            print('\t', 'Victorias Jugador: ', cant_victorias_jugador)
            print('\t', 'Victorias Croupier: ', cant_victorias_croupier)
            print('\t', 'La racha del croupier es: ', acumula_racha, 'manos seguidas')
            print('\t', 'La cantidad de manos con BlackJack Natural fueron: ', manos_bn)
            print('\t', 'La cantidad maxima que tuvo el jugador en el pozo es: ', mayor, '$')
            print('\t', 'El monto promedio del que dispuso el jugador para realizar apuestas fue de: ', str(promedio),
                  '$')
            if mayor_apuesta != 0:
                print('La pérdida más grande que sufrió el jugador (en moneda) fue: ', mayor_apuesta)
            else:
                print('El jugador no sufrio ninguna perdida')

            if cant_victorias_jugador < 0:
                print('*' * 21, 'Porcentaje de victorias de', player, '0%')
            else:
                porcentaje_victorias = porcen_vict(cant_partidos, cant_victorias_jugador)
                print('*' * 21, 'Porcentaje de victorias de', player, str(porcentaje_victorias), '%', '*' * 21)


# LLamada a la funcion principal
loop_principal()
