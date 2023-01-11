# Variables

firstname = "Antonio"
my_last_name = "Gonzalez"
# Para utilizar una palabra reservada utilizar _
_if = "SI"
myEdad123 = 35

my_bool_variable = True

my_int_to_str_variable = str(myEdad123) # Casteamos de int a str

# Variables invalidas

# first-name
# first@name
# first$name
# num-1
# 1num

print(firstname)
print(myEdad123)
print(my_bool_variable)

# concatenar de variables en un print
print(firstname, my_last_name)

print(my_int_to_str_variable)
# Imprimimos el tipo de variable (str)
print(type(my_int_to_str_variable))


# Algunas funciones del sistema
print(len(my_last_name))

print("My name is:", firstname)
print("My last name is:", my_last_name)

# Variables en una sola linea. !!!No recomendable¡¡¡
name, surname, alias, age = "Alejandro", "Geek", "DEV", 33

print("Me Llamo:",name, surname,".Mi edad es:", age, ".Y mi alias es:", alias)


# Imput en Python (Descomentar para probar)
"""
firt_name = input("Cual es tu nombre: ")
age = input("Cuantos años tienes? ")
print(firt_name)
print(age) 
"""

# Cambiamos su tipo
name = 35
age = "Sebastian"

print(name)
print(age)

# Forzamos el tipo
address: str = "Mi direccion"
address = 32
print(address)
