### Lists ###

# listas: list('reinaldo','chavez')
# tuplas: tuple['reinaldo', 'chavez']
# diccionarios: dics{'reinaldo','chavez'}
# estos tipos de datos son similares !pero no son los mismos! 
# !!! cambian sus metodos y las acciones que permiten !!!!  

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [30, 24, 66, 55, 35, 54, 36]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.75, 'Reinaldo', 'Chavez']

print(my_other_list)
print(type(my_list))
print(type(my_other_list))
# accedemos al dato en posicion 0 (35)
print(my_other_list[0])
print(my_other_list[1])
# da la vuelta a la lista
#  1,   2,        3,         4,       -4,  -3,     -2,          -1
# [35, 1.75, 'Reinaldo', 'Chavez'] - [35, 1.75, 'Reinaldo', 'Chavez']
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list[-4])
# len cuenta los elementos de una lista { retorna un 4 }
print(len(my_other_list))
# count retorna el numero de ocurrencias de un valor
print(my_other_list.count('Reinaldo'))
# count valida la variable exacta en este caso nos entrega un 0
print(my_other_list.count('reinaldo'))
#print(my_other_list[-5]) indexError
#print(my_other_list[4]) indexError

age, height, name, lastname = my_other_list
print(name)

print(my_list + my_other_list)

# en python se puede cambiar el tipo de dato solo cambiando el tipo de asignación
# cambiamos my_list <list> a <str>
#my_list = "Hola Python"
print(my_list)
print(type( my_list ))

# añadir un nueva elemento a una lista
my_other_list.append('ReiDevs')
print(my_other_list)

# insert en lista python {posicion, valor a insertar}
my_other_list.insert(1, 'Rojo')
print(my_other_list)

# eleminar un valor de una lista
# solo elimina un elemento (si hay mas de un elemento con el valor seteado solo eliminara el primero)
# el elemento debe ser conocido
my_other_list.remove('Rojo')
print(my_other_list)

# quita un elemento de la lista
print(my_list.pop(2))
my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

# elimina por el indice del elemento {en este caso 2}
del my_list[2]
print(my_list)

my_new_list = my_list.copy()

# limpia una lista
my_list.clear()
print(my_list)
print(my_new_list)

# reverse list
my_new_list.reverse()
print(my_new_list)

# ordenar una lista
my_new_list.sort()
print(my_new_list)
