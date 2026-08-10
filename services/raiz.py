from util.utlidades import borrar_pantalla;
import util.validacions as vl

def radic()->None:
    """Calcula la raiz n-esima de un numero.

    Solicita al usuario el radicando y el indice de la raiz, y
    calcula el resultado como radicando elevado a (1 / indice).
    El resultado se imprime directamente en pantalla.
    """
    borrar_pantalla
        
    num1 = vl.val_float("Ingres el radadicando: ", 0);
    num2 = vl.val_float("Ingrese el indice de raiz: ", 2);    
    
    raiz = 1 / num2
        
    total = num1 ** raiz
    print (f"El resultado es: {total}")