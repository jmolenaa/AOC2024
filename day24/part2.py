from utils import *
import sys
from collections import defaultdict, deque


def makeWire(c, i):
	if i < 10:
		return c + "0" + str(i)
	else:
		return c + str(i)


def getBinary(wires):
	wires.sort()
	wires.reverse()
	number = list()
	for wire in wires:
		number.append(wire[1])
	return ''.join(number)


def getZNumber(wireDict: defaultdict, gates: defaultdict):
	gatesHandled = set()
	while len(gatesHandled) != len(gates):
		for resultWire, operation in gates.items():
			wire1, operator, wire2 = operation
			if wire1 in wireDict and wire2 in wireDict:
				if operator == "XOR":
					wireDict[resultWire] = wireDict[wire1] ^ wireDict[wire2]
				elif operator == "OR":
					wireDict[resultWire] = wireDict[wire1] | wireDict[wire2]
				else:
					wireDict[resultWire] = wireDict[wire1] & wireDict[wire2]
				gatesHandled.add(resultWire)

	zWires = list()
	for wire, bit in wireDict.items():
		if wire[0] == 'z':
			zWires.append((wire, str(bit)))
	return getBinary(zWires)


def addGates(gatesAffected: defaultdict, gatesDict: defaultdict, zWire, currentWire):
	if currentWire[0] == 'x' or currentWire[0] == 'y':
		return
	gatesAffected[zWire].add(currentWire)
	# print(gates[currentWire])
	wire1, operator, wire2 = gatesDict[currentWire]
	addGates(gatesAffected, gatesDict, zWire, wire1)
	addGates(gatesAffected, gatesDict, zWire, wire2)


def printGatesWireIsInputFor(gatesDict, n, wireToCheck, gatesToPrint):
	if n == 0:
		return
	# wire1, operator, wire2 = gatesDict[wire]
	# print(wire1, operator, wire2, " = ", wire)
	# if wire1[0] != 'x' and wire1[0] != 'y':
	# 	printGatesAfter(gatesDict, n - 1, wire1)
	# if wire2[0] != 'x' and wire2[0] != 'y':
	# 	printGatesAfter(gatesDict, n - 1, wire2)
	nextWires = set()
	for wire, gate in gatesDict.items():
		wire1, operator, wire2 = gate
		if wire1 == wireToCheck or wire2 == wireToCheck:
			gatesToPrint.add((wire1, operator, wire2, wire))
			nextWires.add(wire)
	# if int(wire1[1:]) == wireNumber:
		#
		# 	print(gate, gatesDict[wire], )
	for wire in nextWires:
		printGatesWireIsInputFor(gatesDict, n - 1, wire, gatesToPrint)


def main(file):
	with open(file) as file:
		initialWires, gates = file.read().split("\n\n")

	part1 = 0
	part2 = 0
	wires = defaultdict()
	xWires, yWires = list(), list()
	for line in initialWires.split("\n"):
		wire, bit = line.split(':')
		if wire[0] == 'x':
			xWires.append((wire, bit[1]))
		else:
			yWires.append((wire, bit[1]))
		wires[wire] = int(bit)
	firstNumber = int(getBinary(xWires), 2)
	secondNumber = int(getBinary(yWires), 2)
	expectedResult = bin(firstNumber + secondNumber)[2:]
	print(firstNumber, secondNumber, expectedResult)

	gatesDict = defaultdict()
	for gate in gates.split("\n"):
		wire1, operator, wire2, dummy, resultWire = gate.split()
		gatesDict[resultWire] = (wire1, operator, wire2)
	number = getZNumber(wires.copy(), gatesDict)
	print(f"The answer to part 1 is: {int(number, 2)}")
	print(number)
	print(expectedResult)
	i = len(number) - 1
	gatesAffected = defaultdict(set)
	gatesThatWork = defaultdict(set)
	gatesforWire = defaultdict(set)
	for bit, expectedBit in zip(number, expectedResult):
		# print(i, bit, expectedBit)
		if bit != expectedBit:

			wire = makeWire("z", i)
			print(i)
			addGates(gatesAffected, gatesDict, wire, wire)
		else:
			wire = makeWire("z", i)
			addGates(gatesThatWork,gatesDict, wire, wire)
			# print(wire)
		addGates(gatesforWire, gatesDict, wire, wire)
		i -= 1

	# print(wire)
	mostCommon = set(gatesAffected["z44"])
	# print(len(mostCommon))
	# for wire, gates in gatesAffected.items():
	# 	mostCommon &= gates
	# print(len(mostCommon))
	for wire, gates in gatesThatWork.items():
		mostCommon -= gates
		# print(wire, gates)

	allGates = set()
	for i in range(1, len(number)):
		# gatesToPrint = gatesforWire[makeWire("z", i)] - gatesforWire[makeWire("z", i - 1)]
		# allGates.update(gatesToPrint)
		# print(gatesToPrint)
		print("\nFOR WIRE: ", makeWire("z", i))
		gatesToPrint = set()

		printGatesWireIsInputFor(gatesDict, 2, makeWire("x", i), gatesToPrint)
		for gate in gatesToPrint:
			wire1, operator, wire2, wire = gate
			print(wire1, operator, wire2, " = ", wire)


	# print(gatesforWire["z19"] - gatesforWire["z18"])
	# print(gatesforWire["z18"] - gatesforWire["z17"])
	# print(gatesforWire["z23"] - gatesforWire["z22"])
	# for wire, gates in gatesforWire.items():
	# 	print(wire, gates)
	# print(len(mostCommon))
	part2 = ["z12", "qdg", "z19", "vvf", "dck", "fgn", "z37", "nvh"]


	# print(*number, sep='')

	print(f"The answer to part 2 is:")
	print(*sorted(part2), sep=",")


if __name__ == "__main__":
	if len(sys.argv) == 1:
		main("test_case")
	else:
		main(sys.argv[1])
