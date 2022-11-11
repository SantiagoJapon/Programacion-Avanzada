#WHILE 
print("WHILE")
i = 0

while i <= 10:
    print(i)
    #i= i + 1
    i += 1

#WHILE BREAK
print("BREAK")
i = 0

while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1

#WHILE CONTINUE
print("CONTINUE")
i = 0

while i <= 20:
    i += 1
    if i == 10:
        continue
    print(i)

"""
Calcular los primeros 50 numeros impares.

Calcular los primeros 20 numeros pares, pero retirar el 10

calcular los multiplos de 5 pero detener la ejecucion en el tercero
"""
print("EJERCICIO 1")
i = 1 

while i <= 50:
    i += 2
    print(i)

print("EJERCICIO 2")
i = 0
while i <=20:
    i += 2
    if i == 10:
        continue
    print(i)

print("EJERCICIO 3")
i = 5
while i <= 30:
    print(i)
    if i == 15:
        break
    i += 5