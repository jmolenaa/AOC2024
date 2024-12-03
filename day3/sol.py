import re


def calculateSolution(multiples):
	solution = 0
	for multiple in multiples:
		numbers = re.findall(r"\d+", multiple)
		solution += int(numbers[0]) * int(numbers[1])
	return solution


def main():
	with open("input") as file:
		line = file.read()

	multiples = re.findall(r"mul\(\d*,\d*\)", line)
	part1 = calculateSolution(multiples)

	multiples = list()
	i = 0
	off = False
	while True:
		dont = re.search(r"don't\(\)", line[i:])
		multiple = re.search(r"mul\(\d*,\d*\)", line[i:])
		if off is True:
			do = re.search(r"do\(\)", line[i:])
			if do is not None:
				i += do.end()
				off = False
			else:
				break
		elif multiple is None:
			break
		elif multiple is not None and dont is None or multiple.start() < dont.start():
			multiples.append(multiple.group())
			i += multiple.end()
		else:
			i += dont.end()
			off = True

	part2 = calculateSolution(multiples)

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	main()