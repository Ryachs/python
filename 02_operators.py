### Operadores ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 2) # Operador de modulo (saber si hay un multiplo - devuelve el resto de la operacion)
print(10 % 3) # Deberia devolver un 1 (10 / 3 = 1)
print(10 // 3) # flor division
print(2 ** 3) # 2 elevado a 3

print("Hola" + " Python" + " ¿Que tal?")
print("Hola " + str(5))
print("Hola " * (2 ** 3))

### Operadores Comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print(3 > 4 == 2)

print("----------------")

print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Zola")    # Ordenacion alfabetica
print(len("aaaa") >= len("abaa")) # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")


### Operadores Logicos ###

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(not (3 > 4)) # Negamos la condicion
