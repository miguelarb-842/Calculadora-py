def menu():
    """Muestra en pantalla el menu principal de la calculadora.

    Presenta el titulo, las opciones disponibles (suma, resta,
    multiplicacion, division, potencia, radicalizacion y resolucion
    cuadratica) y la opcion para salir. No solicita entrada del
    usuario ni retorna ningun valor.
    """
    print("Calculadora".center(50))
    print("Seleccione la operacion que desea realizar: ")
    print("""
        1. Suma
        2. Resta
        3. Multiplicación
        4. División
        5. Potencia
        6. Radicalización
        7. Resolución cuadrática para ax² ± bx + c = 0
        0. Salir 
        """)