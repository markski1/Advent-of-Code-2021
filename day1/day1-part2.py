archivo = open("input.txt", "r")
lineas = archivo.readlines()

acumulador = [0, 0, 0]
sumas = []

contador = 0

for linea in lineas:
	actual = int(linea)
	acumulador[contador % 3] = actual
	contador += 1
	if (contador >= 3):
		sumas.append(sum(acumulador))

anterior = -1
incrementaciones = 0

for i in sumas:
	if (anterior != -1):
		if (i > anterior):
			incrementaciones += 1

	anterior = i

print(f"Hubo {incrementaciones} incrementaciones.")

# La solución es un poco distinta a la que implica el enunciado.
# En vez de llevar varias ventanas de 3, se lleva un solo acumulador de 3 elementos
# Y se va agregando a una lista cada vez que uno cambia, luego simplemente se comparan
# los elementos de la misma.

# Ejemplo:

# [198, 208, 209] = 615 {primer}
# [212, 208, 209] = 629 {incremento}
# [212, 213, 209] = 634 {incremento}
# [212, 213, 217] = 642 {incremento}
# [218, 213, 217] = 648 {incremento}
# [218, 223, 217] = 658 {incremento}
# [218, 223, 222] = 663 {incremento}
# [224, 223, 222] = 669 {incremento}
# [224, 216, 222] = 662 {decremento}
# [224, 216, 233] = 673 {incremento}