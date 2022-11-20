nota = int(input("Ingresa tu nota: "))
def rangoNota(int: nota):
    global nota
    if nota == 10:
        print("tu no es excelente")
    elif nota >= 9:
        print("tu nota es excelente")

