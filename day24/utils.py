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


def makeDirs():
	return [(0, 1), (0, -1), (1, 0), (-1, 0)]
	# for dy, dx in directions:
	# 	new_y, new_x = y + dy, x + dx


def addPos(pos1, pos2):
	return (pos1[0] + pos2[0], pos1[1] + pos2[1])


def subPos(pos1, pos2):
	return (pos1[0] - pos2[0], pos1[1] - pos2[1])


def getNums(line: str):
	return list(map(int, re.findall(r"-*\d+", line)))


def getNumsStr(line: str):
	return re.findall(r"\d+", line)


def getNumsNeg(line: str):
	return list(map(int, re.findall(r"-*\d+", line)))


def getNumsStrNeg(line: str):
	return re.findall(r"-*\d+", line)


def gridChar(grid, pos):
	return grid[pos[0]][pos[1]]


def setGridChar(grid, pos, char):
	grid[pos[0]][pos[1]] = char


def findInGrid(grid, charToFind):
	for y, line in enumerate(grid):
		for x, char in enumerate(line):
			if char == charToFind:
				return (y, x)

def distance(pos1, pos2):
	return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])