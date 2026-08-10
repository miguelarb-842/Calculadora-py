import util.validacions as vl

def ingresarNumeros(mensaje1:str, mensaje2:str)-> tuple[float, float]:
    """Solicita al usuario dos numeros decimales por teclado.

    Args:
        mensaje1: Texto que se muestra al solicitar el primer numero.
        mensaje2: Texto que se muestra al solicitar el segundo numero.

    Returns:
        tuple[float, float]: Una tupla con los dos numeros ingresados,
        en el orden (num1, num2).
    """
    num1 = vl.val_float(mensaje1);
    num2 = vl.val_float(mensaje2);
    
    return num1, num2;