import time
#Este programa ayuda a saber si podemos hacer un triàngulo
#dadas tres longitudes

print("hola.te voy a ayudar con eso de los triangulos")
l1 = int(input("Ingresa la longitud uno\n"))
l2 = int(input("Ingresa la longitud dos\n"))
l3 = int(input("Ingresa la longitud tres\n"))

print("Las longitudes entregadas hasta el numero son!")

print(l1,l2,l3)

if(l1 <= l2+l3):
    print("vamos bien,revisemos los otros casos")
    time.sleep(0.5)
    if(l2 <= l1+l3):
        print("seguimos bien,veamos el tercero")
        time.sleep(0.5)
        if(l3 <=l2+l3):
            print("si es posible el triàngulo")
        else:
            print("No es posible el triangulo")
    else:
        print("No es posible el triàngulo")
else:
    print("No es posible el triàngulo",l1,"No es menor que", l2, "+", l3)

