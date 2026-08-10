from services.input_numeros import ingresarNumeros;
from util.utlidades import borrar_pantalla;

def poten()->None:
    
    borrar_pantalla
            
    num1, num2 = ingresarNumeros(
        "Ingrese la base de potencia: ",
        "Ingrese a que grado potenciar: "
    );
    
    total = num1 ** num2 
    print (f"El resultado es: {total}")
