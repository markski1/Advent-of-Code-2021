# Remove from the given list all the values where a given digit is either the most or the least common.
# if checkLess is false, remove the less common ones, if otherwise then otherwise.
def cleanList(list, digit, checkLess):
	zeros = []
	ones = []
	for line in list:
		if line[digit] == "0":
			zeros.append(line)
		else:
			ones.append(line)

	evaluation = len(zeros) > len(ones)
	if checkLess:
		evaluation = not evaluation

	if evaluation:
		return zeros
	else:
		return ones





file = open("input.txt", "r")
lines = file.readlines()
file.close()

OxygenGeneratorList = lines
digitToCheck = 0
# run cleanList on the list until there's only one value left.
while len(OxygenGeneratorList) > 1:
	OxygenGeneratorList = cleanList(OxygenGeneratorList, digitToCheck, False)
	digitToCheck += 1

CO2ScrubberList = lines
digitToCheck = 0
# run cleanList on the list until there's only one value left.
while len(CO2ScrubberList) > 1:
	CO2ScrubberList = cleanList(CO2ScrubberList, digitToCheck, True)
	digitToCheck += 1

# convert the item left in each list to a decimal integer.
# same method as part 1
CO2ScrubberRating = 0
OxygenGeneratorRating = 0
for i in range(12):
	if OxygenGeneratorList[0][i] == "1":
		OxygenGeneratorRating += pow(2, 12-(i+1))
	if CO2ScrubberList[0][i] == "1":
		CO2ScrubberRating += pow(2, 12-(i+1))

print(f"{CO2ScrubberRating} CO2ScrubberRating, {OxygenGeneratorRating} OxygenGeneratorRating, {CO2ScrubberRating*OxygenGeneratorRating}.")