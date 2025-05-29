def es_entero(valor_int):
    if type(valor_int) == int:
        return True
    
    if valor_int == "":
        return False
    
    if type(valor_int) == str and valor_int.isdigit():
        return True
    
    return False

def notas_validas(notas):
    if notas >= 1 and notas <= 10:
        return True
    else:
        return False