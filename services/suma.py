import util.validacions as vl
from util.utlidades import(borrar_pantalla,Esperar_tecla)

def suma() -> None:
    """Realiza la suma de una cantidad variable de numeros.

    Solicita al usuario cuantos numeros desea sumar, valida esa
    cantidad, y luego solicita cada numero individualmente para
    calcular el total. El resultado se imprime en pantalla.
    """
    while True:
        
        borrar_pantalla()
        
        try:
            print("¿Cuántos números desea sumar?")
            cantidad = int(input("> "))
            
            if not vl.cantidadVali(cantidad): 
                break
            
        except ValueError:
            borrar_pantalla()
            print("Entrada no válida. Por favor, usa solo números enteros (sin letras ni espacios).")
            Esperar_tecla()
            
    total:float = 0
    
    for i in range(cantidad):
        total += vl.val_float(f"\nIngrese el número {i + 1} a sumar: ")

    print(f"La suma es: {total}")