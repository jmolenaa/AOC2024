from utils import *
import sys


def turn(dir):
	turns = {
		(0, 1): (1, 0),
		(1, 0): (0, -1),
		(0, -1): (-1, 0),
		(-1, 0): (0, 1)
	}
	return turns[dir]


def makeStep(grid, pos : tuple, dir : tuple, positions: set, cost: int, minScore, alreadyHappened: dict, seats: set):

	# check if we reached the end,
	# update the lowest score if the current one is lower than the previous lowest
	# also, clear seats, since the previous lowest score isn't valid
	# if our current score is equal to the minimum score, add the positions
	# through which we got to the seats set
	if gridChar(grid, pos) == 'E':
		if cost < minScore[0]:
			minScore[0] = cost
			seats.clear()
		if cost == minScore[0]:
			seats.update(positions)
		return

	# checks if current position and direction were already visited
	# if the cost we had in the previous visit was lower than now,
	# there's no point continuing down this path since the final score will always be higher
	# if the current score is lower or we haven't visited we cache the current state
	if (pos, dir) in alreadyHappened and alreadyHappened[(pos, dir)] < cost:
		return
	alreadyHappened[(pos, dir)] = cost

	# no point continuing if we already exceeded our minimum score
	if cost > minScore[0]:
		return

	# keep set of newpositions so we don't change the positions of the previous iteration
	newpositions = set(positions)
	newDir = tuple(dir)
	# makes steps in every direction as long as there is a spot free and
	# we haven't visited that spot in the current route
	# the first two turns add 1000 to the cost, the third one reduces it by 1000
	# this is because we can turn clockwise instead of 3 times counterclockwise
	for i in range(4):
		newPos = tuple(addPos(pos, newDir))
		if gridChar(grid, newPos) in {'.', 'E'} and newPos not in positions:
			newpositions.add(newPos)
			makeStep(grid, newPos, newDir, newpositions, cost + 1, minScore, alreadyHappened, seats)
			newpositions.remove(newPos)

		newDir = turn(newDir)
		if i < 2:
			cost += 1000
		else:
			cost -= 1000


def main():
	with open("input") as file:
		grid = file.read().split("\n")

	startPos = (len(grid) - 2, 1)
	startDir = (0, 1)
	positions = {startPos}

	sys.setrecursionlimit(5000)

	minScore = [100000000000000]
	# caching dictionary, keys are positions and directions, values are the cost on that spot
	alreadyHappened = dict()
	# set keeping track of positions on lowest cost routes
	seats = set()

	makeStep(grid, startPos, startDir, positions, 0, minScore, alreadyHappened, seats)

	print(f"The answer to part 1 is: {minScore[0]}")
	print(f"The answer to part 2 is: {len(seats)}")

if __name__ == "__main__":
	main()