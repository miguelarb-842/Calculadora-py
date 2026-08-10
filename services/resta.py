from services.input_numeros import ingresarNumeros;
from util.utlidades import borrar_pantalla;

def resta() -> None:
    """Realiza la resta de dos numeros ingresados por el usuario.

    Solicita dos numeros, calcula la diferencia entre el primero
    y el segundo, e imprime el resultado en pantalla.
    """
    borrar_pantalla()
    print("¡Recuerde!: restar un número negativo equivale a sumar.\n")
    num1, num2 = ingresarNumeros(
        "Ingrese el primer numero a restar: ", 
        "Ingrese el segundo numero a restar:"
    );
    total = num1 - num2
    
    print(f"La resta es: {total}")
