from utils import *
import sys
import functools
positions = dict()


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
				while moveY > 0:
					inputs.append('^')
					moveY -= 1
			inputs.append('<')
			moveX -= 1
			i += 1
		while moveY > 0:
			inputs.append('^')
			moveY -= 1
		i = 0
		while moveY < 0:
			if buttonPosY == 4 and posX == 1 and i == 0:
				while moveX < 0:
					inputs.append('>')
					moveX += 1
			inputs.append('v')
			moveY += 1
			i += 1
		while moveX < 0:
			inputs.append('>')
			moveX += 1




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


# def directionalKeypad(code):
# 	keypad = {
# 					 '^': (1, 2), 'A': (1, 3),
# 		'<': (2, 1), 'v': (2, 2), '>': (2, 3),
# 	}
# 	pos = (1, 3)
# 	inputs = list()
# 	for char in code:
# 		buttonPosY, buttonPosX = keypad[char]
# 		posY, posX = pos
# 		moveY = posY - buttonPosY
# 		moveX = posX - buttonPosX
# 		i = 0
# 		while moveX > 0:
# 			if buttonPosX == 1 and posY == 1 and i == 0:
# 				inputs.append('v')
# 				moveY += 1
# 			inputs.append('<')
# 			moveX -= 1
# 			i += 1
# 		i = 0
# 		while moveY < 0:
# 			inputs.append('v')
# 			moveY += 1
# 			i += 1
# 		while moveX < 0:
# 			inputs.append('>')
# 			moveX += 1
# 		while moveY > 0:
# 			inputs.append('^')
# 			moveY -= 1
#
# 		# if posX > buttonPosX:
# 		# 	if buttonPosX != 1 or (buttonPosX == 1 and posY == 2):
# 		# 		inputs.extend('<' * (posX - buttonPosX))
# 		# 	if posY < buttonPosY:
# 		# 		inputs.extend('v' * (buttonPosY - posY))
# 		# 	else:
# 		# 		inputs.extend('^' * (posY - buttonPosY))
# 		# 	if buttonPosX == 1 and posY == 1:
# 		# 		inputs.extend('<' * (posX - buttonPosX))
# 		# else:
# 		# 	if posY > buttonPosY:
# 		# 		inputs.extend('>' * abs(posX - buttonPosX))
# 		# 		inputs.extend('^' * (posY - buttonPosY))
# 		# 	else:
# 		# 		inputs.extend('>' * abs(posX - buttonPosX))
# 		# 		inputs.extend('v' * (buttonPosY - posY))
# 		inputs.append('A')
# 		pos = keypad[char]
# 	return inputs


@functools.lru_cache(maxsize=None)
def getSequence(key, pos):
	keypad = {
					 '^': (1, 2), 'A': (1, 3),
		'<': (2, 1), 'v': (2, 2), '>': (2, 3),
	}
	sequence = list()
	buttonPosY, buttonPosX = keypad[key]
	posY, posX = pos
	moveY = posY - buttonPosY
	moveX = posX - buttonPosX
	i = 0
	while moveX > 0:
		if buttonPosX == 1 and posY == 1 and i == 0:
			# while moveY < 0:
			sequence.append('v')
			moveY += 1
		sequence.append('<')
		moveX -= 1
		i += 1
	i = 0
	while moveY > 0:
		if buttonPosY == 1 and posX == 1 and i == 0:
			while moveX < 0:
				sequence.append('>')
				moveX += 1
		sequence.append('^')
		moveY -= 1
		i += 1
	while moveY < 0:
		sequence.append('v')
		moveY += 1
		i += 1
	while moveX < 0:
		sequence.append('>')
		moveX += 1
	sequence.append('A')
	return sequence

@functools.lru_cache(maxsize=None)
def directionalKeypad(key, currentPos, i, robots):
	keypad = {
					 '^': (1, 2), 'A': (1, 3),
		'<': (2, 1), 'v': (2, 2), '>': (2, 3),
	}
	totalKeys = 0
	sequence = getSequence(key, positions[i])
	# print(sequence, sep='')
	if i == robots:
		return len(sequence)
	for nextKey in sequence:
		keysPressed = directionalKeypad(nextKey, positions[i + 1], i + 1, robots)
		totalKeys += keysPressed
		positions[i + 1] = keypad[nextKey]
	return totalKeys


def main(file):
	keypad = {
		'^': (1, 2), 'A': (1, 3),
		'<': (2, 1), 'v': (2, 2), '>': (2, 3),
	}
	with open(file) as file:
		lines = file.read().split("\n")

	part1 = 0
	part2 = 0
	# positions = dict()
	for line in lines:
		totalKeys = 0
		numericPart = getNumsNeg(line)[0]
		robotCode = numericKeypad(line)
		stringLength = 0
		prevRobot = robotCode
		for i in range(26):
			positions[i] = (1, 3)
		for key in robotCode:
			# print("next key", key)
			totalKeys += directionalKeypad(key, positions[1], 1, 2)
			positions[1] = keypad[key]
		part1 += totalKeys * numericPart
		totalKeys = 0
		# for i in range(25):
		for i in range(1, 26):
			positions[i] = (1, 3)
		for key in robotCode:
			# print("next key", key)
			totalKeys += directionalKeypad(key, positions[1], 1, 25)
			positions[1] = keypad[key]
			# break
		part2 += totalKeys * numericPart
		# break

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	if len(sys.argv) == 1:
		main("test_case")
	else:
		main(sys.argv[1])
