from utils import *


def getGridChar(grid, pos):
	return grid[pos[0]][pos[1]]


def setGridChar(grid, pos, char):
	grid[pos[0]][pos[1]] = char


def moveBoxesPart1(grid, robotPos, dir):
	pos = addPositions(robotPos, dir)
	while grid[pos[0]][pos[1]] != "." and grid[pos[0]][pos[1]] != "#":
		pos = addPositions(pos, dir)
	if grid[pos[0]][pos[1]] == ".":
		while getGridChar(grid, subtractPositions(pos, dir)) == 'O':
			setGridChar(grid, pos, 'O')
			pos = subtractPositions(pos, dir)
		setGridChar(grid, robotPos, '.')
		robotPos = addPositions(robotPos, dir)
		setGridChar(grid, robotPos, '@')
	return robotPos


def addBox(grid, boxesToMove, pos):
	if getGridChar(grid, pos) == '[':
		boxesToMove.add(tuple(pos))
		boxesToMove.add((pos[0], pos[1] + 1))
	elif getGridChar(grid, pos) == ']':
		boxesToMove.add(tuple(pos))
		boxesToMove.add((pos[0], pos[1] - 1))
	else:
		return False


def addBoxes(grid, boxesToMove, dir):
	nextRowBoxes = set(boxesToMove)
	for box in boxesToMove:
		inFront = addPositions(box, dir)
		if getGridChar(grid, inFront) == '.':
			continue
		elif getGridChar(grid, inFront) == '#':
			return set()
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

	setGridChar(updatedGrid, robotPos, '.')
	robotPos = addPositions(robotPos, dir)
	setGridChar(updatedGrid, robotPos, '@')
	return robotPos, updatedGrid


def move(grid, robotPos, dir, part):
	inFront = addPositions(robotPos, dir)
	if grid[inFront[0]][inFront[1]] == ".":
		grid[robotPos[0]][robotPos[1]] = "."
		robotPos = inFront
		grid[robotPos[0]][robotPos[1]] = "@"
	elif grid[inFront[0]][inFront[1]] == "O":
		robotPos = moveBoxesPart1(grid, robotPos, dir)
	elif grid[inFront[0]][inFront[1]] == "[" or grid[inFront[0]][inFront[1]] == "]":
		robotPos, grid = moveBoxesPart2(grid, robotPos, dir)
	return robotPos, grid


def solvePart1(grid, moves, robotPos):
	part1 = 0
	for char in moves:
		if char == "^":
			robotPos, grid = move(grid, robotPos, (-1, 0), 1)
		elif char == "<":
			robotPos, grid = move(grid, robotPos, (0, -1), 1)
		elif char == ">":
			robotPos, grid = move(grid, robotPos, (0, 1), 1)
		elif char == "v":
			robotPos, grid = move(grid, robotPos, (1, 0), 1)

	for y, line in enumerate(grid):
		for x, char in enumerate(line):
			if char == 'O':
				part1 += 100 * y + x
	print(f"The answer to part 1 is: {part1}")


def adjustGrid(grid):
	adjustedGrid = list()
	for y, line in enumerate(grid):
		adjustedGrid.append(list())
		for x, char in enumerate(line):
			if char == "@":
				adjustedGrid[y].append('@')
				adjustedGrid[y].append('.')
			elif char == "O":
				adjustedGrid[y].append('[')
				adjustedGrid[y].append(']')
			else:
				adjustedGrid[y].append(char)
				adjustedGrid[y].append(char)
	return adjustedGrid


def main():
	with open("input") as file:
		lines = file.read().split("\n\n")

	part1 = 0
	part2 = 0
	map = lines[0].split("\n")
	for y,line in enumerate(map):
		x = line.find("@")
		if x != -1:
			robotPos = (y, x)
			break
	grid = newGrid(map)
	moves = ''.join(lines[1].split("\n"))
	solvePart1(grid, moves, robotPos)

	grid = newGrid(map)
	grid = adjustGrid(grid)
	for y, line in enumerate(grid):
		for x, char in enumerate(line):
			if char == "@":
				robotPos = (y, x)
				break

	i = 0
	for char in moves:
		if char == "^":
			robotPos, grid = move(grid, robotPos, (-1, 0), 2)
		elif char == "<":
			# print("p")
			robotPos, grid = move(grid, robotPos, (0, -1), 2)
		elif char == ">":
			robotPos, grid = move(grid, robotPos, (0, 1), 2)
		elif char == "v":
			robotPos, grid = move(grid, robotPos, (1, 0), 2)


	for y, line in enumerate(grid):
		for x, char in enumerate(line):
			if char == '[':
				part2 += 100 * y + x
	print(f"The answer to part 2 is: {part2}")

if __name__ == "__main__":
	main()