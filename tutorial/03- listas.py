import math
squares = [1,4,9,16,25]

# Desafio: A partir del arreglo anterior crear uno que tenga sus raices
# root == 'raìz
roots = []

for number in squares:
    roots.append(int(math.sqrt(number)))

print(roots)


# roots = [1,2,3,4,5]


## sqrt: square o raiz cuadrada
## root:rt

## append: agrega al final

## reemplazar algùn elemento del arreglo segùn el ìndice
roots[4] = 6

print(roots)