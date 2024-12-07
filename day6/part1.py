def inBounds(grid, pos):
    if pos[0] < 0 or pos[0] >= len(grid) or \
            pos[1] < 0 or pos[1] >= len(grid[0]):
        return False
    return True


def changedirection(dir):
    if dir == [-1, 0]:
        dir = [0, 1]
    elif dir == [0, 1]:
        dir = [1, 0]
    elif dir == [1, 0]:
        dir = [0, -1]
    elif dir == [0, -1]:
        dir = [-1, 0]
    return dir


# Checks if taking a step in current direction is possible
# if we go out of bounds returns 2
# if we encounter an obstacle returns 0
def canstep(grid, pos, dir):
    if inBounds(grid, [pos[0] + dir[0], pos[1] + dir[1]]) == False:
        return 2
    newPos = [pos[0], pos[1]]
    newPos[0] = newPos[0] + dir[0]
    newPos[1] = newPos[1] + dir[1]
    if grid[newPos[0]][newPos[1]] == '#':
        return 0
    return 1


# attempts to take a step
# if it is, changes the position of the guard and puts an x
# on the new position (used later to calculate the spaces the guard visited)
# if there is an obstacle turns the guard and tries to step again
# if the guard goes out of bounds sets the position to [-1,-1] so the simulation stops
def tryStep(grid, pos, dir):
    while True:
        if canstep(grid, pos, dir) == 1:
            pos[0] = pos[0] + dir[0]
            pos[1] = pos[1] + dir[1]
            grid[pos[0]][pos[1]] = 'x'
            break
        elif canstep(grid, pos, dir) == 2:
            return grid, [-1, -1], dir
        else:
            dir = changedirection(dir)
    return grid, pos, dir


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

    # simulates the guards steps, stops when they walk out of bounds
    # returns everything cause I forget how lists and references in python work
    while True:
        grid, pos, dir = tryStep(grid, pos, dir)
        if pos == [-1, -1]:
            break

    for line in grid:
        for char in line:
            if char == '^' or char == 'x':
                part1 += 1

    print(f"The answer to part 1 is: {part1}")


if __name__ == "__main__":
    main()
