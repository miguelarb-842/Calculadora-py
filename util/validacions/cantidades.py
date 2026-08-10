from util.utlidades import (borrar_pantalla,Esperar_tecla)

def cantidadVali(Valor:int)->bool:
    
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
