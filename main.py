from util.utlidades import (borrar_pantalla,Esperar_tecla)
from util.validaciones import(CONTINUAR,CONTINUAR_CHICHARONERA)
from services.secciones import(menu)

from calculations.operaciones import(
    Suma,
    resta,
    multiplicacion,
    divic,
    poten,
    radic,
    Chicharon
    )

def main():
       while True:
        while True:
            borrar_pantalla()
            menu()
            try:
                opcion = int(input("Seleccione una opción: "))
                break
            except ValueError:
                borrar_pantalla()
                print("Error: ingrese un número válido.")
                Esperar_tecla()
                
        borrar_pantalla()
        match opcion:
                
            case 0:
                print("Se ha salido correctamente, gracias por entrar en la tienda")
                return

            case 1:
                resultado = Suma()
                if not CONTINUAR(resultado):
                    return
            
            case 2: 
                resultado = resta()
                if not CONTINUAR(resultado):
                    return
                
            case 3:
                resultado = multiplicacion()
                if not CONTINUAR(resultado):
                    return
            case 4:
                resultado = divic()
                if not CONTINUAR(resultado):
                    return 
            case 5:
                resultado = poten()
                if not CONTINUAR(resultado):
                    return
            case 6:
                resultado = radic()
                if not CONTINUAR(resultado):
                    return
            case 7: 
                Chicharon()
                if not CONTINUAR_CHICHARONERA():
                    return
                                    
if __name__ == "__main__":
    main()
