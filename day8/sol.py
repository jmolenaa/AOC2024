from collections import defaultdict


def inBounds(grid, pos):
	if pos[0] < 0 or pos[0] >= len(grid) or \
			pos[1] < 0 or pos[1] >= len(grid[0]):
		return False
	return True


# checks for the two antinode spots for part1
def addantinodespart1(coordinate1, coordinate2, grid):
	xdiff = coordinate1[1] - coordinate2[1]
	ydiff = coordinate1[0] - coordinate2[0]
	antinode1 = [coordinate1[0] + ydiff, coordinate1[1] + xdiff]
	antinode2 = [coordinate2[0] - ydiff, coordinate2[1] - xdiff]
	if inBounds(grid, antinode1):
		grid[antinode1[0]][antinode1[1]] = "#"
	if inBounds(grid, antinode2):
		grid[antinode2[0]][antinode2[1]] = "#"


# loops until out of bounds setting antinodes as $
def adddirection(grid, antinode, xdiff, ydiff):
	while inBounds(grid, antinode):
		if grid[antinode[0]][antinode[1]] != "#":
			grid[antinode[0]][antinode[1]] = "$"
		antinode = [antinode[0] + ydiff, antinode[1] + xdiff]


# takes the coordinates of the first antenna and goes in
# the line defined by the two antennas in both directions
# every xdiff and ydiff will put down a $ signifying a new antinode
def addantinodespart2(coordinate1, coordinate2, grid):
	xdiff = coordinate1[1] - coordinate2[1]
	ydiff = coordinate1[0] - coordinate2[0]
	adddirection(grid, coordinate1, xdiff, ydiff)
	adddirection(grid, coordinate1, -xdiff, -ydiff)


def main():
	with open("input") as file:
		lines = file.read().split("\n")

	part1 = 0
	part2 = 0

	# make grid that is changeable
	grid = list()
	for y, line in enumerate(lines):
		grid.append(list())
		for x, char in enumerate(line):
			grid[y].append(char)

	# create a dictionary of antennas
	# the key is the digit or letter corresponding to the antenna
	# the value is a list containing coordinates that hold that antenna
	antennas = defaultdict(list)
	for y, line in enumerate(grid):
		for x, char in enumerate(line):
			if char != '.':
				antennas[char].append((y, x))

	# loop through the dictionary and for each type of antenna
	# loops through the list containing the coordinates of that antenna
	# then loops through the list again matching the antenna with every other antenna
	# for each pair of antennas will adjust the grid for part1 and part2
	for coordinates in antennas.values():
		for i, coordinate1 in enumerate(coordinates):
			for coordinate2 in coordinates[i + 1:]:
				addantinodespart1(coordinate1, coordinate2, grid)
				addantinodespart2(coordinate1, coordinate2, grid)

	# after changing the grid it's a matter of calculating
	# the # symbol for part1 and the # and $ symbols for part2
	for line in grid:
		for char in line:
			if char == "#":
				part1 += 1
				part2 += 1
			if char == "$":
				part2 += 1


	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	main()
