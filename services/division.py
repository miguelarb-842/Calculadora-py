from services.input_numeros import ingresarNumeros;
from util.utlidades import borrar_pantalla;
from util.validaciones import val_float

def divic()->float:
    while True:
        borrar_pantalla
        num1, num2 = ingresarNumeros(
            "Ingrese el primer numero a dividir: ",
            "Ingrese el segundo numero a dividir: "
        );
        while (True):
            if(num2 == 0):
                print("\n\tERROR: no se puede dividir por 0.\n");
                num2 = val_float("Ingrese el segundo numero a dividir: ");
                continue;
            break;
            
        total = num1 / num2
        return total