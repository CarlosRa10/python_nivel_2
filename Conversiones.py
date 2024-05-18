#Conversiones Implicita
num1 = 20
num2 = 10.5

print(type(num1))
print(type(num2))

num1 = num1 + num2
print(num1)

print(type(num1))
print(type(num2))

#Conversiones Explicitas
num1 = 10.5
print(num1)
print(type(num1))

num2 = int(num1)#Forzosamente elimino los decimales
print(num2)
print(type(num2))

edad = input("Dime tu edad: ")
print(type(edad))
edad = int(edad)
print(type(edad))
nueva_edad = 1 + edad
print(nueva_edad)
#print("Tu nueva edad es " + nueva_edad) #No puede concatenar y mucho menos sumar
###EXAMEN###
num1 = 1.5
num1 = int(num1)
print(type(num1))

num1 = 10
num1 = float(num1)
print(type(num1))

num1 = 10
num2 = 8.5
print(num1 + num2)
print(float(num1) + int(num2))

#En lugar escribir 
var = 10
var = float(var)
print("Numero flotante: " + str(var))
#Escribes solo
Var = 10
print("Numero flotante:", float(var))