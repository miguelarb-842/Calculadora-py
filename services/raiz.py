from util.utlidades import borrar_pantalla;
from util.validaciones import val_float

def radic()->float:
    borrar_pantalla
        
    num1 = val_float("Ingres el radadicando: ", 0);
    num2 = val_float("Ingrese el indice de raiz: ", 2);    
    
    raiz = 1 / num2
        
    total = num1 ** raiz
    return total