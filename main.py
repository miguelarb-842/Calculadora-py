"""
Calculadora basica hecha en Python con 7 funciones.
Cada una sigue el funcionamiento matematico convencional.

Autor: Miguel J. Gutierrez, Walter Jiron
Repositorio: https://github.com/miguelarb-842/Calculadora-py

"""
from util.utlidades import (borrar_pantalla,Esperar_tecla)
import util.validacions as vl
import services as cal

def main():
    """Ejecuta el bucle principal de la calculadora.

    Muestra el menu, captura la opcion del usuario y despacha
    la operacion correspondiente hasta que se seleccione salir
    o el usuario decida no continuar.
    """
    while True:
        borrar_pantalla()
        cal.menu();
        opcion = vl.valInt("Seleccione una opción: ", 0, 7);
                
        borrar_pantalla()
        match opcion:
                
            case 0:
                print("Se ha salido correctamente, gracias por entrar en la tienda")
                return

            case 1:
                cal.suma()
                  
            case 2: 
                cal.resta()
            
            case 3:
                cal.multiplicacion()
    
            case 4:
                cal.divic()
                 
            case 5:
                cal.poten()
                
            case 6:
                cal.radic()
                
            case 7: 
                cal.chicharon()
                
            case _:
                print("\n\tERROR: la opcion que ingreso no esta en el menu.\n");
                Esperar_tecla();
                borrar_pantalla();
                
        if not vl.valSi_No():
            return
                                    
if __name__ == "__main__":
    main()