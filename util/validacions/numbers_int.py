from util.utlidades import borrar_pantalla

def valInt(mensaje:str, min:int = None, max:int = None)-> int:
    """Solicita al usuario un numero entero por teclado y lo valida.

    Repite la solicitud hasta recibir un entero valido, opcionalmente
    dentro de un rango minimo y/o maximo.

    Args:
        mensaje: Texto que se muestra al solicitar el numero.
        min: Valor minimo aceptado (inclusive). Si es None, no hay limite inferior.
        max: Valor maximo aceptado (inclusive). Si es None, no hay limite superior.

    Returns:
        int: El numero entero ingresado por el usuario que cumple
        con las restricciones indicadas.
    """
    num:int;
    while(True):
        try:
            num = int(input(mensaje));
            
            if(min is None and max is None):
                return num;
            
            if(min is None):
                if(num <= max):
                    return num;
                print(f"\n\tERROR: El numero debe ser menor o igual a {max}\n");
                continue;
            
            if(max is None):
                if(num >= min):
                    return num;
                borrar_pantalla();
                print(f"\n\tERROR: El numero debe ser mayor o igual a {min}\n");
                continue;
            
            if(num >= min and num <= max):
                return num;
            print(f"\n\tERROR: El numero debe estar entre {min} y {max}")
        except Exception:
            print("\n\tERROR: solo puedes entrar letras.\n");
                