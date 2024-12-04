def findWord(x: int, y: int, lines, xinc: int, yinc: int):
	lineLen = int(len(lines[0]))
	lineHeight = int(len(lines))
	if x + xinc * 3 >= lineLen or y + yinc * 3 >= lineHeight or x + xinc * 3 < 0 or y + yinc * 3 < 0:
		return 0
	if lines[y][x] == 'X' and \
			lines[y + yinc][x + xinc] == 'M' and \
			lines[y + yinc * 2][x + xinc * 2] == 'A' and \
			lines[y + yinc * 3][x + xinc * 3] == 'S':
		return 1
	return 0


def findWords(x: int, y: int, lines):
	amount = 0
	amount += findWord(x, y, lines, 1, 0)
	amount += findWord(x, y, lines, -1, 0)
	amount += findWord(x, y, lines, 0, 1)
	amount += findWord(x, y, lines, 0, -1)
	amount += findWord(x, y, lines, 1, 1)
	amount += findWord(x, y, lines, 1, -1)
	amount += findWord(x, y, lines, -1, -1)
	amount += findWord(x, y, lines, -1, 1)
	return amount


def oneMas(x:int, y:int, lines):
	if lines[y][x] == 'A' and lines[y + 1][x + 1] == 'S' and lines[y - 1][x - 1] == 'M' or \
			lines[y][x] == 'A' and lines[y + 1][x + 1] == 'M' and lines[y - 1][x - 1] == 'S':
		return True
	return False


def secondMas(x:int, y:int, lines):
	if lines[y][x] == 'A' and lines[y + 1][x - 1] == 'S' and lines[y - 1][x + 1] == 'M' or \
			lines[y][x] == 'A' and lines[y + 1][x - 1] == 'M' and lines[y - 1][x + 1] == 'S':
		return True
	return False


def findXmas(x: int, y: int, lines):
	lineLen = int(len(lines[0]))
	lineHeight = int(len(lines))
	if x + 1 >= lineLen or y + 1 >= lineHeight or x - 1 < 0 or y - 1 < 0:
		return 0
	if oneMas(x, y, lines) and secondMas(x, y, lines):
		return 1
	return 0


# USE MAP FOR NUMBERS
def main():
	with open("input") as file:
		lines = file.read().split("\n")

	part1 = 0
	part2 = 0
	for y, line in enumerate(lines):
		for x, char in enumerate(line):
			part1 += findWords(x, y, lines)
			part2 += findXmas(x, y, lines)

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	main()