from .utlidades import(Esperar_tecla,borrar_pantalla)

def Esnumero(mensaje: str = "> ") -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese solo números.")

def CantidadVali(Valor:int)->bool:
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


    
    
def CONTINUAR(num: float) -> bool:
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
            
def CONTINUAR_CHICHARONERA() ->bool:
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
                
    