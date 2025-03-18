import unittest
base = float(input("Ingresar base: "))
altura = float(input("Ingresar Altura: "))

def calcular_area (base,altura):
    return base * altura

resultado = calcular_area(base,altura)

print("El resultado del área del rectángulo es: ", resultado)