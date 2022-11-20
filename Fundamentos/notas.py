#pedor una nota al usuario si la nota es menor a 10 o menor o igual a 9 imprimir excelete
#si la nota es menor a 9 y mayor o igual a 8, impirmir muy buineo
#si la nota es menor a 8 y mayor o igual a 7, imprimir bueno
#si la nota es menor a 7 imprimir reprobado
nota = int(input("Ingresa tu nota: "))
def rangoNota(int: nota):
    global nota
    if nota < 10 or nota >= 9:
        print("Tu nota es excelente")
    if nota < 9 or nota >= 8:
        print("Tus notas son muy buenas")
    if nota < 8 or nota >=7:
        print("Tus notas son buenas")
    if nota < 7:
        print("Lamentablemente estas reprobado")
if nota > 10:
    print("esta nota no esta en el rango")
