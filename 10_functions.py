### Functions ###

# definir una funcion
def my_function():
    print("Esto es una funcion")

my_function()

def sum_two_values(first_number, second_number):
    print(first_number + second_number)

sum_two_values(5, 9)
sum_two_values(5698, 9548)
sum_two_values("5", "9")
sum_two_values(1.4, 5.2)

def sum_two_values_with_return(first_number, second_number):
    my_sum = first_number + second_number
    return my_sum


my_return = sum_two_values_with_return(14, 58)
print(my_return)

# la f se utiliza para dar formato al texto
def print_name(name, surname):
    print(f"{ name } { surname }")

print_name("Reinaldo", "Chavez")

def print_name(name, surname):
    print(f"{ name } { surname }")

print_name(surname = "Chavez", name = "Reinaldo")

# asignar un valor por defecto
def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{ name } { surname } { alias }")


print_name_with_default("Reinaldo", "Chavez", "ale")

# Sin alias (muestra el alias por defecto) 
print_name_with_default("Reinaldo", "Chavez")


def print_texts(*text):
    print(text)

print_texts("Hola", "desde", "python")

def print_texts(*texts):
    for text in texts:
        print(text)
    print(text)

print_texts("Hola", "desde", "python")

# Los paso a mayusculas
def print_texts(*texts):
    for text in texts:
        print(text.upper())
    print(text)

print_texts("Hola", "desde", "python")