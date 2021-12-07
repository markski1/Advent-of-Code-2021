archivo = open("input.txt", "r")
lineas = archivo.readlines()

# llevamos la cuenta de la ocurrencia de ceros y unos en cada posición.
# son numeros binarios de 12 digitos, por lo tanto llevamos listas con 12 contadores
ceros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
unos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# vamos linea por linea y contando cada digito
for linea in lineas:
	for i in range(12):
		if linea[i] == '0':
			ceros[i] += 1
		else:
			unos[i] += 1

epsilon = gamma = 0

# para los 12 digitos vamos sumando a epsilon y a gamma sus respectivos valores.
# recordar que el valor de un digito binario es dos llevado al valor de su posición (contando desde la derecha y comenzando en uno)
for i in range(12):
	if ceros[i] > unos[i]:
		epsilon += pow(2, 12-(i+1))
	else:
		gamma += pow(2, 12-(i+1))

print(f"{gamma} gamma, {epsilon} epsilon, {gamma*epsilon}.")