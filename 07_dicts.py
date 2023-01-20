### Dictionaries ###

# formas de declarar un diccionario
my_dict = dict()
my_other_dict = []

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    "Nombre": "Reinaldo",
    "Apellido": "Chavez",
    "Edad": 30
}

print(my_other_dict)
print(type(my_other_dict)) # Ahora cambia a ,dict

my_dict = {
    "Nombre": "Reinaldo",
    "Apellido": "Chavez",
    "Edad": 30,
    "Lenguajes": {"Python", "Java"},
    1 : 1.75
}
print(my_other_dict)
print(my_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict["Nombre"]) # imprimimos uno de los elementos

my_dict["Nombre"] = "Alexis" # Modificamos un valor al diccionario

print(my_dict["Nombre"]) 
print(my_dict)

my_dict["Calle"] = "Calle Benavente" # Agregamos un valor al diccionario

print(my_dict)

del my_dict["Calle"] # eliminamos 1 elemento del diccionario
print(my_dict)

print("Reinaldo" in my_dict)
print("Nombre" in my_dict) # en los diccionarios se busca por clave no valor

print(my_dict.items()) # muestra las valores como items
print(my_dict.keys()) # muestra solo las keys del diccionario
print(my_dict.values()) # muestra solo los valores del diccionarios

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) # Crea un nuevo diccionario sin conservar los datos vinen como None

# desde una lista
my_list = ["Nombre", 1, "Piso", "Arenero"]
my_new_dict = dict.fromkeys((my_list))

print(my_new_dict)

print(my_dict.fromkeys(("Nombre", 1)))


my_new_dict = dict.fromkeys((my_dict)) # crea una copia del diccionario pero vacio solo contiene las claves
my_new_dict["Lenguajes"] = "Java" # le paso un valor
print(my_new_dict)


my_new_dict = dict.fromkeys(my_dict, {"Reinaldo, Chavez"}) 

print(my_new_dict)