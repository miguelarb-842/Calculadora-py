from util.utlidades import borrar_pantalla

def val_float(mensaje: str = "> ", min:int = None, max:int = None) -> float:
    """Solicita al usuario un numero decimal por teclado y lo valida.

    Repite la solicitud hasta recibir un float valido, opcionalmente
    dentro de un rango minimo y/o maximo.

    Args:
        mensaje: Texto que se muestra al solicitar el numero.
        min: Valor minimo aceptado (inclusive). Si es None, no hay limite inferior.
        max: Valor maximo aceptado (inclusive). Si es None, no hay limite superior.

    Returns:
        float: El numero decimal ingresado por el usuario que cumple
        con las restricciones indicadas.
    """
    num:float;
    while True:
        try:
            num = float(input(mensaje));
            
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
        except ValueError:
            print("Entrada no válida. Por favor, ingrese solo números.")