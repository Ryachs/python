### Tuples ###

# formas de definirlas
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.75, 'Reinaldo', 'Chavez')
my_other_tuple = (35, 60, 30)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) # indexError (sobrepasa la tupla)
#print(my_tuple[-6]) # indexError (sobrepasa la tupla)

# Cuenta cuantas veces se encuentra un valor
print(my_tuple.count("Reinaldo"))
# Nos muestra el indice (posicion) del elemento 
print(my_tuple.index("Reinaldo")) # indice 2
print(my_tuple.index("Chavez")) # indice 3

# LAS TUPLAS SON INMUTABLES
#my_tuple[1] = 1.90 # Error - no se puede cambiar los valores ni agregar nuevos 


print(my_tuple + my_other_tuple)

my_sum_tuple = my_tuple + my_other_tuple

print(my_sum_tuple)

# imprime los elementos de la posicion 3 al 6
# 0,  1,    2,          3,        4,  5,  6
# 35, 1.75, 'Reinaldo', 'Chavez', 35, 60, 30
# Imprime: Chavez, 35, 60
print(my_sum_tuple[3:6])

# Agregamos valores cambiando la tupla por una lista momentaniamente
my_tuple = list(my_tuple)
print(type(my_tuple))
my_tuple[3] = "DEVPYTHON"
my_tuple.insert(1, "Azul")

my_tuple = tuple(my_tuple)
print(type(my_tuple))
print(my_tuple)

# Borrar una tupla - elimina la variable
del my_tuple
print(my_tuple) # NameError: name 'my_tuple' is not defined