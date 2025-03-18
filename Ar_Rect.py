base = float(input("Ingresar base: "))
altura = float(input("Ingresar Altura: "))

def calcular_area (base,altura):
    return base * altura

resultado = calcular_area(base,altura)
print("El resultado del área del rectángulo es: ", resultado)

# En este caso realizaremos la prueba al código realizado anterioremente 
#Arrange
#Defininimos que testearemos la función llamada calcular_area.

import unittest
# Act - Acción
def test_area():
    print('test passed')
    # Enviamos a la función calcular_area los valores 4 y 5 
    assert calcular_area(4,5) == 20
test_area()