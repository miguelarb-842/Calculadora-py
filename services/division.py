from services.input_numeros import ingresarNumeros;
from util.utlidades import (borrar_pantalla,Esperar_tecla);
import util.validacions as vl

def divic()->None:
    """ Resuelve la ecucucion de divicion entre dos numeros [num1,num2].
    
    Sele solicita al usuario el divisor [num1] y el dividendo [num2].
    Cuando se ingresa en el divisor un 0 se señala un error y devuelve:
        ERROR: no se puede dividir por 0.
    Y se le solicita al usuario volver a ingresar los valores
    
    """
    while (True):
        
        borrar_pantalla
        num1, num2 = ingresarNumeros(
        "Ingrese el primer numero a dividir: ",
        "Ingrese el segundo numero a dividir: "
        );
        
        if(num2 == 0):
            print("\n\tERROR: no se puede dividir por 0.\n");
            Esperar_tecla()
            borrar_pantalla()
            continue;
        
        break;
    
    total = num1 / num2
    print(f"El resultado es {total}")