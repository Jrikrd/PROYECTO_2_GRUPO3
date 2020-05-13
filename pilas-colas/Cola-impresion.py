import os #Libreria utilizada para funciones de limpiar pantalla y pausa
from collections import deque  #Libreria utilizada para la funcion de cola

cola = deque() # definir la cola
ciclo = True #Ciclo de menu
while  ciclo: 
    os.system("cls") 
    print('+++++++++++++++')  #Menu
    print('Desea ?')
    print('1) Agregar un elemento a la cola de impresion')
    print('2) imprimir')
    print('3) salir')
    menu = int(input('ingrese una opcion:  '))
    if menu >0 and menu <4: #Validacion de ingreso de opcion correcta
        if menu ==1: # Agregar un archivo a la cola de impresión
            os.system("cls")
            print ('ingrese la ruta de la carpeta en la que quiere listar sus archivos')
            ruta = input() # Variable para leer la ruta de la carpeta
            os.system('cls')
            print ('Se encontraron los siguientes archivos en la carpeta actual.')
            # en listar los nombres 44de los archivos 
            files = os.listdir(ruta)
            cont = 0
            for elem in files: #Ciclo para mostrar los archivos que estan en la carpeta
                cont += 1
                print([cont], elem)
            print('[0] Cancelar')     
            print('Ingrese el número de archivo que desea agregar a la cola:')
            archivo = int(input()) #Variable para seleccionar el archivo que se quiere agregar a la cola
            if archivo != 0:
                elemento = files[archivo - 1]
                cola.append(elemento) #Agregar un archivo a las cola de impresion
                print('La cola de impresión es:')
                cont2=0
                cont3=0
                for elem in cola:
                    cont2 += 1
                    print([cont2], cola[cont3])
                    cont3 += 1                   
            os.system("pause")
        if menu == 2:
            if len(cola) > 0:
                os.system("cls")
                # extraer el primer elemento en la cola
                siguiente_elemento = cola.popleft()

                print(f'se imprimio el archivo: {siguiente_elemento}') 
                if len(cola) > 0:
                    print('La cola de impresión es:')
                    cont2=0
                    cont3=0
                    for elem in cola:
                        cont2 += 1
                        print([cont2], cola[cont3])
                        cont3 += 1 
                else:
                    print('la cola de impresion esta vacia ') 

            else:
                os.system("cls")
                print('la cola de impresion esta vacia ')  
            os.system("pause")    
        if menu == 3:
            ciclo = False 
            os.system('cls')     
    else:
        print('ingrese un valor correcto')
        os.system("pause")
