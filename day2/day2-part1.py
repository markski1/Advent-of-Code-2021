def extractNumber(line):
	# commands have syntax along the lines of "forward 4", so just grab the value after the space which will be a number.
	pos = line.find(" ")
	return int(line[pos+1].split()[0])




file = open("input.txt", "r")
lines = file.readlines()
file.close()

depth, horizontal = 0, 0

# commands are "down, up, forward", looking at the first digit is good enough
for line in lines:
	if line[0] == "d":
		depth += extractNumber(line)
	elif line[0] == "u":
		depth -= extractNumber(line)
	else:
		horizontal += extractNumber(line)

print(f"{depth} depth, {horizontal} horizontal , {depth*horizontal}.")