x = 6
y = 2
z = 7

print(f"{x}+{y} es igual a {x+y}")
print(f"{x}-{y} es igual a {x-y}")
print(f"{x}*{y} es igual a {x*y}")
print(f"{x}/{y} es igual a {x/y}")

#División al piso = si es decimal lo lleva a entero hacia abajo
print(f"{z} dividido al piso de {y} es igual a {z//y}")
#El módulo = al resto de una operación
print(f"{z} modulo de {y} es igual a {z%y}")
#La potencia = cuando ponemos un número al cuadrado o al cubo
print(f"{x} elevado a la {y} es igual a {x**y}")
print(f"{x} elevado a la {3} es igual a {x**3}")
print(f"la raiz cuadrada de {x} es {x**0.5}")

num1 = round(13/2,0)
print(num1)
print(type(num1))
###EXAMEN###
dividendo = 874
divisor = 27
print(f"el cociente de los siguientes dos números: {dividendo} dividido entre {divisor} es {dividendo//divisor}.")

dividendo = 456
divisor = 33
resultado = dividendo%2
print(f"{resultado}")

raiz_cuadrada = 783
resultado = raiz_cuadrada**0.5
print(f"{resultado}")