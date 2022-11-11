#WHILE 
print("--------------------------WHILE--------------------------")
i = 0

while i <= 10:
    print(i)
    #i= i + 1
    i += 1

#WHILE BREAK
print("--------------------------BREAK----------------------")
i = 0

while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1

#WHILE CONTINUE
print("------------------------CONTINUE----------------------------")
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
print("----------------------EJERCICIO 1----------------------")
i = 1 

while i <= 50:
    i += 2
    print(i)

print("-----------------EJERCICIO 2---------------------")
i = 0
while i <=20:
    i += 2
    if i == 10:
        continue
    print(i)

print("------------------EJERCICIO 3--------------------")
i = 5
while i <= 30:
    print(i)
    if i == 15:
        break
    i += 5

#FOR LOOP
print("--------------FOR LOOP-----------------")
personas =["Juan", "Pedro", "Maria"]
for persona in personas:
    print(persona)

frutas = ["pera", "manzana", "banana", "fresas"]
for fruta in frutas:
    if fruta == "banana":
        break
    print(fruta)

print("-----------------otro ejercicio----------")
frutas = ["pera", "manzana", "banana", "fresas"]
for fruta in frutas:
    if fruta == "banana":
        continue
    print(fruta)

#crear un ciclo for que realice el recorrido de 10 personas 

print("------------------ejercicio en clase---------------------------")
personas = ["Juan", "Pedro", "Mateo", "Carla", "Sofia", "Nathaly", "Charly","Daniel", "Emilio", "Santiago"]
for persona in personas:
    print(persona)
