from utils import *
import sys
import functools
available_towels = set()


@functools.lru_cache(maxsize=None)
def lookForTowel(pattern: str, start: int, i: int):
	global available_towels
	possibilities = 0
	while i < len(pattern) + 1:
		if pattern[start:i] in available_towels:
			if i == len(pattern):
				return possibilities + 1
			possibilities += lookForTowel(pattern, i, i + 1)
		i += 1
	return possibilities


def main(file):
	with open(file) as file:
		lines = file.read().split("\n\n")

	global available_towels
	for towel in lines[0].split(", "):
		available_towels.add(towel)
	part2 = 0
	part1 = 0
	patterns = lines[1].split("\n")
	for j, pattern in enumerate(patterns):
		possibilities = lookForTowel(pattern, 0, 1)
		if possibilities != 0:
			part1 += 1
		part2 += possibilities

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	if len(sys.argv) == 1:
		main("test_case")
	else:
		main(sys.argv[1])
