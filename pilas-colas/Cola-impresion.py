import os
from collections import deque
# definir la cola
cola = deque()
ciclo = True

while  ciclo: 
    print('+++++++++++++++')
    print('Desea ?')
    print('1) Agregar un elemento a la cola de impresion')
    print('2) imprimir')
    print('3) salir')
    menu = int(input('ingrese una opcion:  '))
    if menu >0 and menu <4:
        if menu ==1:
            os.system("cls")
            print ('ingrese la ruta de la carpeta en la que quiere listar sus archivos')
            ruta = input()
            os.system('cls')
            print ('Se encontraron los siguientes archivos en la carpeta actual.')
            # en listar los nombres de los archivos 
            files = os.listdir(ruta)
            print(files)
            print('Ingrese el número de archivo que desea agregar a la cola:')
            archivo = int(input())
            archivo -=1
            elemento = files[archivo]
            print('La cola de impresión es:')
            i=0
            print([i+1] , elemento)
            cola.append(elemento)
            print(cola)
        if menu == 2:
            if len(cola) > 0:
                # extraer el primer elemento en la cola
                siguiente_elemento = cola.popleft()

                print(f'se imprimio el archivo: {siguiente_elemento}')
                print(f'Cola de impresión: {cola}')
            else:
                print('la cola de impresion esta vacia ')  
        if menu == 3:
            ciclo = False 
            os.system('cls')     
    else:
        print('ingrese un valor correcto')
ciclo = True