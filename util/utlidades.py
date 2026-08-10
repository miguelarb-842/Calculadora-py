import os
import time

def borrar_pantalla():
    """Limpia la pantalla de la terminal.

    Utiliza el comando 'cls' en sistemas Windows y 'clear'
    en el resto de sistemas operativos (Linux/Mac).
    """
    os.system("cls" if os.name == "nt" else "clear")
    
def Esperar_tecla(mensaje:str = "> Presione Enter para continuar..."):
    input(mensaje)
    """Pausa la ejecucion del programa
    
    Args:
        mensaje = Texto que se muestra antes de esperar la entrada
            del usuario. Por defecto pide presionar Enter.
    """
def desea_continuar(pregunta: str = "¿Desea realizar otra operación? (s/n): ") -> bool:
    """Pregunta al usuario si desea realizar otra operacion.

    Repite la pregunta hasta recibir una respuesta valida.

    Args:
        pregunta: Texto que se muestra al solicitar la respuesta.
            Por defecto pregunta si desea realizar otra operacion.

    Returns:
    
        True si el usuario respondio afirmativamente (s, si, sí),
        False si respondio negativamente (n, no).
        
        Encaso que no se reciva una respuesta valida el programa devuelve: 
            "Por favor, responda 's' o 'n'. 
    """
    while True:
        respuesta = input(pregunta).strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        elif respuesta in ("n", "no"):
            return False
        else:
            print("Por favor, responda 's' o 'n'.\n")
            Esperar_tecla()