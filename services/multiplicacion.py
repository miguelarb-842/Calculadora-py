from services.input_numeros import ingresarNumeros;
from util.utlidades import borrar_pantalla;

def multiplicacion()->float:
    while True:
        borrar_pantalla()
        
        num1, num2 = ingresarNumeros(
            "Ingrese el primer numero a multiplicar: ",
            "Ingrese el segundo numero a multiplicar: "
        );
        
        total = num1 * num2
        return total