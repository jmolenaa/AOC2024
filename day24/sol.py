from utils import *
import sys
from collections import defaultdict, deque


def main(file):
	with open(file) as file:
		initialWires, gates = file.read().split("\n\n")

	part1 = 0
	part2 = 0
	wires = defaultdict()
	for line in initialWires.split("\n"):
		wire, bit = line.split(':')
		wires[wire] = int(bit)

	gatesQueue = set(gates.split("\n"))
	gatesHandled = set()
	while gatesQueue:
		for gate in gatesQueue:
			wire1, operator, wire2, dummy, resultWire = gate.split()
			if wire1 in wires and wire2 in wires:
				if operator == "XOR":
					wires[resultWire] = wires[wire1] ^ wires[wire2]
				elif operator == "OR":
					wires[resultWire] = wires[wire1] | wires[wire2]
				else:
					wires[resultWire] = wires[wire1] & wires[wire2]
				gatesHandled.add(gate)
		gatesQueue -= gatesHandled

	zWires = list()
	for wire, bit in wires.items():
		if wire[0] == 'z':
			zWires.append((wire, bit))
	zWires.sort()
	zWires.reverse()
	number = list()
	for wire, bit in zWires:
		number.append(bit)
	print(*number, sep='')

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	if len(sys.argv) == 1:
		main("test_case")
	else:
		main(sys.argv[1])
