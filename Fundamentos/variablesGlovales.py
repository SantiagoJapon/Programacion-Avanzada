salario = int(input("Hola, por favro ingresa tu salario: "))

def calcularSalario(int: salario):
    global salario
    #salario = 300
    seguro = 50
    salarioTotal = salario - seguro
    return salarioTotal

print(calcularSalario(salario))
