#Crear una funciòn que sume todos los numeros n

def sum_up_to(n):
    acc = 0
    print("##########")
    for number in range(1,n + 1):
        acc += number
    print("La suma es:", acc)        


sum_up_to(20)