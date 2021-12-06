def extraerNumero(linea):
	#los comandos tienen sintaxis onda "forward 4", asi que es nomas sacar el numero despues del espacio.
	pos = linea.find(" ")
	return int(linea[pos+1].split()[0])




archivo = open("input.txt", "r")
lineas = archivo.readlines()

profundidad, horizontal = 0, 0

# los comandos son "down, up, forward", con ver el primer caracter alcanza
for linea in lineas:
	if linea[0] == "d":
		profundidad += extraerNumero(linea)
	elif linea[0] == "u":
		profundidad -= extraerNumero(linea)
	else:
		horizontal += extraerNumero(linea)

print(f"{profundidad} profundidad, {horizontal} horizontal , {profundidad*horizontal}.")