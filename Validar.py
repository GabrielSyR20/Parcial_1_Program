def es_entero(valor_int): # Verifica si el valor es un entero
    if type(valor_int) == int:
        return True
    
    if valor_int == "":
        return False
    
    if type(valor_int) == str and valor_int.isdigit():
        return True
    
    return False

def notas_validas(notas): # Verifica si las notas están en el rango válido
    if notas >= 1 and notas <= 10:
        return True
    else:
        return False