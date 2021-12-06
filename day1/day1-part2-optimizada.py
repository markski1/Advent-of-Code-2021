# version (que teoricamente deberia ser) poquito mas rapida pero menos entendible.
# el tema es que por cuestiones misteriosas de python performa igual que la otra a pesar de hacer todo en una iteración, qcyo

archivo = open("input.txt", "r")
lineas = archivo.readlines()
archivo.close()

acumulador = [0, 0, 0]

contador = 0
actual = -1
anterior = -1

incrementaciones = 0

for linea in lineas:
	actual = int(linea)
	acumulador[contador % 3] = actual
	contador += 1
	if (contador >= 3):
		actual = sum(acumulador)
		if (anterior != -1):
			if (actual > anterior):
				incrementaciones += 1
		anterior = actual

print(f"Hubo {incrementaciones} incrementaciones.")