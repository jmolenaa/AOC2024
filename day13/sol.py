from utils import inBounds, newGrid
import re


# so the formula is derived from two functions:
# func1 : A[X] * pressA + B[X] * pressB = prize[X]
# func2 : A[Y] * pressA + B[Y] * pressB = prize[Y]
# pretty much however much we press A and B will move the claw
# in the X axis, we need the presses to reach the prize on the X axis
# same for the Y axis
# in this formula we're missing only pressA and pressB, so we solve for those

# first I rearrange func1, so I have the definition of pressA
# first I subtract B[X] * pressB from both sides
# -> A[X] * pressA = prize[X] - B[X] * pressB
# then I divide by A[X]
# -> pressA = (prize[X] - B[X] * pressB) / A[X]

# now I apply the definition of pressA to func2
# -> A[Y] * (prize[X] - B[X] * pressB) / A[X] + B[Y] * pressB = prize[Y]
# now I only have pressB as an unknown, so I solve for it
# first I multiply both sides by A[X]
# -> A[Y] * (prize[X] - B[X] * pressB) + B[Y] * pressB * A[X] = prize[Y] * A[X]
# then I get rid of the brackets
# -> A[Y] * prize[X] - A[Y] * B[X] * pressB + B[Y] * pressB * A[X] = prize[Y] * A[X]
# now I subtract both sides with A[Y] * prize[X]
# -> - A[Y] * B[X] * pressB + B[Y] * pressB * A[X] = prize[Y] * A[X] - A[Y] * prize[X]
# I rearrange the left side, so the (- A[Y] * B[X] * pressB) is second, so we have the minus in a nicer spot
# -> B[Y] * pressB * A[X] - A[Y] * B[X] * pressB = prize[Y] * A[X] - A[Y] * prize[X]
# then I pull pressB in front of brackets, putting the other variables inside brackets
# -> pressB * (B[Y] * A[X] - A[Y] * B[X]) = prize[Y] * A[X] - A[Y] * prize[X]
# now I divide both sides by (B[Y] * A[X] - A[Y] * B[X])
# -> pressB = (prize[Y] * A[X] - A[Y] * prize[X]) / (B[Y] * A[X] - A[Y] * B[X])
# now that we have pressB, we can use the earlier formula for pressA to calculate it
# -> pressA = (prize[X] - B[X] * pressB) / A[X]

def calculateButtonPresses(prize, A, B):
	X, Y = 0, 1  # for readability
	pressB = (prize[Y] * A[X] - A[Y] * prize[X]) / (B[Y] * A[X] - A[Y] * B[X])
	pressA = (prize[X] - B[X] * pressB) / A[X]
	return pressA, pressB


def calculateTokens(prize, A, B):
	pressA, pressB = calculateButtonPresses(prize, A, B)
	# check if our result is an integer, if it's not, it's not possible to get the prize
	if int(pressB) == pressB and int(pressA) == pressA:
		return int(pressB + pressA * 3)
	return 0


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

		part1 += calculateTokens(prize, buttonA, buttonB)
		part2 += calculateTokens([prize[0] + 10000000000000, prize[1] + 10000000000000], buttonA, buttonB)

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")

if __name__ == "__main__":
	main()