def extraerNumero(linea):
	#los comandos tienen sintaxis onda "forward 4", asi que es nomas sacar el numero despues del espacio.
	pos = linea.find(" ")
	return int(linea[pos+1].split()[0])




archivo = open("input.txt", "r")
lineas = archivo.readlines()

profundidad, horizontal, orientacion = 0, 0, 0

# los comandos son "down, up, forward", con ver el primer caracter alcanza
for linea in lineas:
	if linea[0] == "d":
		orientacion += extraerNumero(linea)
	elif linea[0] == "u":
		orientacion -= extraerNumero(linea)
	else:
		valor = extraerNumero(linea)
		horizontal += valor
		profundidad += orientacion * valor

print(f"{profundidad} profundidad, {horizontal} horizontal , {profundidad*horizontal}.")