import util.validacions as vl

def ingresarNumeros(mensaje1:str, mensaje2:str)-> tuple[float, float]:
    num1 = vl.val_float(mensaje1);
    num2 = vl.val_float(mensaje2);
    
    return num1, num2;