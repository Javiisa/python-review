# objetivo: Dibujar una lìnea diagonal en un cuadrado de 10*10

# El siguiente codigo imprime una mariz de 10x10
for i in range(1,11):
    line = ""
    for j in range(1,11):
        if(j == i):
            line += '*'
        else:
            line += "-"
    print(line)    