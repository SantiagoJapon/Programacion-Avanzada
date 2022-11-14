print("---------Este es el ejercicio 1----------------------")
def multiplicar(a,b):
    if b == 0:
        return 0
    elif b == 1:
        return a 
    else:
        return a + multiplicar(a, b - 1)

if __name__ == "__main__":
    resulado = multiplicar(2, 5)
    print(resulado)

print("---------este es el ejercicio 2------")
texto = "santiago japon"

texto_invertido = "".join(reversed(texto))

print(texto)
print(texto_invertido)

print("-------ejercicio 3-------")
lista = []
cantidad = int(input("Cantidad: "))
mayor = 0 
menor = 0
i = 1
while(cantidad > 0):
    numero = float(input("Numero #" + str(i) + ": "))
    lista.append(numero)
    i = i + 1 
    cantidad = cantidad - 1 
mayor = max(lista)
menor = min(lista)

print("Lista: ", lista)
print("Mayor: ", mayor)
print("Menor: ", menor)


print("----------------este es el ejercicio 4-------")
radio = float(input("radio: "))
pi = 3.1416
volumen = 4/3 * pi * (radio * radio * radio)
print(f'{volumen} m')


print("---------ejercicio 5-----")
edad = int(input("edad: "))
if(edad > 18):
    print("tiene la mayoria de edad")
else:
    print("no tiene la mayoria de edad")

print("---------ejercicio 6-------")
numero = 4
resta = numero%2
condicion = resta == 0
print(condicion)


print("=========ejercicio7=========")
def obtener_vocales(palabra):
    vocales = "aeiouAEIOU"
    return set([c for c in palabra if c in vocales])
texto = "zorro"
print(obtener_vocales(texto))


print("======ejercicio8===========")
def sumaDigitos(num):
    s = 0 
    while num > 0:
        s = s + num % 10
        num = num // 10
    return s

n = int(input("cantidad de numeros: "))
suma = 0
while n > 0:
    num = int(input("numero: "))
    suma = suma + sumaDigitos(num)
    n = n - 1
print(suma)


print("========ejercicio9=========")


print("==========ejercicio10=========")
print("ingrese los numeros: ", end = "")
numeros = list(map(int, input().split()))
print(numeros)
numeros.sort()
print(numeros)
numeros.reverse()


print("========ejercicio 11=====")
i = 0

while i <= 10:
    print(i)
    #i= i + 1
    i += 1

print("=======ejercicio12======")

print("===========ejercicio 13=========")

print("======ejercicio 14===========")
libros = ["Harry Potter", "Alicia en el pais de las maravillas"]
autores = ["J. K. Rowling", "Lewis Carroll"]
print(list(libros, autores))

print("========ejercicio 15========")
numero1 = int(input("ingrese el primer valor: "))
numero2 = int(input("ingrese el segundo valor: "))

if(numero1 > numero2 or numero2 > numero1):
    print("este numero es mayor")
else:
    print("este numero es menor")

print("==============ejercicio 16===")
tupla = (13, 1, 8, 3, 2, 5, 8)
Lista = list(tupla)
print(list)

print("=========ejercicio 17====")
def potencia(base, exponente):
    resultado = 1
    for i in range(exponente):
        resultado *= base
    return resultado
print(potencia(2,3))


print("=============ejercicio18========")
suma1 = int(input("ingrese numero: "))
suma2 = int(input("ingrese numero: "))
resultado = suma1 + suma2
print("el resultado es: ", resultado)


print("====ejercicio19=======")
A = int(input("ingrese el numero de cinco cifras: "))
c5 = A % 10
c4 = int((A%10)/10)
c3 = int((A%100)/100)
c2 = int((A%1000)/1000)
c1 = int(A - (A%10000)/1000)

print(str(c5)+ str(c4)+str(c3)+str(c2)+str(c1))

print("==============ejercicio 20 ============")
def saludo(nombre):
    print("Hola, {}, bienvenid@, soy Santiago".format(nombre))
    print("Estoy feliz de que estes aqui")
    print("Vuelve pronto <3")
    return None
nom_persona = input("Introduce tu nombre: ")
saludo(nom_persona)