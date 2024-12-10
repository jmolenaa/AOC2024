from utils import inBounds, makeDirections


def counttrailhead(lines: list[str], x: int, y: int, trails: set, rating: list, height: int):
	if height == 9:
		trails.add((y, x))
		rating[0] += 1
		return

	directions = makeDirections()
	for dy, dx in directions:
		newY = y + dy
		newX = x + dx
		if inBounds(lines, [newY, newX]) and int(lines[newY][newX]) == height + 1:
			counttrailhead(lines, newX, newY, trails, rating, height + 1)


def main():
	with open("input") as file:
		lines = file.read().split("\n")

	part1 = 0
	part2 = 0
	# just bruteforce all the trails with recursion
	# ways of reaching the highest point are kept in a set
	# whenever we reach the highest point we add it to the set
	# the set contains every point only once
	# rating will keep track of any way to reach any highest point
	# it's a list so I can change it from other function calls
	for y, line in enumerate(lines):
		for x, char in enumerate(line):
			if char == "0":
				trails = set()
				rating = [0]
				counttrailhead(lines, x, y, trails, rating,  0)
				part1 += len(trails)
				part2 += rating[0]

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")

if __name__ == "__main__":
	main()