# version un poquito mas rapida pero menos entendible

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