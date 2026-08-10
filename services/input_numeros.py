from util.validaciones import (val_float);

def ingresarNumeros(mensaje1:str, mensaje2:str)-> tuple[float, float]:
    num1 = val_float(mensaje1);
    num2 = val_float(mensaje2);
    
    return num1, num2;