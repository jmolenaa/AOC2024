from utils import inBounds, newGrid, addPositions
import re


def main():
	with open("input") as file:
		slotmachines = file.read().split("\n\n")

	part1 = 0
	part2 = 0
	for slotmachine in slotmachines:
		A, B, prize = slotmachine.split("\n")
		buttonA = (int(re.search(r'\d+', A).group()), int(A[A.find("Y") + 2:]))
		buttonB = (int(re.search(r'\d+', B).group()), int(B[B.find("Y") + 2:]))
		prize = (int(re.search(r'\d+', prize).group()), int(prize[prize.find("Y") + 2:]))
		minimumTokens = 2000
		for i in range(1, 101):
			for j in range(1, 101):
				if i * buttonA[0] + j * buttonB[0] == prize[0] and i * buttonA[1] + j * buttonB[1] == prize[1]:
					tokens = i * 3 + j
					if tokens < minimumTokens:
						minimumTokens = tokens
		if minimumTokens != 2000:
			part1 += minimumTokens

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")

if __name__ == "__main__":
	main()