from .utlidades import(Esperar_tecla,borrar_pantalla)

def val_float(mensaje: str = "> ", min:int = None, max:int = None) -> float:
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
            
def valInt(mensaje:str, min:int = None, max:int = None)-> int:
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
                
                

def cantidadVali(Valor:int)->bool:
    if Valor == 0:
        print("\nEste valor no puede ser 0")
        Esperar_tecla()
        borrar_pantalla()
        return True
    
    elif Valor <= 0:
        print("\nDebe ser un entero positivo.")
        Esperar_tecla()
        borrar_pantalla()
        return True
        
    elif Valor == 1:
        print("\nNo se puede sumar solamente un numero")
        Esperar_tecla()
        borrar_pantalla()
        return True
    
    else:
        return False


    
    
def continuar(num: float) -> bool:
    while True:
        print(f"\nEl resultado es: {num}")
        print("¿Deseas continuar con otra operación?\n")

        Desear = input("[S/N] -> ").strip().lower()

        if Desear == "s":
            return True
        
        elif Desear == "n":
            borrar_pantalla()
            print("Entendido, se salio del programa correctamente...")
            print("¡Esperamos verte pronto!")
            return False
        
        else:
            print("Entrada no válida, únicamente se permiten 'S' o 'N'.")
            borrar_pantalla()
            Esperar_tecla()
            
def continuar_chicharonera() ->bool:
     while True:
        print("\n¿Deseas continuar con otra operación?\n")
    
        Desear = input("[S/N] -> ").strip().lower()
    
        if Desear == "s":
                return True
            
        elif Desear == "n":
            borrar_pantalla()
            print("Entendido, se salio del programa correctamente...")
            print("¡Esperamos verte pronto!")
            return False
            
        else:
            print("Entrada no válida, únicamente se permiten 'S' o 'N'.")
            borrar_pantalla()
            Esperar_tecla()
                
    