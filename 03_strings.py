#Los strings son cadenas de letras
#Se pueden hacer "" o '

str_one ="Micro"
str_two = 'System'

#Juntaruno o màs strings se denomina concatenar.En python se puede concatenar ultilizando el operador '+'
print(str_one + str_two)

# Ojo con la ',' la funciòn print NO
#concatena
print(str_one, str_two)

#podemos tambièn multiplicar un string con un int

print('Hello'*3)

str_three ='Bye'

result = str_three * 5

print(result)

#Existe la funcion len() que nos entrga el largo de un string
#Numero de caracteres
print(len(result))
