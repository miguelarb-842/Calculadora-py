from util.utlidades import (borrar_pantalla,Esperar_tecla)
from util.validaciones import(continuar,continuar_chicharonera, valInt)
import services as cal


def main():
    while True:
        borrar_pantalla()
        cal.menu();
        opcion = valInt("Seleccione una opción: ", 0, 7);
        
       
                
        borrar_pantalla()
        match opcion:
                
            case 0:
                print("Se ha salido correctamente, gracias por entrar en la tienda")
                return

            case 1:
                resultado = cal.suma()
                if not continuar(resultado):
                    return
            
            case 2: 
                resultado = cal.resta()
                if not continuar(resultado):
                    return
                
            case 3:
                resultado = cal.multiplicacion()
                if not continuar(resultado):
                    return
            case 4:
                resultado = cal.divic()
                if not continuar(resultado):
                    return 
            case 5:
                resultado = cal.poten()
                if not continuar(resultado):
                    return
            case 6:
                resultado = cal.radic()
                if not continuar(resultado):
                    return
            case 7: 
                cal.chicharon()
                if not continuar_chicharonera():
                    return
            case _:
                print("\n\tERROR: la opcion que ingreso no esta en el menu.\n");
                Esperar_tecla();
                borrar_pantalla();
                                    
if __name__ == "__main__":
    main()
