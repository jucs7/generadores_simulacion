import math # Funcion para el MCD
import csv

def congruencial_mixto():
    # Parámetros
    Xn = int(input("Semilla: "))
    X_0 = Xn
    a = int(input("Multiplicador: "))
    c = int(input("Constante aditiva: "))
    m = int(input("Modulo: "))

    # Validar parámetros
    if not (0 < Xn < m and 0 < a < m and 0 <= c < m and 0 < m):
        print("Error: Por favor ingresa valores adecuados para los parámetros.")
        return

    validar_mixto(a,c,m)

    # Listas para almacenar los números generados
    generados = []
    normalizados = []
    print("\nNumeros generados: ")
    
    while True:
        # Fórmula del método congruencial mixto
        Xn = (a * Xn + c) % m
        # Validar si se completó el periodo
        if Xn in generados:
            break
        # Agregar el número generado al conjunto
        generados.append(Xn)
        # Normalizamos el número para que esté entre 0 y 1
        normalizados.append(Xn / m) 
        # Imprimir el número generado
        print(Xn / m)  

    # Escribir los números generados en un archivo CSV
    with open('generados.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['n;Xn;Generados'])
        writer.writerow([f"0;{X_0}"])
        for i in range(0, len(generados)):
            writer.writerow([f"{i+1};{generados[i]};{normalizados[i]}"])

    print("Archivo 'generados.csv' creado satisfactoriamente con los números generados.")

def validar_mixto(a, c, m):
    # Verificar si 'a' es impar y no divisible por 3 o 5
    if a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
        print("Warning: El multiplicador 'a' debe ser un entero impar no divisible por 3 o 5.")

    # Verificar si 'c' es impar
    if c % 2 == 0:
        print("Warning: La constante aditiva 'c' debe ser un entero impar.")

    # Verificar si 'c' y 'm' son primos entre sí
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    if gcd(c, m) != 1:
        print("Warning: 'c' debe ser relativamente primo a 'm'.")

def congruencial_multiplicativo():
    # Parámetros
    Xn = int(input("\nSemilla: "))
    X_0 = Xn
    a = int(input("Multiplicador: "))
    m = int(input("Modulo: "))

    # Validar parámetros
    if not (0 < Xn < m and 0 < a < m and 0 < m):
        print("Error: Por favor ingresa valores adecuados para los parámetros.")
        return

    # Validar si m es primo
    if not validar_multiplicativo(m):
        print("Warning: El valor de 'm' no es primo.")

    # Listas para almacenar los números generados
    generados = []
    normalizados = []
    print("\nNumeros generados: ")

    while True:
        # Fórmula del método congruencial mixto
        Xn = (a * Xn) % m
        # Validar si se completó el periodo
        if Xn in generados:
            break
        # Agregar el número generado al conjunto
        generados.append(Xn)
        normalizados.append(Xn / m)
        # Imprimir el número generado
        print(Xn / m)  # Normalizamos el número para que esté entre 0 y 1

    # Escribir los números generados en un archivo CSV
    with open('generados.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['n;Xn;Generados'])
        writer.writerow([f"0;{X_0}"])
        for i in range(0, len(generados)):
            writer.writerow([f"{i+1};{generados[i]};{normalizados[i]}"])

    print("Archivo 'generados.csv' creado satisfactoriamente con los números generados.")

def validar_multiplicativo(m):
    # Validar si m es primo
    if m <= 1:
        return False
    if m <= 3:
        return True
    if m % 2 == 0 or m % 3 == 0:
        return False
    i = 5
    while i * i <= m:
        if m % i == 0 or m % (i + 2) == 0:
            return False
        i += 6
    return True

def cuadrados_medios():
    # Parametros
    semilla = int(input("Ingrese la semilla (valor inicial de 4 dígitos): "))

    # Validar semilla
    if not (len(str(semilla)) == 4):
        print("Error: La semilla debe ser un numero de 4 digitos.")
        return

    n = int(input("Ingrese la cantidad de números aleatorios a generar: "))
    print("Números pseudoaleatorios generados:")
    generados = []
    for _ in range(n): 
        semilla = int(str(semilla ** 2).zfill(8)[2:6])
        generados.append(semilla / 10000)  # Normalizar para obtener números entre 0 y 1
        print(semilla / 10000)

def lagged_fibonacci():
    # Parametros
    x0 = int(input("Primer valor inicial: "))
    x1 = int(input("Segundo valor inicial: "))
    lag = int(input("Lag: "))
    mod = int(input("Modulo: "))
    n = int(input("Ingrese la cantidad de números aleatorios a generar: "))

    # Secuencia con los numeros generados
    generados = [x0, x1]
    print("Números pseudoaleatorios generados:")    
    for x in range(0, n):
        # Calcular el próximo número pseudoaleatorio
        Xn = (generados[x - lag] + generados[x - lag + 1]) % mod
        generados.append(Xn)
        print(Xn)

def bbs():
    # Parametros
    p = int(input("Valor de P: "))
    q = int(input("Valor de Q: "))
    semilla = int(input("Semilla: "))
    n = int(input("Cantidad de numeros aleatorios a generar: "))

    # Calcula el módulo n
    modulus = p * q

    # Genera la lista de números pseudoaleatorios
    generados = []
    for _ in range(n):
        semilla = (semilla * semilla) % modulus
        generados.append(semilla)
        print(semilla)


print("Generador: ")
print("1. Congruencial mixto")
print("2. Congruencial multiplicativo")
print("3. Cuadrados medios")
print("4. Lagged Fibonacci")
print("5. BBS")
opc = int(input("-->"))

if opc == 1:
    congruencial_mixto()
elif opc == 2:
    congruencial_multiplicativo()
elif opc == 3:
    cuadrados_medios()
elif opc == 4:
    lagged_fibonacci()
elif opc == 5:
    bbs()

