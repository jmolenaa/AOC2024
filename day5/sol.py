from collections import defaultdict


# USE MAP FOR NUMBERS
def checkUpdate(numbers, rulesDict):
	updatedNumbers = list()

	for number in numbers:
		# gets the rules, if there are no rules for the number returns an empty list
		rules = rulesDict[number]
		newPageIndex = -1
		for i, prevNumber in enumerate(updatedNumbers):
			if prevNumber in rules:
				newPageIndex = i
				break
		# if the newPageIndex hasn't changed it means the current order of pages is correct
		if newPageIndex == -1:
			updatedNumbers.append(number)
		else:
			updatedNumbers.insert(newPageIndex, number)
	return updatedNumbers


def main():
	with open("input") as file:
		rules, updates = file.read().split("\n\n")

	part1 = 0
	part2 = 0
	updates = updates.split("\n")
	rulesDict = defaultdict(list)

	for rule in rules.split("\n"):
		page1, page2 = rule.split("|")
		rulesDict[page1].append(page2)

	for update in updates:
		numbers = update.split(",")
		updatedNumbers = checkUpdate(numbers, rulesDict)
		if updatedNumbers == numbers:
			part1 += int(numbers[int(len(numbers) / 2)])
		else:
			part2 += int(updatedNumbers[int(len(numbers) / 2)])
	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	main()