file = open("input.txt", "r")
lines = file.readlines()
file.close()

accumulator = [0, 0, 0]
additions = []

counter = 0

for line in lines:
	current = int(line)
	accumulator[counter % 3] = current
	counter += 1
	if (counter >= 3):
		additions.append(sum(accumulator))

previous = -1
incrementations = 0

for i in additions:
	if (previous != -1):
		if (i > previous):
			incrementations += 1

	previous = i

print(f"There's been {incrementations} incrementations.")

# It's worth noting that this solution is based off someone else's solution in C.
# I couldn't figure out a (efficient) way to keep count of the addition windows.
# As it turns out, it's not necesary if you just add the additions to a single list each
# time you go through a line.

# Example:

# [198, 208, 209] = 615 {first}
# [212, 208, 209] = 629 {increment}
# [212, 213, 209] = 634 {increment}
# [212, 213, 217] = 642 {increment}
# [218, 213, 217] = 648 {increment}
# [218, 223, 217] = 658 {increment}
# [218, 223, 222] = 663 {increment}
# [224, 223, 222] = 669 {increment}
# [224, 216, 222] = 662 {decrement}
# [224, 216, 233] = 673 {increment}