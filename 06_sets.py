### Sets ###
# set es una palabra reservada como list, tuple
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {'Reinaldo', 'Chavez', 35} # al llenarlo con esta estructura se aplica el tipo de datos Set

print(my_other_set)
print(type(my_other_set)) # set

print(len(my_other_set))

my_other_set.add("Reydev")

print(my_other_set) # un set no es una estructura ordenada

my_other_set.add("Reydev") # un set no admite repetidos

print(my_other_set)

print("Reinaldo" in my_other_set) # Realiza busquedas true cuando existe false cuando no
print("Reynaldo" in my_other_set)

my_other_set.remove("Reydev") # Elimina un elemento
print(my_other_set)

my_other_set.clear() # Elimina los elementos del set
print(my_other_set)
print(len(my_other_set))

my_other_set = {'Reinaldo', 'Chavez', 35}

# del my_other_set # del esta asociado al sistema (elimina el elemento por completo hasta la variable)

# creamos una lista con el set
my_set = {"Reinaldo", "Alexis", 55}
my_list = list(my_set)
print(my_list)

print(my_list[0])

# unimos 2 set
my_other_set = {"Java", "Python", "JavaScript"}


my_new_set = my_set.union(my_other_set)

print(my_new_set)

# imprimimos los diferencias
print(my_new_set.difference(my_set))