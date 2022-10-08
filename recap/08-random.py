import random
import time
#El mòdulo random tiene varias funciones pra trabajar con nùmeros aleatorios.
#La funciòn choice es una las màs usadas eligiendo un elemento al azar desde una lista

fruits = ['manzana','pera','frutillas','piña']

#Imprimir una fruta al azar
print('redoble de tambores....')

for i in range(1,4):
    print("..")
    time.sleep(0.5)

    print('Tu fruta es:')
    print(random.choice(fruits))