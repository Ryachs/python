### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
# python permite mezclar While con if y else (son opcionales)
if my_condition == 10: # recordar que cuenta las repeticiones no el numero 10 como tal 0 - 10
    print("Mi condicion es igual a 10")
else:
    print("Mi condicion es igual o mayor a 10")

print("La ejecucion a terminado")


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condicion es 15")
        print("Se detuvo la ejecucion -", my_condition)
        break
    
    print("Mi condicion es menor que 20 -", my_condition)

print("La ejecucion Continua")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

# Tuple
my_tuple = (30, 1.75, "Reinaldo", "Chavez", "Concepcion")

for element in my_tuple:
    print(element)

# Set
my_set = {"Reinaldo", "Chavez", 30}

for element in my_set:
    print(element)

# Dict
my_dict = {
    "Nombre":"Reinaldo", 
    "Apellido":"Chavez", 
    "Edad": 30
}
# solo imprime las key del dictionary
for element in my_dict:
    print(element)

my_dicts = {
    "Nombre":"Isaac", 
    "Apellido":"Chavez", 
    "Edad": 20
}
# de esta forma imprime solo los values del dictionary
for element in my_dicts.values():
    print(element)
else:
    print("El bucle for para mi diccionario a finalizado")

my_doc = {
    "Nombre":"Ares", 
    "Tipo":"Perro", 
    "Edad": 4
}
# break
for element in my_doc:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle for para mi diccionario de mascotas a finalizado")

print("La ejecucion continua")

# continue
for element in my_doc:
    print(element)
    if element == "Edad":
        continue
else:
    print("El bucle for para mi diccionario de mascotas a finalizado")

print("La ejecucion continua 2")