### conditional ###

my_condition = True
if my_condition:
    print("Se ejecuta la condicion del if")

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condicion del segundo if")

# aca debe cumplir 2 condiciones 
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto a 25")

print("La ejecucion continua")

my_string = "mi cadena de texto"

if my_string:
    print("Mi cadena de texto no es vacia")


if my_string == "mi cadena de textooooo":
    print("mis cadenas de texto")

my_string_dos = ""
if not my_string_dos:
    print("Mi Cadena de texto es vacia")