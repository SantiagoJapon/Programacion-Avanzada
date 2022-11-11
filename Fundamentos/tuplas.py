tuplas = ("hola mundo", "esto se conoce como", "tupla")
print(tuplas)
#las tuplas no se pueden modificar 
lista = list(tuplas)
print(type(lista))
lista.append("Santiago")
print(lista)
print(tuplas)