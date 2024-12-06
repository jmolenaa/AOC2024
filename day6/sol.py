def tryStep(grid, pos, dir):
	if pos[0] + dir[0] < 0 or pos[0] + dir[0] >= len(grid) or \
		pos[1] + dir[1] < 0 or pos[1] + dir[1] >= len(grid[0]):
		return 2
	newPos = [pos[0], pos[1]]
	dy,dx = dir
	newPos[0] = newPos[0] + dy
	newPos[1] = newPos[1] + dx
	if grid[newPos[0]][newPos[1]] == '#':
		return 0
	return 1


def tryWalk(grid, pos, dir):
	while True:
		if tryStep(grid, pos, dir) == 1:
			pos[0] = pos[0] + dir[0]
			pos[1] = pos[1] + dir[1]
			grid[pos[0]][pos[1]] = 'x'
			break
		elif tryStep(grid, pos, dir) == 2:
			return grid, [-1, -1], dir
		else:
			if dir == [-1, 0]:
				dir = [0, 1]
			elif dir == [0, 1]:
				dir = [1, 0]
			elif dir == [1, 0]:
				dir = [0, -1]
			elif dir == [0, -1]:
				dir = [-1, 0]

	# if dir == 1:
	# 	if pos[0] - 1 >= 0 and lines[pos[0] - 1][pos[1]] == '.':
	return grid, pos, dir

def tryWalkObs(grid, pos, dir):
	while True:
		if tryStep(grid, pos, dir) == 1:
			pos[0] = pos[0] + dir[0]
			pos[1] = pos[1] + dir[1]
			grid[pos[0]][pos[1]] = 'x'
			break
		elif tryStep(grid, pos, dir) == 2:
			return grid, [-1, -1], dir
		else:
			if dir == [-1, 0]:
				dir = [0, 1]
			elif dir == [0, 1]:
				dir = [1, 0]
			elif dir == [1, 0]:
				dir = [0, -1]
			elif dir == [0, -1]:
				dir = [-1, 0]

	# if dir == 1:
	# 	if pos[0] - 1 >= 0 and lines[pos[0] - 1][pos[1]] == '.':
	return grid, pos, dir


def main():
	with open("input") as file:
		lines = file.read().split("\n")

	part1 = 0
	part2 = 0

	grid = list()
	for y, line in enumerate(lines):
		grid.append(list())
		for x, char in enumerate(line):
			grid[y].append(char)
			if char == '^':
				pos = [y, x]
	dir = [-1, 0]
	while True:
		grid, pos, dir = tryWalk(grid, pos, dir)
		if pos == [-1, -1]:
			break

	for line in grid:
		for char in line:
			if char == '^' or char == 'x':
				part1 += 1

	grid = list()
	for y, line in enumerate(lines):
		grid.append(list())
		for x, char in enumerate(line):
			grid[y].append(char)
			if char == '^':
				pos = [y, x]
	dir = [-1, 0]
	startpos = pos
	pos[0] = pos[0] - 1
	while True:
		grid, pos, dir, obstacle = tryWalkObs(grid, pos, dir, startpos)
		if pos == [-1, -1]:
			break
		if obstacle is True:
			part2 += 1

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")

if __name__ == "__main__":
	main()