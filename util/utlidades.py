import os
import time

def borrar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperar(segundos: float):
    time.sleep(segundos)

def Esperar_tecla(mensaje:str = "> Presione Enter para continuar..."):
    input(mensaje)
    
def desea_continuar(pregunta: str = "¿Desea realizar otra operación? (s/n): ") -> bool:
    while True:
        respuesta = input(pregunta).strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        elif respuesta in ("n", "no"):
            return False
        else:
            print("Por favor, responda 's' o 'n'.\n")
            Esperar_tecla()