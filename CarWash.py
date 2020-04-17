import json
import sys
base_de_datos = []
ciclo = True
while ciclo:
    print('Programa de lavado de autos ','\n')
    print('1. Motocicleta (Q.15)')
    print('2. Automovil (Q.30)')
    print('3. Camioneta (Q.50)')
    print('4. Salir')
    print('Seleccione el tipo de vehiculo que desea lavar: ','\n' ) 
    tipo_vehiculo = int(input())
    if tipo_vehiculo == 4: 
        sys.exit()

    if tipo_vehiculo >0 and tipo_vehiculo <4:
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
        while ciclo_cliente:
            print('Seleccione el tipo de cliente:','\n')
            print('1. Cliente Estandar')
            print('2. Miembro','\n')
            tipo_Cliente = int(input())
            if tipo_Cliente >0 and tipo_Cliente <3:
                cliente = ('Estandar')
                if tipo_Cliente == 2:
                    Miembro = Precio * 0.10
                    cliente = ('Miembro') 
                ciclo_cliente = False                
            else:
                print('\n''*****Opcion seleccionada no es valida*****''\n')
        print('¿Es fin de semana? (Y/N)')
        Finde = True
        descuento_finde = input()
        if descuento_finde == ('N') or ('n'):
            Finde = False
            Fd = Precio * 0.10    
        Registro_Clientes = {} # Lista para guardar nombres
        Descuentos = Miembro + Fd
        Total = Precio - Descuentos - Miembro
        Registro_Clientes['Tipo'] = Vehiculo #listado 1
        Registro_Clientes['Precio'] = Precio  #listado 2
        Registro_Clientes['Cliente'] = cliente
        Registro_Clientes['Fin De Semana'] = Finde
        Registro_Clientes['Descuentos'] = Descuentos
        Registro_Clientes['Total'] = Total
        base_de_datos.append(Registro_Clientes)  # Agregar datos a listado
        print('\n','Registro Agregado','\n')
        print('¿Desea realizar otro registro? (Y/N)')
        volver_intentarlo = input()  
        if volver_intentarlo == ('N') or ('n'): 
            ciclo = False  
        with open('base_de_datos.json', 'w') as archivo: # Para exportar datos a un Json
            json.dump(base_de_datos, archivo)                 
    else:
        print('\n''*****Opcion seleccionada no es valida*****''\n')
    ciclo = True