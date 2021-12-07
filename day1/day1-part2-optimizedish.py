# Theoretically this version should run faster and use less memory.
# It uses slightly less memory but runs about as fast as the normal version.

file = open("input.txt", "r")
lines = file.readlines()
file.close()

accumulator = [0, 0, 0]

counter = 0
current = -1
previous = -1

incrementations = 0

for line in lines:
	current = int(line)
	accumulator[counter % 3] = current
	counter += 1
	if (counter >= 3):
		current = sum(accumulator)
		if (previous != -1):
			if (current > previous):
				incrementations += 1
		previous = current

print(f"There's been {incrementations} incrementations.")