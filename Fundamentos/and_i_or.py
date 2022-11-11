#La sentencia con AND solo se ejecuta si ambas variables son verdaderas AND
num1 = 2
num2 = 3
num3 = 4
if num1 < num2 and num2 < num3:
    print("esto se imprime si es verdadero1")
else:
    print("esto se imprime si es falso1")


#CONDICIONAL OR
#solo se ejecusi si al menos una de las condiciones es verdadera
num1 = 4
num2 = 5
num3 = 10
if num1 > num2 or num2 < num3:
    print("si es verdadero2")
else:
    print("si es falso2")

if num1 > num2 or num3 < num2:
    print("si es verdadero3")
else:
    print("si es falso3")



