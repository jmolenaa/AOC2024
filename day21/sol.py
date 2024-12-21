from utils import *
import sys


def numericKeypad(line):
	keypad = {
		'7': (1, 1), '8': (1, 2), '9': (1, 3),
		'4': (2, 1), '5': (2, 2), '6': (2, 3),
		'1': (3, 1), '2': (3, 2), '3': (3, 3),
					 '0': (4, 2), 'A': (4, 3),
	}
	pos = (4, 3)
	inputs = list()
	for char in line:
		# print(char)
		buttonPosY, buttonPosX = keypad[char]
		posY, posX = pos
		moveY = posY - buttonPosY
		moveX = posX - buttonPosX
		i = 0
		while moveX > 0:
			if buttonPosX == 1 and posY == 4 and i == 0:
				inputs.append('^')
				moveY -= 1
			inputs.append('<')
			moveX -= 1
			i += 1
		i = 0
		while moveY < 0:
			if buttonPosY == 4 and posX == 1 and i == 0:
				inputs.append('>')
				moveX += 1
			inputs.append('v')
			moveY += 1
			i += 1
		while moveX < 0:
			inputs.append('>')
			moveX += 1
		while moveY > 0:
			inputs.append('^')
			moveY -= 1




		# if posX > buttonPosX:
		# 	if buttonPosX != 1 or (buttonPosX == 1 and posY < 4):
		# 		inputs.extend('<' * (posX - buttonPosX))
		# 	if posY > buttonPosY:
		# 		inputs.extend('^' * (posY - buttonPosY))
		# 	else:
		# 		inputs.extend('v' * (buttonPosY - posY))
		# 	if buttonPosX == 1 and posY == 4:
		# 		inputs.extend('<' * (posX - buttonPosX))
		# else:
		# 	if posY > buttonPosY:
		# 		inputs.extend('>' * abs(posX - buttonPosX))
		# 		inputs.extend('^' * (posY - buttonPosY))
		# 	else:
		# 		if buttonPosY != 4:
		# 			inputs.extend('v' * (buttonPosY - posY))
		# 		inputs.extend('>' * abs(posX - buttonPosX))
		# 		if buttonPosY == 4:
		# 			inputs.extend('v' * (buttonPosY - posY))

		inputs.append('A')
		pos = keypad[char]
	return inputs


def directionalKeypad(code):
	keypad = {
					 '^': (1, 2), 'A': (1, 3),
		'<': (2, 1), 'v': (2, 2), '>': (2, 3),
	}
	pos = (1, 3)
	inputs = list()
	for char in code:
		buttonPosY, buttonPosX = keypad[char]
		posY, posX = pos
		moveY = posY - buttonPosY
		moveX = posX - buttonPosX
		i = 0
		while moveX > 0:
			if buttonPosX == 1 and posY == 1 and i == 0:
				inputs.append('v')
				moveY += 1
			inputs.append('<')
			moveX -= 1
			i += 1
		i = 0
		while moveY < 0:
			inputs.append('v')
			moveY += 1
			i += 1
		while moveX < 0:
			inputs.append('>')
			moveX += 1
		while moveY > 0:
			inputs.append('^')
			moveY -= 1

		# if posX > buttonPosX:
		# 	if buttonPosX != 1 or (buttonPosX == 1 and posY == 2):
		# 		inputs.extend('<' * (posX - buttonPosX))
		# 	if posY < buttonPosY:
		# 		inputs.extend('v' * (buttonPosY - posY))
		# 	else:
		# 		inputs.extend('^' * (posY - buttonPosY))
		# 	if buttonPosX == 1 and posY == 1:
		# 		inputs.extend('<' * (posX - buttonPosX))
		# else:
		# 	if posY > buttonPosY:
		# 		inputs.extend('>' * abs(posX - buttonPosX))
		# 		inputs.extend('^' * (posY - buttonPosY))
		# 	else:
		# 		inputs.extend('>' * abs(posX - buttonPosX))
		# 		inputs.extend('v' * (buttonPosY - posY))
		inputs.append('A')
		pos = keypad[char]
	return inputs




def main(file):
	with open(file) as file:
		lines = file.read().split("\n")

	part1 = 0
	part2 = 0
	for line in lines:
		numericPart = getNumsNeg(line)[0]
		firstRobotCode = numericKeypad(line)
		secondRobotCode = directionalKeypad(firstRobotCode)
		thirdRobotCode = directionalKeypad(secondRobotCode)
		# print(*firstRobotCode, len(firstRobotCode), sep='')
		# print(*secondRobotCode, len(secondRobotCode), sep='')
		# print(*thirdRobotCode, len(thirdRobotCode), sep='')
		part1 += len(thirdRobotCode) * numericPart
		# print(numericPart)
		# break

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	if len(sys.argv) == 1:
		main("test_case")
	else:
		main(sys.argv[1])
