from utils import *
import sys
from collections import deque, Counter


def main(file):
	with open(file) as file:
		lines = file.read().split("\n")

	part1 = 0
	part2 = 0

	bananasForPattern = Counter()
	for line in lines:
		secret_number = getNumsNeg(line)[0]
		prices = deque()
		prices.append(secret_number % 10)
		for i in range(2000):
			secret_number = ((secret_number * 64) ^ secret_number) % 16777216
			secret_number = ((int(secret_number / 32)) ^ secret_number) % 16777216
			secret_number = ((secret_number * 2048) ^ secret_number) % 16777216

			prices.append(secret_number % 10)
		part1 += secret_number

		sequence = deque()
		for i in range(3):
			sequence.append(prices[1] - prices.popleft())

		sequenceSeen = set()
		while len(prices) > 1:
			sequence.append(prices[1] - prices.popleft())
			sequenceTuple = tuple(sequence)
			if sequenceTuple not in sequenceSeen:
				bananasForPattern[sequenceTuple] += prices[0]
				sequenceSeen.add(sequenceTuple)
			sequence.popleft()

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {max(bananasForPattern.values())}")


if __name__ == "__main__":
	if len(sys.argv) == 1:
		main("test_case")
	else:
		main(sys.argv[1])
