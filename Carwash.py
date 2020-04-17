import json
import sys
import os

base_de_datos = []     #Guardar la información de las ventas que se vayan realizando
Ciclo = True
while Ciclo:  #Ciclo que permite repetir el menu para que se llenen todos los datos que quieran
   os.system("cls")
   print('\t', '***LAVADO DE AUTOS***', '\n')
   print('TIPO DE VEHICULO')
   print('1. Motocicleta Q. 15') 
   print('2. Automovil Q. 30')
   print('3. Camioneta Q. 50')
   print('4. Salir')
   TipoVehiculo = int(input('Ingrese el tipo de Vehiculo a lavar: ')) #Leer la opcion seleccionada del tipo de vehiculo

   if TipoVehiculo == 4: #Salir del programa
      sys.exit() 

   if TipoVehiculo > 0 and TipoVehiculo < 4:
      if TipoVehiculo == 1:
         Vehiculo = ('Motocicleta')
         Precio = 15 
      if TipoVehiculo == 2:
         Vehiculo = ('Automovil')
         Precio = 30  
      if TipoVehiculo == 3:
         Vehiculo = ('Camioneta') 
         Precio = 50 
         
      CicloCliente = True
      while CicloCliente: #Ciclo para elegir el tipo de cliente 
         os.system("cls")
         print('TIPO DE CLIENTE')
         print('1. Estandar')
         print('2. Miembro')
         TipoCliente = int(input('Ingrese el tipo de Cliente: ')) #Leer la opcion de Cliente seleccionada

         if TipoCliente >0 and TipoCliente < 3:
            if TipoCliente == 1:
               Cliente = ('Estandar')
            if TipoCliente == 2:
               Cliente = ('Miembro')

            os.system("cls")
            print('Indicar si es fin de semana', '\n', 'y = SI', '\n', 'n = NO') 
            FinD = input().lower() #Variable para indicar si es fin de semana o no

            if FinD == ('y'):
               FinSemana = True
            if FinD == ('n'):
               FinSemana = False
            
            CicloCliente = False #Cerrar el ciclo de seleccion de cliente
      
         else:
            print('Error', 'Ingrese un Valor Correcto')
            os.system("pause")

      #Calculos si es fin de semana y si es Miembro
      if FinD == ('n'):
         DescuentoF = Precio * 0.10
      if TipoCliente == 2:
         DescuentoM = Precio * 0.10
      if FinD == ('n') and TipoCliente == 2:
         Total = Precio - DescuentoF - DescuentoM
         Descuento = DescuentoF + DescuentoM
      if FinD == ('n') and TipoCliente == 1:
         Total = Precio - DescuentoF
         Descuento = DescuentoF
      if FinD == ('y') and TipoCliente == 2:
         Total = Precio - DescuentoM
         Descuento = DescuentoM
      if FinD == ('y') and TipoCliente == 1:
         Total = Precio
         Descuento = 0

      os.system("cls")
      print(f'Tipo: {Vehiculo}')
      print(f'Precio: {Precio}')
      print(f'Cliente: {Cliente}')
      print(f'Fin de Semana: {FinSemana}')
      print(f'Descuentos {Descuento}')
      print(f'Total: {Total}')
      os.system("pause") 

      Registro_Clientes = {} # Lista para guardar los datos de la venta
      Registro_Clientes['Tipo'] = Vehiculo #listado 1
      Registro_Clientes['Precio'] = Precio  #listado 2
      Registro_Clientes['Cliente'] = Cliente #listado 3
      Registro_Clientes['Fin De Semana'] = FinSemana #listado 4
      Registro_Clientes['Descuentos'] = Descuento #listado 5
      Registro_Clientes['Total'] = Total #listado 6
      base_de_datos.append(Registro_Clientes)  # Agregar datos a listado de registros   

      with open('base_de_datos.json', 'w') as archivo: # Para exportar datos a un Json
         json.dump(base_de_datos, archivo)        

   else:
      print('Error', 'Ingrese Un valor Correcto')
      os.system("pause")   