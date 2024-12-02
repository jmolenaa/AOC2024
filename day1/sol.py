def main():
	with open("input") as file:
		lines = file.read().split("\n")

	list1 = list()
	list2 = list()
	for line in lines:
		numbers = line.split()
		list1.append(numbers[0])
		list2.append(numbers[1])
	
	list1.sort()
	list2.sort()
	part1 = 0
	part2 = 0
	for i, num in enumerate(list1):
		amount = list2.count(num)
		part2 += int(num) * int(amount)
		part1 += abs(int(list1[i]) - int(list2[i]))


	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")

if __name__ == "__main__":
	main()