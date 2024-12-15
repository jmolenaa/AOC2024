import re


def inBounds(grid, pos):
	if pos[0] < 0 or pos[0] >= len(grid) or \
			pos[1] < 0 or pos[1] >= len(grid[0]):
		return False
	return True


def newGrid(grid):
	newgrid = list()
	for y, line in enumerate(grid):
		newgrid.append(list())
		for x, char in enumerate(line):
			newgrid[y].append(char)
	return newgrid


def makeDirections():
	return [(0, 1), (0, -1), (1, 0), (-1, 0)]


def addPositions(pos1, pos2):
	return [pos1[0] + pos2[0], pos1[1] + pos2[1]]


def subtractPositions(pos1, pos2):
	return [pos1[0] - pos2[0], pos1[1] - pos2[1]]


def getNumbers(line: str):
	return re.findall(r"\d+", line)


def getNumbersInt(line: str):
	return list(map(int, re.findall(r"-*\d+", line)))


def getNumbersNegative(line: str):
	return re.findall(r"-*\d+", line)


def getNumbersIntNegative(line: str):
	return list(map(int, re.findall(r"-*\d+", line)))
	# for dy, dx in directions:
	# 	new_y, new_x = y + dy, x + dx


def getGridChar(grid, pos):
	return grid[pos[0]][pos[1]]


def setGridChar(grid, pos, char):
	grid[pos[0]][pos[1]] = char
