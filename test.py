import pytest
from calc import suma

def test_suma_numeros():
    # Prueba 1: suma de dos números enteros
    assert suma(2, 3) == 5

    # Prueba 2: suma de dos números decimales
    assert suma(2.5, 3.5) == 6.0

    # Prueba 3: suma de número entero y número decimal
    assert suma(2, 3.5) == 5.5

    # Prueba 4: manejo de error al recibir un texto
    assert suma(2, "texto") == "error"
