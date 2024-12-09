from collections import defaultdict


def calculatepart1(ids):
	part1 = 0
	gapindex = ids.index('.') # keeps track of where our gap is
	idindex = len(ids) - 1 # index for ids, moves from the back to the front
	# loops from the back until we have a contiguous row of ids
	# happens when we reach the gapindex
	# whenever we encounter an id (something different from ".")
	# we move the id to the first possible gap
	# then we move the gap pointer to the next possible gap

	# we also set the id moved to a hashtag
	# the way I count the solution could cause an edge case
	# where the last moved id couldn't be moved fully so no change would cause it
	# to be counted twice
	# TL:DR to avoid thinking about edge cases I just erase the moved IDs
	while idindex > gapindex:
		if ids[idindex] != ".":
			ids[gapindex] = ids[idindex]
			ids[idindex] = "#"
			while ids[gapindex] != ".":
				gapindex += 1
		idindex -= 1

	# adds up the solution, stops at the first # or .
	for i, char in enumerate(ids):
		if char == "#" or char == ".":
			break
		part1 += i * int(char)
	return part1


def calculatepart2(ids, gaps, idoccurence):
	part2 = 0
	idindex = len(ids) - 1
	# moves from the back to the front, stops in theory at the start
	# in theory the last blocks aren't moved at all cause the gaps would have been filled
	while idindex > 0:
		# skip gaps
		if ids[idindex] == '.':
			idindex -= 1
			continue

		# calculate how big the file is
		size = blocksize(ids, idindex)
		# loops over the gaps from start to end to find a gap big enough
		for gap in gaps:
			gapsize, gapspot = gap
			# if the gap is behind the index of the file, we don't move the file
			# this also ensure we don't move files twice, cause we would have moved it
			# as far as possible the first time
			if gapspot >= idindex:
				break
			# if we can fit the file we adjust the gapsize by the filesize
			# we also move the gap index
			if size <= gapsize:
				gap[0] = gap[0] - size
				gap[1] = gap[1] + size
				# moves file
				for j in range(size):
					ids[gapspot + j] = ids[idindex]
				# file moved so we break from the gap loop and move onto the next one
				break
		# move index by the whole file
		idindex -= size
	# calculates the answer, since I moved the files without changing their original position
	# it causes weird stuff, cause some files appear twice
	# since the file we need to count is always first I keep track
	# of what ids I've counted with the dictionary
	# whenever I count an id I detract it from the dictionary
	# if the id in the dictionary is 0 we don't count it, cause it's the original file position
	for i, char in enumerate(ids):
		if char == ".":
			continue
		if idoccurence[char] > 0:
			part2 += i * int(char)
			idoccurence[char] = idoccurence[char] - 1
	return part2


def blocksize(ids, idindex) -> int:
	size = 0
	id = ids[idindex]
	while ids[idindex] == id:
		size += 1
		idindex -= 1
	return size

def main():
	with open("input") as file:
		line = file.read()

	ids = list() # a list of all the ids in order with '.' where gaps are
	gaps = list() # a list of keeping track of how big gaps are and where their starting index is
	actualIndex = 0 # index of the ids list, used for gaps indexing
	idoccurence = defaultdict(int) # dictionary of how many times each id occurs
	for i, char in enumerate(line):
		if i % 2 == 1:
			gaps.append([int(char), int(actualIndex)])
		if i % 2 ==0:
			idoccurence[int(i / 2)] = int(char)
		for j in range(int(char)):
			if i % 2 == 0:
				ids.append(int(i / 2))
			else:
				ids.append('.')
		actualIndex += int(char)

	idspart1 = ids.copy()
	idspart2 = ids.copy()
	part1 = calculatepart1(idspart1)
	part2 = calculatepart2(idspart2, gaps, idoccurence)

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")

if __name__ == "__main__":
	main()