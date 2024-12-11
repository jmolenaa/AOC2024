from utils import inBounds, newGrid
from collections import defaultdict


def simulateUntilRepeat(beginStone):
	stones = [beginStone]
	for i in range(35):
		line = list()
		for stone in stones:
			if stone == 0:
				line.append(1)
			elif len(str(stone)) % 2 == 0:
				stone = str(stone)
				halflength = int(len(stone) / 2)
				stone1, stone2 = int(stone[:halflength]), int(stone[halflength:])
				line.append(stone1)
				line.append(stone2)
			else:
				line.append(stone * 2024)
		stones = list(line)
		if stones[0] == beginStone:
			return stones, i





def main():
	with open("input") as file:
		line = file.read()

	part1 = 0
	part2 = 0
	stones = list(map(int, line.split()))
	stonesDict = defaultdict(int)
	for stone in stones:
		stonesDict[stone] = 1

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
		# print(stonesDict)

	for key, value in stonesDict.items():
		part1 += value


	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")

if __name__ == "__main__":
	main()

# Initial arrangement:
# 125 17
#
# After 1 blink:
# 253000 1 7
#
# After 2 blinks:
# 253 0 2024 14168
#
# After 3 blinks:
# 512072 1 20 24 28676032
#
# After 4 blinks:
# 512 72 2024 2 0 2 4 2867 6032
#
# After 5 blinks:
# 1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32
#
# After 6 blinks:
# 2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2
