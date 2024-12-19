from utils import *
import sys


def main(file):
	with open(file) as file:
		lines = file.read().split("\n")

	part1 = 0
	part2 = 0
	for line in lines:
		numbers = getNumsNeg(line)

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	if len(sys.argv) == 1:
		main("test_case")
	else:
		main(sys.argv[1])
