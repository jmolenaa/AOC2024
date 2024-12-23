from utils import *
import sys
from collections import defaultdict


def main(file):
	with open(file) as file:
		lines = file.read().split("\n")

	part1 = 0
	part2 = 0
	computers = defaultdict(list)
	for line in lines:
		computer1, computer2 = line.split('-')
		computers[computer1].append(computer2)
		computers[computer2].append(computer1)

	connectedTriplet = set()
	for key, values in computers.items():
		for value1 in values:
			for value2 in values:
				if value1 == value2:
					continue
				triplet = tuple(sorted([key, value1, value2]))
				if value2 in computers[value1] and triplet not in connectedTriplet:
					connectedTriplet.add(triplet)

	onlyT = set()
	for triplet in connectedTriplet:
		for value in triplet:
			if value[0] == 't':
				onlyT.add(triplet)
				break

	lanParties = set()
	for key, values in computers.items():
		currentLanParty = [key]
		for value1 in values:
			add = True
			for value2 in currentLanParty:
				if value2 not in computers[value1]:
					add = False
					break
			if add == True:
				currentLanParty.append(value1)
		lanParties.add(tuple(sorted(currentLanParty)))

	maxLanParty = ()
	for lanParty in lanParties:
		if len(lanParty) > len(maxLanParty):
			maxLanParty = lanParty

	print(f"The answer to part 1 is: {len(onlyT)}")
	print(f"The answer to part 2 is:")
	print(*maxLanParty, sep=',')


if __name__ == "__main__":
	if len(sys.argv) == 1:
		main("test_case")
	else:
		main(sys.argv[1])
