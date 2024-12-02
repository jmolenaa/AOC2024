def check_validity(numbers):
	if numbers == sorted(numbers) or numbers == sorted(numbers, reverse=True):
		for number1, number2 in zip(numbers, numbers[1:]):
			diff = abs(number1 - number2)
			if diff == 0 or diff > 3:
				return False
		return True
	return False

def check_sorted(numbers):
	i = 0
	for number1, number2 in zip(numbers, numbers[1:]):
		diff = abs(number1 - number2)
		if number1 >= number2 or diff > 3:
			newNumbers = list(numbers)
			newNumbers.pop(i)
			if check_validity(newNumbers) == True:
				return True
			newNumbers = list(numbers)
			newNumbers.pop(i + 1)
			if check_validity(newNumbers) == True:
				return True
		i += 1
	return False

def check_reverse(numbers):
	i = 0
	for number1, number2 in zip(numbers, numbers[1:]):
		diff = abs(number1 - number2)
		if number1 <= number2 or diff > 3:
			newNumbers = list(numbers)
			newNumbers.pop(i)
			if check_validity(newNumbers) == True:
				return True
			newNumbers = list(numbers)
			newNumbers.pop(i + 1)
			if check_validity(newNumbers) == True:
				return True
		i += 1
	return False

def main():
	with open("input") as file:
		lines = file.read().split("\n")

	part1 = 0
	part2 = 0

	for line in lines:
		removed = 0
		numbers = list(map(int, line.split()))
		if check_validity(numbers) == True:
			part1 += 1
			part2 += 1
		elif check_sorted(numbers) or check_reverse(numbers):
			part2 += 1

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")

if __name__ == "__main__":
	main()