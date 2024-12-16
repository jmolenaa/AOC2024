from utils import *
import sys
minCost = 100000000000000
alreadyHappened = dict()
part2 = set()


def turn(dir):
	if dir == (0, 1):
		return (1, 0)
	elif dir == (1, 0):
		return (0, -1)
	elif dir == (0, -1):
		return (-1, 0)
	elif dir == (-1, 0):
		return (0, 1)


def makeStep(grid, pos : tuple, dir : tuple, positions: set, cost: int):
	global minCost
	global alreadyHappened
	if (pos, dir) in alreadyHappened and alreadyHappened[(pos, dir)] < cost:
		return
	alreadyHappened[(pos, dir)] = cost
	if cost > minCost:
		return
	if gridChar(grid, pos) == 'E':
		if cost < minCost:
			minCost = cost
		return
	newpositions = set(positions)
	i = 0
	newDir = tuple(dir)
	while i < 4:
		newPos = tuple(addPos(pos, newDir))
		if gridChar(grid, newPos) in {'.', 'E'} and newPos not in positions:
			cost += 1
			newpositions.add(newPos)
			makeStep(grid, newPos, newDir, newpositions, cost)
			newpositions.remove(newPos)
			cost -= 1
		if i < 2:
			cost += 1000
			newDir = turn(newDir)
			i += 1
		elif i > 1:
			cost -= 1000
			newDir = turn(newDir)
			i += 1


def makeStepPart2(grid, pos : tuple, dir : tuple, positions: set, cost: int):
	global minCost
	global alreadyHappened
	global part2
	if (pos, dir) in alreadyHappened and alreadyHappened[(pos, dir)] < cost:
		return
	alreadyHappened[(pos, dir)] = cost
	if cost > minCost:
		return
	if gridChar(grid, pos) == 'E':
		print("happens")
		if cost == minCost:
			part2.update(positions)
		return
	newpositions = set(positions)
	i = 0
	newDir = tuple(dir)
	while i < 4:
		newPos = tuple(addPos(pos, newDir))
		if gridChar(grid, newPos) in {'.', 'E'} and newPos not in positions:
			# print("no", newPos, newpositions)
			cost += 1
			newpositions.add(newPos)
			makeStepPart2(grid, newPos, newDir, newpositions, cost)
			newpositions.remove(newPos)
			cost -= 1
		if i < 2:
			cost += 1000
			newDir = turn(newDir)
			i += 1
		elif i > 1:
			cost -= 1000
			newDir = turn(newDir)
			i += 1


def main():
	with open("input") as file:
		lines = file.read().split("\n")

	# part1 = 0
	# part2 = 0
	pos = (len(lines) - 2, 1)
	dir = (0, 1)
	dirs = makeDirs()
	positions = set()
	positions.add(pos)
	sys.setrecursionlimit(5000)
	print(sys.getrecursionlimit())
	makeStep(lines, pos, dir, positions, 0)
	global alreadyHappened
	alreadyHappened = dict()
	print(minCost)
	makeStepPart2(lines, pos, dir, positions, 0)

		

	print(f"The answer to part 1 is: {minCost}")
	print(f"The answer to part 2 is: {len(part2)}")

if __name__ == "__main__":
	main()