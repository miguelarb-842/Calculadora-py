from services.input_numeros import ingresarNumeros;
from util.utlidades import borrar_pantalla;
import util.validacions as vl

def divic()->None:
    borrar_pantalla
    num1, num2 = ingresarNumeros(
        "Ingrese el primer numero a dividir: ",
        "Ingrese el segundo numero a dividir: "
    );
    while (True):
        if(num2 == 0):
            print("\n\tERROR: no se puede dividir por 0.\n");
            num2 = vl.val_float("Ingrese el segundo numero a dividir: ");
            continue;
        break;
        
    total = num1 / num2
    print(f"El resultado es {total}")