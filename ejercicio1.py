print("\n Ejercicio N°1 \n")

# Obtener tres valores numéricos válidos del usuario
valor1 = float(input("Ingrese el primer valor: "))
valor2 = float(input("Ingrese el segundo valor: "))
valor3 = float(input("Ingrese el tercer valor: "))

# Inicializar variables para el orden
menor = valor1
intermedio = valor2
mayor = valor3

# Comparar y reordenar los valores
if valor2 < menor:
    menor, intermedio = valor2, menor
if valor3 < menor:
    menor, intermedio, mayor = valor3, menor, intermedio
if valor3 > mayor:
    intermedio, mayor = mayor, valor3
if valor2 > mayor:
    intermedio, mayor = valor2, mayor

# Mostrar los valores ordenados de menor a mayor
print("====================================================")
print("\n Valores ordenados de menor a mayor: \n")
print(menor)
print(intermedio)
print(mayor)