from utils import *
import sys


def traverse(grid, pos, positions, shortestPath, alreadyHappened):
	# exit condition
	# if the set of positions holds less positions than the
	# shortestPath we've a shorter route
	if pos[0] == len(grid) - 1 and pos[1] == len(grid[0]) - 1:
		if len(positions) < shortestPath[0]:
			shortestPath[0] = len(positions)

	# optimizing checks:
	# we check the dictionary if we already reached this position
	# with a lower or equal cost (no point in trying this one again)
	if pos in alreadyHappened and alreadyHappened[pos] <= len(positions):
		return
	# if we already exceed the shortestPath, no point looking further
	if len(positions) > shortestPath[0]:
		return
	# if the path we've taken so far put us in a position
	# that in the best case scenario we would still exceed the shortestPath
	# we don't look further, f.e.
	# shortestPath is 350, we are at coordinates 50,50 and have visited 340 positions
	# best case scenario it would take 40 more steps to get to 70,70
	# so our best possible shortestPath is 380, which exceeds 350
	if (len(grid) - 1 - pos[0]) + (len(grid) - 1 - pos[1]) + len(positions) > shortestPath[0]:
		return

	# add to dict, or update dict with a lower cost
	alreadyHappened[pos] = len(positions)
	# copy positions, so we don't change our previous stack
	newPositions = positions.copy()
	newPositions.add(pos)
	dirs = makeDirs()
	for dir in dirs:
		newPos = tuple(addPos(pos, dir))
		if inBounds(grid, newPos) and gridChar(grid, newPos) == "." and newPos not in newPositions:
			traverse(grid, newPos, newPositions, shortestPath, alreadyHappened)


# traverses the map for the given amount of bytes
def traverseMapForByteNum(byteNum, lines):

	# create grid
	grid = [["."] * 71 for i in range(71)]

	# drop in bytes
	for line in lines[:byteNum]:
		bytePos = getNumsNeg(line)
		grid[bytePos[1]][bytePos[0]] = '#'

	# start recursion, have the shortest path as a list,
	# so we can change it in our function calls
	# starts at (0, 0), creates a set of positions we've visited
	# also makes a dict, where we will keep track of positions visited and their cost
	shortestPath = [1000000]
	traverse(grid, (0, 0), {(0, 0)}, shortestPath, dict())
	return shortestPath[0]


def main():
	with open("input") as file:
		lines = file.read().split("\n")

	sys.setrecursionlimit(5000)
	part1 = traverseMapForByteNum(1024, lines)

	# binary search, trying different byte numbers to narrow down
	# where the cutoff is
	# if we don't find a path we look to the left
	# if we do we look to the right
	low = 0
	high = len(lines)
	while low <= high:
		mid = low + int((high - low) / 2)
		shortestPath = traverseMapForByteNum(mid, lines)
		if shortestPath == 1000000:
			high = mid - 1
		else:
			low = mid + 1

	# Haven't confirmed this, but I believe we can exit the binary search
	# with either the first byte number that will block off the path
	# or the last byte number that doesn't block it off
	# so this last check is to see which case happens
	# if for the current mid, we can't find a path, then
	# this is the first byte that blocks it off
	# now, due to how slices work, we need to grab mid -1
	if traverseMapForByteNum(mid, lines) == 1000000:
		part2 = lines[mid - 1]
	else:
		part2 = lines[mid]
	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	main()