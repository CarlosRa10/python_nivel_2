x = 10
y = 5
z = x + y
print("Mis números son " + str(x) + " y " + str(y))#Se hizo conversiones y concatenaciones.. no es nada practico
print("Mis números son {} y {}".format(x,y))#Funcion format
print(f"Mis números son {x} y {y}")#Formato literal
print("La suma de {} y {} es igual a {}".format(x,y,z))#Funcion format

color = "rojo"
matricula = 54123

print(f"El auto es {color} y su matrícula es {matricula}")

nombre = "Carlos"
edad = 24
cadena_concatenada = nombre + " tiene " + str(edad) + " años."
print(cadena_concatenada)

nombre = "Carlos"
edad = 24
print(nombre, "tiene", edad, "años.")

num_int = 10
print(type(num_int))
print("Esto es un numero entero ",num_int) #Esto agarrara porque hay un "," y automaticamente lo convierte en string
#print("Esto es un numero entero "+num_int)#Esto no agarra porque no puedes concatenar un string con otro tipo de dato, es necesario hacer un casting
###EXAMEN###
nombre_asociado = "Carlos Ramirez"
numero_asociado = 102030
print(f"Estimado/a {nombre_asociado}, su número asociado es: {numero_asociado}")

puntos_nuevos = 100
puntos_totales =200
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")

puntos_anteriores = 100
puntos_nuevos = 250
puntos_totales = puntos_anteriores + puntos_nuevos
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")
