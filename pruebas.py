import csv
import math
from scipy.stats import chi2 # Libreria para la tabla de chi cuadrado

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

	return True if abs(Z_0) < alfa else False

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

	return True if X2_0 < X2_an else False

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

	return True if X2_0 < X2_a else False

def kolmogorov_smirnov(numeros):

	return 0

numeros_generados = leer_csv('generados.csv')
print("Lista de números:", numeros_generados)
# print(promedios(numeros_generados))
# print(frecuencias(numeros_generados))
print(series(numeros_generados))