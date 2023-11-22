#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")
# write 'hello world' to the console
print("hello world")


# Importar la libreria random
import random

# Crear una lista de opciones para el juego
opciones = ["piedra", "papel", "tijera", "fin"]

# Crear una variable para la puntuación del jugador
puntuacion_jugador = 0

# Crear una variable para la puntuación del oponente
puntuacion_oponente = 0

# Crear una variable para el estado del juego
estado_juego = True

# Crear una función para el juego
def juego():
    # Crear una variable para la puntuación del jugador
    global puntuacion_jugador
    # Crear una variable para la puntuación del oponente
    global puntuacion_oponente
    # Crear una variable para el estado del juego
    global estado_juego
    # Crear una variable para el oponente
    oponente = random.choice(opciones)
    # Crear una variable para la entrada del jugador
    jugador = input("Elige piedra, papel o tijera: ").lower()

    # Crear una condición para el juego
    if jugador in opciones:
        # Crear una condición para el empate
        if jugador == oponente:
            print("Empate!")
        # Crear una condición para la victoria del jugador
        elif jugador == "piedra" and oponente == "tijera":
            print("Ganaste!")
            puntuacion_jugador += 1
        elif jugador == "papel" and oponente == "piedra":
            print("Ganaste!")
            puntuacion_jugador += 1
        elif jugador == "tijera" and oponente == "papel":
            print("Ganaste!")
            puntuacion_jugador += 1
        # Crear una condición para la victoria del oponente
        elif jugador == "piedra" and oponente == "papel":
            print("Perdiste!")
            puntuacion_oponente += 1
        elif jugador == "papel" and oponente == "tijera":
            print("Perdiste!")
            puntuacion_oponente += 1
        elif jugador == "tijera" and oponente == "piedra":
            print("Perdiste!")
            puntuacion_oponente += 1
        # Crear una condición para el final del juego
        elif jugador == "fin":
            estado_juego = False
        # Crear una condición para la entrada no válida
        else:
            print("Entrada no válida!")
    # Crear una condición para la entrada no válida
    else:
        print("Entrada no válida!")

# Crear un bucle para el juego
while estado_juego:
    juego()
    print("Puntuación del jugador: " + str(puntuacion_jugador))
    print("Puntuación del oponente: " + str(puntuacion_oponente))
    print("")

# Crear una condición para la victoria del jugador
if puntuacion_jugador > puntuacion_oponente:
    print("¡Ganaste el juego!")
# Crear una condición para la victoria del oponente
elif puntuacion_oponente > puntuacion_jugador:
    print("¡Perdiste el juego!")
# Crear una condición para el empate
else:
    print("¡Empate!")




                    

