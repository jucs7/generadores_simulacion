import csv
import math
from scipy.stats import chi2 # Libreria para la tabla de chi cuadrado
from scipy.stats import kstwobign # Librería para la tabla de valores criticos de Kolmogorov-Smirnov

# Leer archivo .csv con los numeros generados
def leer_csv(archivo):
	numeros = []
	with open(archivo, 'r') as archivo_csv:
		lector_csv = csv.reader(archivo_csv)
		for fila in lector_csv:
      		# Suponiendo que la columna de números está en la primera posición
			numero = float(fila[0])  # Convertimos a float si es necesario
			numeros.append(numero)
	return numeros

# Prueba de los promedios
def promedios(numeros):
	# Parametros
	N = len(numeros)
	aritmetica = 0
	media = 0.5
	varianza = math.sqrt(1/12)
	alfa = 1.96

	# Calcular promedio aritmetico
	for n in numeros:
		aritmetica = aritmetica + n
	aritmetica = aritmetica / N

	# Calcular valor del estadístico Z_0
	Z_0 = ((aritmetica - media)*(math.sqrt(N)))/varianza
	print("Estadistico: ", Z_0)

	if abs(Z_0) < alfa:
		print("Los numeros pseudoaleatorios provienen de una distribución uniforme")
	else:
		print("Los numeros pseudoaleatorios NO provienen de una distribución uniforme")

# Prueba de frecuencias
def frecuencias(numeros):
	# Parametros
	N = len(numeros)
	n = int(input("Numero de subintervalos: "))
	sub_intervalos = []
	FE = N / n
	FO = []
	alfa = float(input("Valor de alfa: "))
	X2_0 = 0 # Estadístico
	X2_an = chi2.ppf(1-alfa, n-1) # Variable chi cuadrada

	# Obtener los valores de los subintervalos
	for i in range(0,n):
		sub_intervalos.append(i / n)
		FO.append(0)

	# Obtener los valores de la Frecuencia observada FO
	for i in range(0,N):
		for j in range(0,n-1):
			if numeros[i] >= sub_intervalos[j] and numeros[i] < sub_intervalos[j+1]:
				FO[j] += 1
			elif j == n - 2 and numeros[i] >= sub_intervalos[j+1] and numeros[i] <= 1:
				FO[j+1] += 1

	# Obtener el valor del estadistico
	for i in range(0,n):
		X2_0 += (FO[i] - FE)**2 / FE

	print("Valor del estadistico: ", X2_0)
	print("Valor de chi cuadrado: ", X2_an)

	if X2_0 < X2_an:
		print("Los numeros pseudoaleatorios provienen de una distribución uniforme")
	else:
		print("Los numeros pseudoaleatorios NO provienen de una distribución uniforme")

# Prueba de series
def series(numeros):
	# Parametros
	N = len(numeros)
	n = int(input("Valor de n: "))
	sub_intervalos = []
	FE = (N - 1)/(n**2)
	FO = [[0 for _ in range(n)] for _ in range(n)]
	alfa = float(input("Valor de alfa: "))
	x, y = 0, 0 # Coordenadas de las celdas de frecuencia observada
	X2_0 = 0 # Estadistico
	X2_a = 0 # Variable chi cuadrada

	# Obtener los valores de los subintervalos
	for i in range(0,n):
		sub_intervalos.append(i / n)
	
	# Obtener la frecuencia observada de cada celda
	for i in range(0, N-1):
		Ui = numeros[i]
		Uj = numeros[i+1]
		for j in range(0,n-1):
			if Ui >= sub_intervalos[j] and Ui < sub_intervalos[j+1]:
				x = j
			elif j == n - 2 and Ui >= sub_intervalos[j+1] and Ui <= 1:
				x = j + 1
			if Uj >= sub_intervalos[j] and Uj < sub_intervalos[j+1]:
				y = j
			elif j == n - 2 and Uj >= sub_intervalos[j+1] and Uj <= 1:
				y = j + 1
		FO[x][y] += 1
	
	# Calcular estadistico
	for i in range(0,n):
		for j in range(0,n):
			X2_0 = X2_0 + (FO[i][j] - FE)**2
	X2_0 = ((n**2)/(N - 1)) * X2_0
	X2_a = chi2.ppf(1-alfa, (n**2)-1)

	print("Valor del estadistico: ", X2_0)
	print("Valor de chi cuadrado: ", X2_a)

	if X2_0 < X2_a:
		print("Los numeros pseudoaleatorios provienen de una distribución uniforme")
	else:
		print("Los numeros pseudoaleatorios NO provienen de una distribución uniforme")

# Prueba de Kolmogorov-Smirnov
def kolmogorov_smirnov(numeros):
	n = len(numeros)
	F_0 = sorted(numeros) # # Distribucion acumulada hipotética
	F_n = [] # Distribucion acumulada
	D = 0 # Estadistico
	alfa = float(input("Valor de Alfa: "))
	d_an = kstwobign.ppf(1 - alfa/2) / (n**0.5) # Valor critico de Kolmogorov-Smirnov
	
	for i in range(1,n+1):
		F_n.append(i/n)
	
	for i in range(0,n):
		x = abs(F_n[i] - F_0[i])
		if x > D:
			D = x

	print("Valor del estadístico: ", D)
	print("Valor crítico: ", d_an)

	if D < d_an:
		print("Los numeros pseudoaleatorios provienen de una distribución uniforme")
	else:
		print("Los numeros pseudoaleatorios NO provienen de una distribución uniforme")


numeros_generados = leer_csv('generados.csv')
print("Lista de números:", numeros_generados)

print("Realizar pruebas")
print("1. Promedios")
print("2. Frecuencias")
print("3. Series")
print("4. Kolmogorov-Smirnov")
opc = int(input("->"))

if opc == 1:
	promedios(numeros_generados)
elif opc == 2:
	frecuencias(numeros_generados)
elif opc == 3:
	series(numeros_generados)
elif opc == 4:
	kolmogorov_smirnov(numeros_generados)