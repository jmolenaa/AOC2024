from utils import *
from collections import OrderedDict


def findRobot(grid):
	for y, line in enumerate(grid):
		for x, char in enumerate(line):
			if char == "@":
				return y, x


def adjustGrid(grid):
	adjustedGrid = list()
	for line in grid:
		adjustedLine = list()
		for char in line:
			if char == "@":
				adjustedLine.extend(['@', '.'])
			elif char == "O":
				adjustedLine.extend(['[', ']'])
			else:
				adjustedLine.extend([char, char])
		adjustedGrid.append(adjustedLine)
	return adjustedGrid


def addBox(grid, boxesToMove, pos):
	char = getGridChar(grid, pos)
	boxesToMove.add(tuple(pos))
	if getGridChar(grid, pos) == '[':
		boxesToMove.add((pos[0], pos[1] + 1))
	elif getGridChar(grid, pos) == ']':
		boxesToMove.add((pos[0], pos[1] - 1))


def addBoxes(grid, boxesToMove, dir):
	nextRowBoxes = set(boxesToMove)
	for box in boxesToMove:
		inFront = addPositions(box, dir)
		if getGridChar(grid, inFront) == '.':
			continue
		elif getGridChar(grid, inFront) == '#':
			return OrderedDict()
		else:
			addBox(grid, nextRowBoxes, inFront)
	return nextRowBoxes


def moveBoxesPart2(grid, robotPos, dir):
	boxesToMove = set()
	addBox(grid, boxesToMove, addPositions(robotPos, dir))
	while True:
		newBoxesToMove = addBoxes(grid, boxesToMove, dir)
		if len(newBoxesToMove) == 0:
			return robotPos, grid
		elif len(newBoxesToMove) == len(boxesToMove):
			break
		boxesToMove = newBoxesToMove

	updatedGrid = newGrid(grid)
	updatedBoxes = set()
	for box in boxesToMove:
		setGridChar(updatedGrid, addPositions(box, dir), getGridChar(grid, box))
		updatedBoxes.add(tuple(addPositions(box, dir)))

	for box in boxesToMove:
		if box not in updatedBoxes:
			setGridChar(updatedGrid, box, '.')

	return robotPos, updatedGrid


def move(grid, robotPos, dir, part):
	inFront = addPositions(robotPos, dir)
	if getGridChar(grid, inFront) not in {'#', '.'}:
		robotPos, grid = moveBoxesPart2(grid, robotPos, dir)
	if getGridChar(grid, inFront) == ".":
		setGridChar(grid, robotPos, '.')
		robotPos = inFront
		setGridChar(grid, robotPos, '@')
	return robotPos, grid


def solve(grid, moves):
	robotPos = findRobot(grid)
	directions = {"^": (-1, 0), "<": (0, -1), ">": (0, 1), "v": (1, 0)}
	for char in moves:
		robotPos, grid = move(grid, robotPos, directions[char], 1)

	sumGPS = 0
	for y, line in enumerate(grid):
		for x, char in enumerate(line):
			if char in {'O', '['}:
				sumGPS += 100 * y + x
	return sumGPS


def main():
	with open("input") as file:
		lines = file.read().split("\n\n")

	map = lines[0].split("\n")
	moves = ''.join(lines[1].split("\n"))

	grid = newGrid(map)
	part1 = solve(grid, moves)

	grid = adjustGrid(map)
	part2 = solve(grid, moves)
	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	main()