file = open("input.txt", "r")
lines = file.readlines()
file.close()

incrementations = 0
previous = -1

for line in lines:
	current = int(line)
	if (previous != -1):
		if (current > previous):
			incrementations += 1

	previous = current

print(f"There's been {incrementations} incrementations.")