def suma(a, b):
    try:
        # Convertir a float para verificar que el dato sea un número válido
        a = float(a)
        b = float(b)
        return a + b
    except ValueError:
        return "error"
