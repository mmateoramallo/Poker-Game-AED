import random

# Variables
pozo_jugador = 1000


def gen_card():
    # 3 Tuplas, con las 'figuras', sus respectivos valores, y el palo a generar

    nombres = ('AS', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    valores = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)

    palos = ('diamante', 'corazon', 'trebol', 'pica')

    ind = random.randint(0, 12)

    # Generar la carta a partir de acceder a un indice aleatorio, generado en la variable ind

    carta = (nombres[ind], valores[ind], random.choice(palos))

    return carta


def apostar(pozo):
    # Le solicito al usuario su apuesta a agregar al pozo del jugador
    apuesta = int(input('Ingrese su apuesta: '))
    # Validamos el valor ingresado por el usuario, dado que no puede ser negativo ni cero, se entrara en un buclee, hasta que el valor de la apuesta

    while not (apuesta > 0):
        apuesta = int(input('Ingrese su apuesta ¡Debe Ser Mayor a cero!: '))
    else:
        # La apuesta debe ser múltiplo de 5 y menor o igual al dinero que posee en su pozo.
        if (apuesta % 5 == 0 and apuesta <= pozo):
            # Se agregara el valor de la apuesta correctamente al pozo
            pozo += apuesta
    # Retornamos el valor a la funcion para mas tarde asignarselo al valor del pozo del jugador.
    return pozo


pozo_jugador = apostar(pozo_jugador)

print('El pozo del jugador es: ', pozo_jugador)


def jugar_mano():
    pass


# Bucle Principal
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


def leer_opciones():

    print('-> Menú de opciones')
    print('1 -> Apostar')
    print('2 -> Jugar una Mano')
    print('3 -> Salir')

    opcion = int(input('Ingrese su opcion: '))
    return opcion

def loop_principal():

    opcion = None

    print()
    while opcion != 3:
        opcion = leer_opciones()
