from utils import *


def main():
	with open("input") as file:
		lines = file.read().split("\n")

	part1 = 0
	part2 = 0
	for line in lines:
		numbers = getNumbersInt(line)
		

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")

if __name__ == "__main__":
	main()