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


	# for dy, dx in directions:
	# 	new_y, new_x = y + dy, x + dx
