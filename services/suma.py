from util.validaciones import (cantidadVali, val_float)
from util.utlidades import(borrar_pantalla,Esperar_tecla)


def suma() -> float:
    while True:
        
        borrar_pantalla()
        
        try:
            print("¿Cuántos números desea sumar?")
            cantidad = int(input("> "))
            
            if not cantidadVali(cantidad): 
                break
            
        except ValueError:
            borrar_pantalla()
            print("Entrada no válida. Por favor, usa solo números enteros (sin letras ni espacios).")
            Esperar_tecla()
            
    total:float = 0
    
    for i in range(cantidad):
        total += val_float(f"\nIngrese el número {i + 1} a sumar: ")

    return total 