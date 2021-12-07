def extractNumbers(linea):
	# commands have syntax along the lines of "forward 4", so just grab the value after the space which will be a number.
	pos = linea.find(" ")
	return int(linea[pos+1].split()[0])




file = open("input.txt", "r")
lines = file.readlines()
file.close()

depth, horizontal, aim = 0, 0, 0

# commands are "down, up, forward", looking at the first digit is good enough
for linea in lines:
	if linea[0] == "d":
		aim += extractNumbers(linea)
	elif linea[0] == "u":
		aim -= extractNumbers(linea)
	else:
		value = extractNumbers(linea)
		horizontal += value
		depth += aim * value

print(f"{depth} depth, {horizontal} horizontal , {depth*horizontal}.")