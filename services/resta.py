from services.input_numeros import ingresarNumeros;
from util.utlidades import borrar_pantalla;

def resta() -> float:
    while True:
        borrar_pantalla()
        print("¡Recuerde!: restar un número negativo equivale a sumar.\n")

        num1, num2 = ingresarNumeros(
            "Ingrese el primer numero a restar: ", 
            "Ingrese el segundo numero a restar:"
        );

        total = num1 - num2

        return total
