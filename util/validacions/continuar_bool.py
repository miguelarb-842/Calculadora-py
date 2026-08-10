from util.utlidades import(Esperar_tecla,borrar_pantalla)

def valSi_No() -> bool:
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