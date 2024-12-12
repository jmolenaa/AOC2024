from utils import inBounds, makeDirections


# recursive function, adds the current coordinate to the region plot
# then checks every direction around the coordinates
# if a plot next to the current plot was already in the region we skip it
# if a plot is in the bounds of the map and is of the same plant type
# we increase the area and call this function again with the new plot
# if none of these are true, we are either outside the bounds
# or we have a different plant, both cases mean we have a perimeter
# so we add the current position and the direction it is in to the perimeter set
def calculateRegion(grid, regionPlots: set, area: list[int], perimeters: set, y: int, x: int, plant):
	regionPlots.add((y, x))
	directions = makeDirections()
	for dy, dx in directions:
		new_y, new_x = y + dy, x + dx
		if (new_y, new_x) in regionPlots:
			continue
		elif inBounds(grid, (new_y, new_x)) and grid[new_y][new_x] == plant:
			area[0] += 1
			calculateRegion(grid, regionPlots, area, perimeters, new_y, new_x, plant)
		else:
			perimeters.add(((new_y, new_x), (dy, dx)))


def removePerimeters(perimeters: set, direction: tuple, pos: tuple, dy: int, dx: int):
	i = 1
	while ((pos[0] + dy * i, pos[1] + dx * i), direction) in perimeters:
		perimeters.remove(((pos[0] + dy * i, pos[1] + dx * i), direction))
		i += 1


# in this function we loop until all perimeters have been removed from the set
# we first pop a random perimeter, then we check how it's oriented towards the region
# if the perimeter is below or above the region, it's orientation is horizontal
# if it's to the left or to the right, it's vertical
# next depending on orientation we remove all perimeters that
# have the same orientation and are next to the current perimeter
# f.e. if our perimeter has pos (1,2) and dir (-1,0) it's oriented horizontally
# therefore we try to remove all the ones next to it that are horizontal,
# like (1,3) (1,4) (1,1), we wouldn't remove (1,6), because it's not next to the other ones
# vertical it's the same, but we check the y direction
# once we've removed everything we add one side and move to the next perimeter
def calculatePart2(area: int, perimeters: set):
	sides = 0
	while len(perimeters) != 0:
		perimeter = perimeters.pop()
		pos, direction = perimeter
		if direction[0] == -1 or direction[0] == 1:
			# direction right, then left
			removePerimeters(perimeters, direction, pos, 0, 1)
			removePerimeters(perimeters, direction, pos, 0, -1)
		else:
			# direction down, then up
			removePerimeters(perimeters, direction, pos, 1, 0)
			removePerimeters(perimeters, direction, pos, -1, 0)
		sides += 1
	return sides * area


def main():
	with open("input") as file:
		lines = file.read().split("\n")

	part1 = 0
	part2 = 0
	plotsVisited = set() # set containing all plots we've already visited
	for y, line in enumerate(lines):
		for x, char in enumerate(line):
			# skip plots we already visited
			if (y, x) in plotsVisited:
				continue

			# hold plots of current region
			regionPlots = set()
			# area of current region, is list so we can change it easily in outside functions
			# starts at 1, cause that's the plant we're on currently
			area = [1]
			# set of tuples containing perimeter coordinates
			# plus the perpendicular direction to the region
			# f.e. A |, would have coordinates (0,0) and direction (0,1)
			perimeters = set()

			# calculates region area and perimeters
			calculateRegion(lines, regionPlots, area, perimeters, y, x, lines[y][x])
			# we update the visited plots with all the plots
			# from the area currently being evaluated
			plotsVisited.update(regionPlots)

			# just the area multiplied by amount of perimeters
			part1 += area[0] * len(perimeters)
			part2 += calculatePart2(area[0], perimeters)

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	main()