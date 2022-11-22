inversion = float(input("Cual es la cantidad que va a invertir: "))
interes = float(input("Cual es el interes anual: "))
anios = int(input("Por cuantos anios sera: "))
print("Capital final: " + str(round(inversion * (interes / 100 + 1) ** anios, 2)))