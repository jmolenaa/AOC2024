from utils import *
import time


def getComboOperand(i, A, B, C):
	if 0 <= i <= 3:
		return i
	elif i == 4:
		return A
	elif i == 5:
		return B
	elif i == 6:
		return C
	else:
		print("shouldnt happen")
		return i


def runProgram(program, A, B, C):
	output = ""
	i = 0
	while i < len(program):
		operation = int(program[i])
		litoperand = int(program[i + 1])
		comOperand = int(getComboOperand(int(program[i + 1]), A, B, C))
		if operation == 0:
			A = int(A / pow(2, comOperand))
		elif operation == 1:
			B = B ^ litoperand
		elif operation == 2:
			B = comOperand % 8
		elif operation == 3:
			if A != 0:
				i = litoperand
				continue
		elif operation == 4:
			B = B ^ C
		elif operation == 5:
			if output == "":
				output += str(comOperand % 8)
			else:
				output += "," + str(comOperand % 8)
		elif operation == 6:
			B = int(A / pow(2, comOperand))
		else:
			C = int(A / pow(2, comOperand))

		i += 2
	return output


def runIterations(program, startA, slice, iterators):
	A = startA
	i = 0
	prev = 0
	while True:
		output = runProgram(program, A, 0, 0)
		output = output.split(',')
		if output[:slice] == program[:slice]:
			print(A, A - prev)
			# print(i)
			prev = A
		if program == output:
			return A
		A += iterators[i]
		i = (i + 1) % len(iterators)
		# time.sleep(1)

# part1 is pretty straigthtforward
# part2 though is horrible
def main():
	with open("input") as file:
		lines = file.read().split("\n")

	part1 = 0
	part2 = 0
	for i, line in enumerate(lines):
		numbers = getNumsNeg(line)
		if i == 0:
			A = numbers[0]
		elif i == 1:
			B = numbers[0]
		elif i == 2:
			C = numbers[0]
		elif i == 4:
			program = line.split()[1].split(",")

	part1 = runProgram(program, A, B, C)
	minA = 1
	for i in range((len(program) - 1)):
		minA *= 8

	A = minA
	# runIterations(program, A, 5, [1])
	#
	# A = 35184373168565
	# iterators = [66824, 256, 63992, 1504520, 256, 261888, 256, 199160, 66824, 256, 63992, 1966080]
	# runIterations(program, A, 6, iterators)
	#
	# A = 35184375066301
	# iterators = [256, 2427384, 1766664, 256, 4194048]
	# runIterations(program, A, 7, iterators)
	#
	# A = 35184379260605
	# iterators = [256, 6621688, 1766664, 256, 8388352, 256, 8388352, 256, 8388352, 256, 8388352, 256, 8388352, 256,
	# 			 8388352, 256, 8388352]
	# runIterations(program, A, 8, iterators)
	#
	# A = 35184396037821
	# iterators = [256, 67108608, 256, 67108608, 256, 67108608, 256, 67108608, 256, 67108608, 256, 67108608, 256,
	# 			 67108608, 256, 67108608, 256, 67108608, 256, 67108608, 256, 67108608, 256, 58720000, 256, 8388352,
	# 			 256, 8388352, 256, 16776960, 256, 16776960, 256, 16776960, 256, 8388352, 256, 8388352, 256, 16776960,
	# 			 256, 16776960, 256, 25165568, 256, 67108608, 256, 67108608, 256, 67108608, 256, 67108608, 256,
	# 			 67108608, 256, 67108608, 256, 67108608, 256, 67108608, 256, 67108608, 256, 67108608, 256, 67108608,
	# 			 256, 67108608, 256, 67108608, 256, 56953336, 1766664, 256, 8388352, 256, 8388352, 256, 16776960, 256,
	# 			 16776960, 256, 15010296, 1766664, 256, 8388352, 256, 8388352, 256, 16776960, 256, 16776960, 256,
	# 			 15010296, 10155272, 256, 56953336, 10155272, 256, 67108608]
	# runIterations(program, A, 9, iterators)

	A = 35184396037821
	iterators = [256, 134217472, 256, 134217472, 256, 134217472, 256, 134217472, 256, 134217472, 256, 125828864, 256,
				 8388352, 256, 8388352, 256, 125828864, 256, 134217472, 256, 134217472, 256, 134217472, 256, 67108608,
				 256, 67108608, 256, 67108608, 256, 67108608, 256, 134217472, 256, 124062200, 1766664, 256, 8388352,
				 256, 8388352, 256, 125828864, 256, 134217472]
	part2 = runIterations(program, A, 10, iterators)

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	main()
