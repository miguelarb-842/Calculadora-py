from util.utlidades import(Esperar_tecla,borrar_pantalla)

def valSi_No() -> bool:
    """Ejecuta un bucle hasta que se reciba un valor valido para saber si el usuario 
        desea volver a realizar una operacion matematica.

    Returns:
        True cuando el usuario ingrea "s" o "S".
        En ese caso el usuario desea realizar otra operacion matematica
        
        False cuano el usuario ingresa "n" o "N"
        En ese caso el usuario no sea volver a realizar otra operacion matematica
        
        En caso que no se reciba un valor valido se mostrara:
            "Entrada no válida, únicamente se permiten 'S' o 'N'."
    """
    while True:
        
        print("\n\t ¿Desea volver a hacer otra operacion?")

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