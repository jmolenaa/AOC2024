from collections import defaultdict
from part1 import inBounds, tryStep


def newGrid(grid):
    newgrid = list()
    for y, line in enumerate(grid):
        newgrid.append(list())
        for x, char in enumerate(line):
            newgrid[y].append(char)
    return newgrid


# Tries to put an obstacle in the new grid on position x and y
# Then simulates the guards walk from his start position
# keeps track of all the guards positions and corresponding direction during them
# if the guard reaches the same position with the same direction it means they're in an infinite
def tryObstacle(grid, pos, dir, y: int, x: int):
    newgrid = newGrid(grid)
    newgrid[y][x] = '#'
    newPos = [pos[0], pos[1]]
    newDir = [dir[0], dir[1]]

    # dict to keep track of visited spots and their direction
    placesVisited = defaultdict(tuple)
    placesVisited[tuple(newPos)] = tuple(newDir)
    while True:
        newgrid, newPos, newDir = tryStep(newgrid, newPos, newDir)
        if newPos == [-1, -1]:
            return False
        elif placesVisited[tuple(newPos)] == tuple(newDir):
            return True
        placesVisited[tuple(newPos)] = tuple(newDir)


def main():
    with open("input") as file:
        lines = file.read().split("\n")

    part1 = 0
    part2 = 0

    # Creates new grid with a list of list of chars so we can actually
    # change the characters in the grid, python is naughty with the immutable strings
    grid = list()
    for y, line in enumerate(lines):
        grid.append(list())
        for x, char in enumerate(line):
            grid[y].append(char)
            if char == '^':
                pos = [y, x]
    dir = [-1, 0]
    startpos = [pos[0], pos[1]] # save starting position

    # loops through whole grid, puts an obstacle in every open spot
    # then simulates walk to see if an infinite is reached, if yes adds to the result
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if [y, x] == startpos or grid[y][x] == '#':
                continue
            infiniteloop = tryObstacle(grid, pos, dir, y, x)
            if infiniteloop is True:
                part2 += 1

    print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
    main()
