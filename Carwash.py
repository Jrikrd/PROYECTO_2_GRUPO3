ciclo = True  # ciclo para que el programa regrese al menu de inicio
while ciclo:
    print('Programa de lavado de autos ','\n')
    print('1. Motocicleta (Q.15)')
    print('2. Automovil (Q.30)')
    print('3. Camioneta (Q.50)')
        print('Seleccione el tipo de vehiculo que desea lavar: ','\n' ) 
    tipo_vehiculo = int(input()) 
    if tipo_vehiculo >0 and tipo_vehiculo <4:  #validar solo las opciones del menu
        if tipo_vehiculo == 1:
            Vehiculo = ('Motocicleta')
            Precio = 15 
        if tipo_vehiculo == 2:
            Vehiculo = ('Automovil')
            Precio = 30  
        if tipo_vehiculo == 3:
            Vehiculo = ('Camioneta') 
            Precio = 50 
        ciclo_cliente = True
        while ciclo_cliente: #segundo ciclo para menu 2
            print('Seleccione el tipo de cliente:','\n')
            print('1. Cliente Estandar')
            print('2. Miembro','\n')
            tipo_Cliente = int(input())
            else:
                print('\n''*****Opcion seleccionada no es valida*****''\n')
        print('¿Desea realizar otro registro? (Y/N)')
        volver_intentarlo = input()  
        if volver_intentarlo == ('N') or ('n'): #validar opciones de salida
            ciclo = False                 
    else:
        print('\n''*****Opcion seleccionada no es valida*****''\n')
    ciclo = True #fin ciclo

#fin