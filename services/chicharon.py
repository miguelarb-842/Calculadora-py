from util.utlidades import borrar_pantalla, Esperar_tecla;
from util.validaciones import val_float

def chicharon() -> None:
    print("\nResolución de ecuación cuadrática: ax² + bx + c = 0\n")
    Esperar_tecla()
    borrar_pantalla()

    a = val_float("Ingrese el valor de a: ", 1)

    b = val_float("Ingrese el valor de b: ")
    c = val_float("Ingrese el valor de c: ")

    discriminante = b**2 - 4 * a * c

    if discriminante > 0:
        x1 = (-b + discriminante**0.5) / (2 * a)
        x2 = (-b - discriminante**0.5) / (2 * a)
        print(f"\nHay dos raíces reales:\nx1 = {x1}\nx2 = {x2}")

    elif discriminante == 0:
        x = -b / (2 * a)
        print(f"\nHay una raíz real doble:\nx = {x}")

    else:
        parte_real = -b / (2 * a)
        parte_imaginaria = (abs(discriminante))**0.5 / (2 * a)
        print(f"\nLas raíces son complejas:")
        print(f"x1 = {parte_real} + {parte_imaginaria}i")
        print(f"x2 = {parte_real} - {parte_imaginaria}i")