# Declara una variable de cada una de las siguientes estructuras de datos con al menos 3 elementos cada una:
# Las listas son colecciones ordenadas y mutables, que se pueden edidar facilmente.
lista = [1, 2, 3, 4]

# Las tuplas son colecciones ordenadas péro estas son inmutables, no se puede cambiar sus valores.
tupla = (100, 200, 300)

# Los sets son colecciones desordenadas de elementos únicos, no permite duplicados.
sets = {1, 2, 3, 4, 4, 4, 5}

# Los diccionarios son una coleccion de pares de claver-valor, accedes a los datos por clave unica.
diccionario = {"palindromo":"Palabra reversible","kilometros": 33, "Nombre": "Cristina"}


# 1). Muestra cada estructura usando Print() 

print("Esto es una lista:\n", lista)
print("Esto es una tupla:\n", tupla)
print("Esto es un set:\n", sets)
print("Esto es un diccionario:\n", diccionario)

#2). Acceder a elementos:
# Imprime el segundo elemento de la lista:

print(lista[1])

# Imprime una clave y su valor desde el diccionario:

print(diccionario["Nombre"])

# Explica por qué no puedes acceder por indice a un set:

    # No se puede acceder por medio de un indice a través de un set
    # por que solo admite elementos unicos y no acepta duplicados.

#3). Contar e Iterar:

# Usa len() para mostrar la cantidad de elementos en cada estructuras:

print(len(lista))
print(len(tupla))
print(len(sets))
print(len(diccionario))

#4). Modificar estructuras:

# Agrega un nuevo elemento a la lista y conjunto:
lista.append(5)
sets.append(6)

# Borra un elemento de una lista:
lista.remove(2)

#Agrega una nueva clave al diccionario:
diccionario["Nombre"] = "Pelusa"

# intenta modificar la tupla:
tupla[0] = 500

# El Error que muestra es el siguiente:
#
#   Traceback (most recent call last):
#       File "c:\Users\jesus\Desktop\actividad_m3_l5\estructuras.py", line 50, in <module>
#       tupla[0] = 500
#        ~~~~~^^^
#   TypeError: 'tuple' object does not support item assignment