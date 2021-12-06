archivo = open("input.txt", "r")
lineas = archivo.readlines()

incrementaciones = 0
anterior = -1

for linea in lineas:
	actual = int(linea)
	if (anterior != -1):
		if (actual > anterior):
			incrementaciones += 1

	anterior = actual

print(f"Hubo {incrementaciones} incrementaciones.")