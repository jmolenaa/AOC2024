from utils import *
import math


def calculatePart1(robots, tall, wide):
	quadrants = [0, 0, 0, 0]
	for robot in robots:
		pos, vel = robot
		if pos[0] < int(tall / 2) and pos[1] < int(wide / 2):
			quadrants[0] += 1
		elif pos[0] > int(tall / 2) and pos[1] < int(wide / 2):
			quadrants[1] += 1
		elif pos[0] < int(tall / 2) and pos[1] > int(wide / 2):
			quadrants[2] += 1
		elif pos[0] > int(tall / 2) and pos[1] > int(wide / 2):
			quadrants[3] += 1
	return math.prod(quadrants)



def printGridToFile(robots, grid, second: str, file):
	# truncate file when writing the first time, otherwise append
	for robot in robots:
		pos, vel = robot
		grid[pos[0]][pos[1]] = '#'
	file.write("\nsecond " + second + "\n")
	for line in grid:
		file.write(''.join(line) + "\n")


def main():
	with open("input") as file:
		lines = file.read().split("\n")

	robots = list()
	for line in lines:
		numbers = getNumbersIntNegative(line)
		# grid has coordinate [y][x] and the input has it the other way around
		# that's why we have the weird order of numbers
		robots.append(([numbers[1], numbers[0]], (numbers[3], numbers[2])))

	tall = 103
	wide = 101
	grid = [["."] * wide for i in range(tall)]

	file = open("check", "w")
	print("Will be writing grid to the file 'check', you can use ctrl+f and search for multiple '#' to find the christmas tree")
	# originally checked 100000, but looks like 10000 is enough for the
	# tree to appear, doing 20000 just in case
	for i in range(20000):
		newrobots = list()
		for robot in robots:
			pos, vel = robot
			newpos = addPositions(pos, vel)
			if inBounds(grid, newpos):
				robot = (newpos, vel)
			else:
				robot = ((newpos[0] % tall, newpos[1] % wide), vel)
			newrobots.append(robot)
		robots = newrobots
		printGridToFile(robots, newGrid(grid), str(i + 1), file)
		if i == 99:
			print(f"The answer to part 1 is: {calculatePart1(robots, tall, wide)}")

if __name__ == "__main__":
	main()