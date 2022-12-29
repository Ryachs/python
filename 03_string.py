### String ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

# calcular largo de un string
print(len(my_string))
print(len(my_other_string))

# sumar string
print(my_string + my_other_string)
print(my_other_string + ' ' + my_string)

# salto de linea
my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

# string con tabulacion
my_new_tab_string = "\tEste es un string con tabulacion"
print(my_new_tab_string)

# string con tabulacion
my_scape_string = "\tEste es un string \n escapado"
print(my_scape_string)

# Formateo

# %s: string
# %d: integer
# %f: float

name, lastname, age = 'Reinaldo', 'Chavez', 30
# format utiliza {}
print('Mi nombre es {} {} y mi edad es {}'.format( name, lastname, age ))
# % utiliza %s o %d en este caso!
print('Mi nombre es %s %s y mi edad es %d' %( name, lastname, age ))
# forma normal
print('Mi nombre es ' + name + ' ' + lastname + ' y mi edad es ' + str( age ))
# formatiando el texto con f
print(f'Mi nombre es { name } { lastname } y mi edad es { age }')


# Desempaquetado de caracteres
language = 'python'
a, b, c, d, e, f = language
print(a)
print(b)

# División
language_slide = language[1:3]
# 0-1-2-3-4-5
# p-y-t-h-o-n
print(language_slide)

language_slide = language[1:]
# 0-1-2-3-4-5
# p-y-t-h-o-n
print(language_slide)

language_slide = language[-2]
# 0-1-2-3-4-5
# p-y-t-h-o-n
print(language_slide)

# reverse
reversed_language = language[::-1]
print(reversed_language)

# Funciones
# pone la primera letra en mayuscula
print(language.capitalize())
# pone todo en mayusculas
print(language.upper())
# cuenta las veces que sale el valor ingresado
print(language.count('t'))
# valida si es numerico
print(language.isnumeric())
print('1'.isnumeric())
# pone todo en minusculas
print(language.lower())
# lo transformamos en minusculas y luego comprobamos si esta en minusculas
print(language.lower().islower())
print(language.upper().islower())
# valida si la palabra comienza con py
print(language.startswith('py'))
