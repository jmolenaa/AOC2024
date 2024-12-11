from utils import inBounds, newGrid
from collections import defaultdict


def calculateHowManyStones(stonesDict: defaultdict[int]):
	stoneAmount = 0
	for stoneId in stonesDict:
		stoneAmount += stonesDict[stoneId]
	return stoneAmount


def main():
	with open("input") as file:
		line = file.read()

	part1 = 0
	part2 = 0
	stones = list(map(int, line.split()))
	# keeping track of stones through a default dictionary
	# stone engravings are the keys and the values are the amoung of stones with that engraving
	# at the start all the stones only appear once
	stonesDict = defaultdict(int)
	for stone in stones:
		stonesDict[stone] = 1

	# simulating 75 blinks
	# we make new dictionaries for each blink
	# we do this, because applying to rules to the stones in place
	# would change the current dictionary which could cause issues
	# for every engraving we apply the rule and add
	# however many stones with that engraving we had to the new
	# dictionary with the new engraving as the key
	# f.e. if we have 10 stones with engraving 0
	# we add 10 stones to the new dictionary with engraving 1
	# the new dictionary does not have the 10 stones with engraving 0
	for i in range(75):
		newStonesDict = defaultdict(int)
		for stone, amount in stonesDict.items():
			if stone == 0:
				newStonesDict[1] += amount
			elif len(str(stone)) % 2 == 0:
				stone = str(stone)
				halflength = int(len(stone) / 2)
				stone1, stone2 = int(stone[:halflength]), int(stone[halflength:])
				newStonesDict[stone1] += amount
				newStonesDict[stone2] += amount
			else:
				newStonesDict[stone * 2024] += amount
		stonesDict = newStonesDict.copy()
		if i == 24:
			part1 = calculateHowManyStones(stonesDict)

	part2 = calculateHowManyStones(stonesDict)

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")

if __name__ == "__main__":
	main()
