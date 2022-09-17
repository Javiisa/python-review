# La funciòn principal para manejar archivos es open()
# Esta funciòn recibe dos paràmetros,el nombre del archivo y el modo
# Los mosdos son:

# r: para leer y da error si el archivo no existe
# a: `para realizar append (agregar al final`. Si el archivo no exirte,lo crea
# w: para escribir. Elimina el contenido anterior si existe.

file = open("file_handling/example.txt","r")

# A la funciòn read podemos pasar un nùmero y vaa imprimir esa cantidad de caracteres
print(file.read(54))

# Tambièn existe la funciòn readline() que lee lìnea por lìnea
print("Ejemplo de readline()")
print(file.readline())
print(file.readline())

# Debemos cerrar el archivo luego de usarlo
file.close()