#Programa que calcule la comision de sus ventas totales
#Su nombre y cuanto han vendido este mes
#Ok Carlos. Este mes ganaste tanto
#necesitas inputs, calcular comisiones del monto * comision / 100

nombre = input("Ingrese su nombre: ")
ventas = float(input("Cuanto has vendido este mes: "))
comision = round(ventas * 13 / 100,2)
print(type(ventas))

print(f"Ok {nombre}. Este mes ganaste {comision}$")
