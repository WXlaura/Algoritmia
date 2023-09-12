print("\n Ejercicio N°2 \n")
import math

print("""
* Seleccione de alguna de las siguientes opciones: 
\n 1. Triangulo Unidimensional
\n 2. Triangulo Bidimensional
\n 3. Triangulo tridimensional
""")

a = int(input("Escribe una de las opciones: "))

if a == 1 :
        
    print("""
    * Seleccione de alguna de las siguientes opciones: 
    \n 1. Triangulo Escaleno
    \n 2. Triangulo Isosceles
    \n 3. Triangulo Equilatero
    """)

    b = int(input("Elige alguna de las opciones: "))

    if b == 1 :
        print("Seleccionaste un triangulo Escaleno :D")
        
        a = float(input("Lado a: "))
        b = float(input("Lado b: "))
        c = float(input("Lado c: "))

        # Calcula el ángulo A usando la Ley de los cosenos
        A_rad = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
        A_deg = math.degrees(A_rad)

        # Calcula los ángulos B y C utilizando la suma de ángulos en un triángulo
        B_deg = 180 - A_deg
        C_deg = B_deg

        # Imprime los resultados
        print("Ángulo A:", A_deg, "grados")
        print("Ángulo B:", B_deg, "grados")
        print("Ángulo C:", C_deg, "grados")


    elif b == 2:
        print("Seleccionaste un triangulo Isosceles :D")

        a = float(input("Longitud de los lados iguales: "))  # Longitud de los lados iguales
        A_deg = float(input("Angulo entre los lados iguales: "))  # Ángulo entre los lados iguales en grados

        # Convertir el ángulo de grados a radianes
        A_rad = math.radians(A_deg)

        # Calcular el ángulo B y el ángulo C
        B_rad = C_rad = (math.pi - A_rad) / 2  # La suma de los ángulos interiores es igual a pi radianes (180 grados)

        # Convertir los ángulos de radianes a grados
        B_deg = math.degrees(B_rad)
        C_deg = math.degrees(C_rad)

        # Imprimir los resultados
        print("Ángulo A:", A_deg, "grados")
        print("Ángulo B:", B_deg, "grados")
        print("Ángulo C:", C_deg, "grados")

    
    elif b == 3:
        print("Seleccionaste un triangulo Equilatero :D")

        # Longitud del lado del triángulo equilátero
        lado = float(input("Longitud del lado: "))  # Longitud del lado

        # Calcula el ángulo interno del triángulo equilátero
        angulo_interno_rad = math.radians(60)  # Ángulo interior en radianes (60 grados)
        angulo_interno_deg = math.degrees(angulo_interno_rad)  # Ángulo interior en grados

        # Imprime los resultados
        print("Ángulo interior del triángulo equilátero:", angulo_interno_deg, "grados")

    
    else:
        print("No existe entre las opciones.")

elif a == 2:
    print("""
    * Seleccione de alguna de las siguientes opciones: 
    \n 1. Triangulo Escaleno
    \n 2. Triangulo Isosceles
    \n 3. Triangulo Equilatero
    """)

    b = int(input("Elige alguna de las opciones: "))
    if b == 1 :
        print("Seleccionaste un triangulo Escaleno :D")

        # Coordenadas de los vértices del triángulo en 2D
        x1 = float(input("Vertice del triangulo x1: "))
        x2 = float(input("Vertice del triangulo x2: "))
        x3 = float(input("Vertice del triangulo x3: "))
        y1 = float(input("Vertice del triangulo y1: "))
        y2 = float(input("Vertice del triangulo y2: "))
        y3 = float(input("Vertice del triangulo y3: "))

        # Función para calcular la distancia entre dos puntos (longitud de un lado)
        def distancia(x1, y1, x2, y2):
            return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        # Calcular las longitudes de los lados del triángulo
        a = distancia(x2, y2, x3, y3)
        b = distancia(x1, y1, x3, y3)
        c = distancia(x1, y1, x2, y2)

        # Calcular los ángulos utilizando la Ley de los cosenos
        A_rad = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
        A_deg = math.degrees(A_rad)

        B_rad = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
        B_deg = math.degrees(B_rad)

        C_rad = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
        C_deg = math.degrees(C_rad)

        # Imprimir los resultados
        print("Ángulo A:", A_deg, "grados")
        print("Ángulo B:", B_deg, "grados")
        print("Ángulo C:", C_deg, "grados")


    elif b == 2:
        print("Seleccionaste un triangulo Isosceles :D")
        
        # Coordenadas de los vértices del triángulo isósceles en 2D
        x1 = float(input("Vertice del triangulo x1: "))
        x2 = float(input("Vertice del triangulo x2: "))
        x3 = float(input("Vertice del triangulo x3: "))
        y1 = float(input("Vertice del triangulo y1: "))
        y2 = float(input("Vertice del triangulo y2: "))
        y3 = float(input("Vertice del triangulo y3: "))

        # Función para calcular la distancia entre dos puntos (longitud de un lado)
        def distancia(x1, y1, x2, y2):
            return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        # Calcular las longitudes de los lados del triángulo
        a = distancia(x2, y2, x3, y3)  # Lado igual
        b = distancia(x1, y1, x3, y3)  # Lado igual
        c = distancia(x1, y1, x2, y2)  # Lado diferente

        # Calcular el ángulo entre los lados iguales utilizando la Ley de los cosenos
        A_rad = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
        A_deg = math.degrees(A_rad)

        # Calcular los ángulos en los vértices utilizando la suma de ángulos en un triángulo
        B_deg = C_deg = (180 - A_deg) / 2  # Ángulos en los vértices

        # Imprimir los resultados
        print("Ángulo A:", A_deg, "grados")
        print("Ángulo B:", B_deg, "grados")
        print("Ángulo C:", C_deg, "grados")

    
    elif b == 3:
        print("Seleccionaste un triangulo Equilatero :D")

        # Coordenadas de los vértices del triángulo en 2D
        x1 = float(input("Vertice del triangulo x1: "))
        x2 = float(input("Vertice del triangulo x2: "))
        x3 = float(input("Vertice del triangulo x3: "))
        y1 = float(input("Vertice del triangulo y1: "))
        y2 = float(input("Vertice del triangulo y2: "))
        y3 = float(input("Vertice del triangulo y3: "))

        # Función para calcular la distancia entre dos puntos (longitud de un lado)
        def distancia(x1, y1, x2, y2):
            return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

        # Calcular las longitudes de los lados del triángulo
        lado1 = distancia(x1, y1, x2, y2)
        lado2 = distancia(x2, y2, x3, y3)
        lado3 = distancia(x3, y3, x1, y1)

        # Verificar si el triángulo es equilátero
        es_equilatero = lado1 == lado2 == lado3

        if es_equilatero:
            print("El triángulo es equilátero, y todos sus ángulos son de 60 grados.")
        else:
            print("El triángulo no es equilátero. Sus ángulos no son iguales.")

    
    else:
        print("No existe entre las opciones.")

elif a == 3:
    print("""
    * Seleccione de alguna de las siguientes opciones: 
    \n 1. Triangulo Escaleno
    \n 2. Triangulo Isosceles
    \n 3. Triangulo Equilatero
    """)

    b = int(input("Elige alguna de las opciones: "))
    if b == 1 :
        print("Seleccionaste un triangulo Escaleno :D")
        
        # Coordenadas de los vértices del triángulo en 3D
        x1 = float(input("Vertice del triangulo x1: "))
        x2 = float(input("Vertice del triangulo x2: "))
        x3 = float(input("Vertice del triangulo x3: "))
        y1 = float(input("Vertice del triangulo y1: "))
        y2 = float(input("Vertice del triangulo y2: ")) 
        y3 = float(input("Vertice del triangulo y3: ")) 
        z1 = float(input("Vertice del triangulo z1: "))
        z2 = float(input("Vertice del triangulo z2: "))
        z3 = float(input("Vertice del triangulo z3: "))

        # Función para calcular la distancia entre dos puntos (longitud de un lado)
        def distancia(x1, y1, z1, x2, y2, z2):
            return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

        # Calcular las longitudes de los lados del triángulo
        a = distancia(x2, y2, z2, x3, y3, z3)
        b = distancia(x1, y1, z1, x3, y3, z3)
        c = distancia(x1, y1, z1, x2, y2, z2)

        # Calcular los ángulos utilizando la Ley de los cosenos
        A_rad = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
        A_deg = math.degrees(A_rad)

        B_rad = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
        B_deg = math.degrees(B_rad)

        C_rad = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
        C_deg = math.degrees(C_rad)

        # Imprimir los resultados
        print("Ángulo A:", A_deg, "grados")
        print("Ángulo B:", B_deg, "grados")
        print("Ángulo C:", C_deg, "grados")


    elif b == 2:
        print("Seleccionaste un triangulo Isosceles :D")
        
        # Coordenadas de los vértices del triángulo en 3D
        x1 = float(input("Vertice del triangulo x1: "))
        x2 = float(input("Vertice del triangulo x2: "))
        x3 = float(input("Vertice del triangulo x3: "))
        y1 = float(input("Vertice del triangulo y1: "))
        y2 = float(input("Vertice del triangulo y2: ")) 
        y3 = float(input("Vertice del triangulo y3: ")) 
        z1 = float(input("Vertice del triangulo z1: "))
        z2 = float(input("Vertice del triangulo z2: "))
        z3 = float(input("Vertice del triangulo z3: "))

        # Función para calcular la distancia entre dos puntos (longitud de un lado)
        def distancia(x1, y1, z1, x2, y2, z2):
            return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

        # Calcular las longitudes de los lados del triángulo
        a = distancia(x2, y2, z2, x3, y3, z3)  # Lado igual
        b = distancia(x1, y1, z1, x3, y3, z3)  # Lado igual
        c = distancia(x1, y1, z1, x2, y2, z2)  # Lado diferente

        # Calcular el ángulo opuesto al lado diferente utilizando la Ley de los cosenos
        A_rad = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
        A_deg = math.degrees(A_rad)

        # Calcular los ángulos en los vértices utilizando la suma de ángulos en un triángulo
        B_rad = C_rad = (math.pi - A_rad) / 2  # Ángulos en los vértices en radianes
        B_deg = C_deg = math.degrees(B_rad)  # Ángulos en los vértices en grados

        # Imprimir los resultados
        print("Ángulo A:", A_deg, "grados")
        print("Ángulo B:", B_deg, "grados")
        print("Ángulo C:", C_deg, "grados")

    
    elif b == 3:
        print("Seleccionaste un triangulo Equilatero :D")

        # Coordenadas de los vértices del triángulo en 3D
        x1 = float(input("Vertice del triangulo x1: "))
        x2 = float(input("Vertice del triangulo x2: "))
        x3 = float(input("Vertice del triangulo x3: "))
        y1 = float(input("Vertice del triangulo y1: "))
        y2 = float(input("Vertice del triangulo y2: ")) 
        y3 = float(input("Vertice del triangulo y3: ")) 
        z1 = float(input("Vertice del triangulo z1: "))
        z2 = float(input("Vertice del triangulo z2: "))
        z3 = float(input("Vertice del triangulo z3: "))

        # Función para calcular la distancia entre dos puntos (longitud de un lado)
        def distancia(x1, y1, z1, x2, y2, z2):
            return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

        # Calcular las longitudes de los lados del triángulo
        lado1 = distancia(x1, y1, z1, x2, y2, z2)
        lado2 = distancia(x2, y2, z2, x3, y3, z3)
        lado3 = distancia(x3, y3, z3, x1, y1, z1)

        # Verificar si el triángulo es equilátero (todos los lados son iguales)
        es_equilatero = lado1 == lado2 == lado3

        if es_equilatero:
            print("El triángulo es equilátero, y todos sus ángulos son de 60 grados.")
        else:
            print("El triángulo no es equilátero. Sus ángulos no son iguales.")

    
    else:
        print("No existe entre las opciones.")

else:
    print("No existe en ninguna de las opciones")