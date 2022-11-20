#crear una funcion que nos permita conocer el rango de edad de una persona
nombre = input("Dime tu nombre: ")
print(type(nombre))
edad = int(input("Ahora dime tu edad: "))


def edadCalcular(edad, nombre):
    
    if edad >= 18 and edad <= 65:
        print(nombre, "es mayor de edad")
    elif edad >= 65:
        print(nombre, "usted es parte de la tercera edad")
    else:
        print(nombre, "es menor de edad")
edadCalcular(edad)
