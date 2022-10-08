#Crea un arreglo de 1 al 10
#E imprime solo los elementos pares
numbers = [1,2,3,4,5,6,7,8,9,10]
print("solo numeros pares")
for number in numbers:
    if number % 2 == 0:
        print(number)
    
print("solo numeros inpares")
for number in numbers:
    if number % 2 != 0:
        print(number)
