import os
from collections import deque
print ('ingrese la ruta de la carpeta en la que quiere listar sus archivos')
ruta = input()
# definir la cola
cola = deque()
# en listar los nombres de los archivos 
files=os.listdir(ruta)
for file in files:
  cola.append(file) #agregar los nombre de los archivos a la cola 
while len(cola) > 0:
    # extraer el primer elemento en la cola
    siguiente_elemento = cola.popleft()

    print(f'Siguiente elemento: {siguiente_elemento}')
    print(f'Cola de impresión: {cola}')
    print("#########")

    ##vivos que tenemos que terminarlo