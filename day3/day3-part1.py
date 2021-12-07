file = open("input.txt", "r")
lines = file.readlines()
file.close()

# carry a count of each digit in each position
# It's 12 digit binary numbers, so we'll need 12 counters for each.
zeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# go line for line and count every digit
for linea in lines:
	for i in range(12):
		if linea[i] == '0':
			zeros[i] += 1
		else:
			ones[i] += 1

epsilon = gamma = 0

# for every binary digit go adding to gamma and epsilon
# remember the value of a binary digit is, counting from the right, 2 to the power of it's position.
for i in range(12):
	if zeros[i] > ones[i]:
		epsilon += pow(2, 12-(i+1))
	else:
		gamma += pow(2, 12-(i+1))

print(f"{gamma} gamma, {epsilon} epsilon, {gamma*epsilon}.")