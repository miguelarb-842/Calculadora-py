from services.input_numeros import ingresarNumeros;
from util.utlidades import borrar_pantalla;

def poten()->None:
    """Calcula la potencia n-ezima de cualquier numero real.
    
    Solicita al usuario ingresar la base y el grado a que ese numero se expondra
    El resultado se imprime directamente en pantalla.
    """
    borrar_pantalla
            
    num1:float
    num2:float 
        
    num1, num2 = ingresarNumeros(
        "Ingrese la base de potencia: ",
        "Ingrese a que grado potenciar: "
    );
    
    total = num1 ** num2 
    print (f"El resultado es: {total}")
