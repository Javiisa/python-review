#Las funciones pueden tener paràmetros por defectos

def say_country(country = "Chile"):
    print("Hola soy de", country)

say_country('Bolovia')
say_country('Perù')
say_country('Colombia')
say_country()
