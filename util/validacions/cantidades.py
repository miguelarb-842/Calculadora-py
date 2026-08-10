from util.utlidades import (borrar_pantalla,Esperar_tecla)

def cantidadVali(Valor:int)->bool:
    """Valida si la cantidad es valida.
    
    Args:
        valor: se ingresa el valor a ser evaludado.

    Returns:
        True cuando se ingresa un valor invalido.
        False cuando el valor que se ingresa es correcto.
    """
    if Valor == 0:
        print("\nEste valor no puede ser 0")
        Esperar_tecla()
        borrar_pantalla()
        return True
    
    if  Valor <= 0:
        print("\nDebe ser un entero positivo.")
        Esperar_tecla()
        borrar_pantalla()
        return True
        
    if Valor == 1:
        print("\nNo se puede sumar solamente un numero")
        Esperar_tecla()
        borrar_pantalla()
        return True
    
    return False
