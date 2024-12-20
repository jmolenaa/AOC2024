from utils import *
import sys
from collections import Counter


def createPositionsGrid(grid, pos):
	positions = {pos: 0}
	step = 0
	while True:
		dirs = makeDirs()
		for dir in dirs:
			newPos = tuple(addPos(pos, dir))
			if gridChar(grid, newPos) != '#' and newPos not in positions:
				pos = newPos
				step += 1
				positions[pos] = step
				break
		if gridChar(grid, pos) == 'E':
			break
	return positions, positions[pos]


def checkAround(startPos, position, positions, grid, positionsChecked, maxTime, cheats, maxCheat):
	if distance(startPos, position) > maxCheat:
		return
	for dir in makeDirs():
		currPos = tuple(addPos(position, dir))
		if currPos not in positionsChecked and inBounds(grid, currPos):
			if gridChar(grid, currPos) != '#':
				raceTime = maxTime - positions[currPos] + positions[startPos] + distance(startPos, currPos)
				if (startPos, currPos) not in cheats and raceTime <= maxTime - 100:
					cheats[(startPos, currPos)] = maxTime - raceTime
			positionsChecked.add(currPos)
			checkAround(startPos, currPos, positions, grid, positionsChecked, maxTime, cheats, maxCheat)


def cheating(positions, grid, maxTime, maxCheat):
	cheats = dict()
	for position in positions.keys():
		# print(position)
		positionsChecked = {position}
		checkAround(position, position, positions, grid, positionsChecked, maxTime, cheats, maxCheat)
	return cheats


def main(file):
	with open(file) as file:
		lines = file.read().split("\n")

	grid = newGrid(lines)
	pos = findInGrid(grid, 'S')
	positions, maxTime = createPositionsGrid(grid, pos)

	cheatsPart1 = cheating(positions, grid, maxTime, 1)
	print(f"The answer to part 1 is: {len(cheatsPart1)}")
	cheatsPart2 = cheating(positions, grid, maxTime, 19)
	print(f"The answer to part 2 is: {len(cheatsPart2)}")
	# for position, time in positions.items():
	# 	print(time)
	# 	positionsChecked = {position}
	# 	checkAround(position, position, positions, grid, positionsChecked, maxTime, cheats)
	# 	# break
	# 	# checkCheats(position, time, positions, grid, cheats, maxTime)
	# 	# print(position, time)
	# counting = Counter()
	# for path, amount in cheats.items():
	# 	if amount >= 100:
	# 		# counting[amount] += 1
	# 		part2 += 1
			# print(path)
		# if timeSaved >= 100:
		# 	part1 += amount
		# print(timeSaved, amount)
	# for amount, count in counting.items():
	# 	print(amount, count)
	#
	# print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	if len(sys.argv) == 1:
		main("test_case")
	else:
		main(sys.argv[1])
