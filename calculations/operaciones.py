from util.validaciones import(Esnumero,CantidadVali)
from util.utlidades import(borrar_pantalla,Esperar_tecla)

def Suma() -> float:
    while True:
        
        borrar_pantalla()
        
        try:
            print("¿Cuántos números desea sumar?")
            cantidad = int(input("> "))
            
            if not CantidadVali(cantidad): 
                break
            
        except ValueError:
            borrar_pantalla()
            print("Entrada no válida. Por favor, usa solo números enteros (sin letras ni espacios).")
            Esperar_tecla()
            
    total:float = 0
    
    for i in range(cantidad):
        total += Esnumero(f"\nIngrese el número {i + 1} a sumar: ")

    return total 

def resta() -> float:
    while True:
        borrar_pantalla()
        print("¡Recuerde!: restar un número negativo equivale a sumar.\n")

        num1 = Esnumero("Ingrese el primer numero a restar: ")
        num2 = Esnumero("Ingrese el segundo numero a restar: ")

        total = num1 - num2

        return total
    
def multiplicacion()->float:
    while True:
        borrar_pantalla
        
        num1 = Esnumero("Ingrese el primer numero a multiplicar: ")
        num2 = Esnumero("Ingrese el segundo numero a multiplicar: ")
        
        total = num1 * num2
        return total
        
def divic()->float:
    while True:
        borrar_pantalla
        
        num1 = Esnumero("Ingrese el primer numero a dividir: ")
        num2 = Esnumero("Ingrese el segundo numero a dividir: ")
        
        total = num1 / num2
        return total 

def poten()->float:
    while True:
        borrar_pantalla
                
        num1 = Esnumero("Ingrese la base de potencia: ")
        
        while True:
            num2 = Esnumero("Ingrese a que grado potenciar: ")
        
        total = num1 ** num2 
        return total
      
def radic()->float:
    borrar_pantalla
        
    while True:       
        num1 = Esnumero("Ingres el radadicando: ")
        if num1 <= 0:
            borrar_pantalla()
            print("no se pueden ingresar 0 o numeros negativos")
            Esperar_tecla()   
        else: 
            break
            
    while True:    
        num2 = Esnumero("Ingrese el indice de raiz: ")
        if num1 <= 0:
            
            borrar_pantalla
            print("no se pueden ingresar 0 o numeros negativos")
            Esperar_tecla()  
        else: 
            break
        
        raiz = 1 / num2
        
        total = num1 ** raiz
        return total 
    
def Chicharon() -> None:
    print("\nResolución de ecuación cuadrática: ax² + bx + c = 0\n")
    Esperar_tecla()
    borrar_pantalla()

    a = Esnumero("Ingrese el valor de a: ")
    while a == 0:
        print("El coeficiente 'a' no puede ser 0 (no sería cuadrática).")
        Esperar_tecla()
        borrar_pantalla()
        a = Esnumero("Ingrese el valor de a: ")

    b = Esnumero("Ingrese el valor de b: ")
    c = Esnumero("Ingrese el valor de c: ")

    discriminante = b**2 - 4 * a * c

    if discriminante > 0:
        x1 = (-b + discriminante**0.5) / (2 * a)
        x2 = (-b - discriminante**0.5) / (2 * a)
        print(f"\nHay dos raíces reales:\nx1 = {x1}\nx2 = {x2}")

    elif discriminante == 0:
        x = -b / (2 * a)
        print(f"\nHay una raíz real doble:\nx = {x}")

    else:
        parte_real = -b / (2 * a)
        parte_imaginaria = (abs(discriminante))**0.5 / (2 * a)
        print(f"\nLas raíces son complejas:")
        print(f"x1 = {parte_real} + {parte_imaginaria}i")
        print(f"x2 = {parte_real} - {parte_imaginaria}i")