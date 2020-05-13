import os #Libreria para funciones de limpiar pantalla y pausa
from random import randint #Libreria para generar opcion aleatoria de la computadora
# importar el tipo de dato para utilizar pilas y colas
from collections import deque

Ciclo = True #Ciclo para Repetir el juego 
# definir la pila
Historial = deque()
while Ciclo:
    respuesta_pc = randint(1, 3) # 1 piedra 2 papel 3 tijera
    os.system("cls")
    print ("****************** Bienvenidos *********************")
    print ("************ Juego Piedra, Papel o Tijera **********")
    print ("Ingrese su opción: ") #Menu para selección del jugador
    print ("1. Piedra")
    print ("2. Papel")
    print ("3. Tijera")
    Opcion = int(input("Su opción: "))

    if Opcion > 0 and Opcion < 4: #Validación de opción correcta
        os.system("cls")
        if Opcion == 1:
            Jugador = "Jugador: Piedra"
        elif Opcion == 2:
            Jugador = "Jugador: Papel"
        elif Opcion == 3:
            Jugador = "Jugador: Tijera"

        if respuesta_pc == 1:
            PC = "Computadora: Piedra"
        elif respuesta_pc == 2:
            PC = "Computadora: Papel"
        elif respuesta_pc == 3:
            PC = "Computadora: Tijera"

        if respuesta_pc == Opcion: #Resultados del juego
            Resultado = "Resultado: ¡Empate!"
        if respuesta_pc == 1 and Opcion == 2:
            Resultado = "Resultado: ¡Gana Jugador!"    
        if respuesta_pc == 1 and Opcion == 3:
            Resultado = "Resultado: ¡Gana Computadora!"
        if respuesta_pc == 2 and Opcion == 1:
            Resultado = "Resultado: ¡Gana Computadora!"
        if respuesta_pc == 2 and Opcion == 3:
            Resultado = "Resultado: ¡Gana Jugador!"
        if respuesta_pc == 3 and Opcion == 1:
            Resultado = "Resultado: ¡Gana Jugador!"
        if respuesta_pc == 3 and Opcion == 2:
           Resultado = "Resultado: ¡Gana Computadora!"

        print(Jugador) #Mostrar resultados en pantalla
        print(PC)
        print(Resultado)
        os.system("pause")   
 
        Historial.append([Jugador, PC, Resultado])  #Almacenar datos a la pila

    else:
        print("Escriba un opción válida")
        os.system("pause")

    CicloMenu = True #Ciclo de menu 
    while CicloMenu:
        os.system("cls")
        print("Deseas?") #Menu
        print("1. Volver a jugar")
        print("2. Ver Resultado Anterior")
        print("3. Salir")
        Menu = int(input())

        if Menu == 1:
            CicloMenu = False
        elif Menu == 2:
            os.system("cls")
            if len(Historial) > 0: #Mostrar el historial almacenado
                Ultima = Historial.pop()
                for elem in Ultima:
                    print(elem)

                os.system("pause")
            else:
                print("¡El historial esta vacio!")
                os.system("pause")    
        elif Menu == 3: #Finalizar el juego
            CicloMenu = False
            Ciclo = False  

        else:
            print("Ingrese un Valor Correcto")
            os.system("pause")         