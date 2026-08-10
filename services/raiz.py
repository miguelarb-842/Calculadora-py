from util.utlidades import borrar_pantalla;
import util.validacions as vl

def radic()->None:
    borrar_pantalla
        
    num1 = vl.val_float("Ingres el radadicando: ", 0);
    num2 = vl.val_float("Ingrese el indice de raiz: ", 2);    
    
    raiz = 1 / num2
        
    total = num1 ** raiz
    print (f"El resultado es: {total}")