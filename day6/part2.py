from collections import defaultdict

def tryStep(grid, pos, dir):
    if pos[0] + dir[0] < 0 or pos[0] + dir[0] >= len(grid) or \
            pos[1] + dir[1] < 0 or pos[1] + dir[1] >= len(grid[0]):
        return 2
    newPos = [pos[0], pos[1]]
    dy, dx = dir
    newPos[0] = newPos[0] + dy
    newPos[1] = newPos[1] + dx
    # print(len(grid), len(grid[0]), newPos[0], newPos[1])
    if grid[newPos[0]][newPos[1]] == '#':
        return 0
    return 1


def tryWalk(grid, pos, dir, startPos, turns):
    while True:
        if tryStep(grid, pos, dir) == 1:
            pos[0] = pos[0] + dir[0]
            pos[1] = pos[1] + dir[1]
            break
        elif tryStep(grid, pos, dir) == 2:
            return grid, [-1, -1], dir, turns
        else:
            if dir == [-1, 0]:
                dir = [0, 1]
            elif dir == [0, 1]:
                dir = [1, 0]
            elif dir == [1, 0]:
                dir = [0, -1]
            elif dir == [0, -1]:
                dir = [-1, 0]
            turns += 1

    return grid, pos, dir, turns


def newGrid(grid):
    newgrid = list()
    for y, line in enumerate(grid):
        newgrid.append(list())
        for x, char in enumerate(line):
            newgrid[y].append(char)
    return newgrid

def inBounds(grid, pos, dir):
    if pos[0] < 0 or pos[0] >= len(grid) or \
            pos[1] < 0 or pos[1] >= len(grid[0]):
        return False
    return True


def canPutObstacle(grid, pos, dir, startpos):
    obstaclePos = [pos[0] + dir[0], pos[1] + dir[1]]
    if not inBounds(grid, obstaclePos, dir) or obstaclePos == startpos:
        # print("0", inBounds(grid, obstaclePos, dir))
        return 0
    elif grid[obstaclePos[0]][obstaclePos[1]] == '#':
        return 2
    return 1


# def tryObstacle(grid, pos, dir, startpos):
#     newgrid = newGrid(grid)
#     newPos = [pos[0], pos[1]]
#     newDir = [dir[0], dir[1]]
#     if canPutObstacle(newgrid, pos, dir, startpos) == 0:
#         return False
#     elif canPutObstacle(newgrid, pos, dir, startpos) == 2:
#         if newDir == [-1, 0]:
#             newDir = [0, 1]
#         elif newDir == [0, 1]:
#             newDir = [1, 0]
#         elif newDir == [1, 0]:
#             newDir = [0, -1]
#         elif newDir == [0, -1]:
#             newDir = [-1, 0]
#         return tryObstacle(newgrid, newPos, newDir, startpos)
#
#     obstaclePos = [pos[0] + dir[0], pos[1] + dir[1]]
#     # print(pos, dir, obstaclePos)
#     newgrid[obstaclePos[0]][obstaclePos[1]] = '#'
#     # for line in newgrid:
#     #     print (line)
#     loopStart = [pos[0], pos[1]]
#     startDir = [dir[0], dir[1]]
#     turns = 0
#     newPos = [pos[0], pos[1]]
#     newDir = [dir[0], dir[1]]
#     # print("newhuh")
#
#     printing = False
#     placesVisited = defaultdict(tuple)
#     placesVisited[tuple(newPos)] = tuple(newDir)
#     if newPos == startpos:
#         printing = True
#     while True:
#         # print(newPos, newDir)
#         newgrid, newPos, newDir, turns = tryWalk(newgrid, newPos, newDir, startpos, turns)
#         # if printing == True:
#         #     print(newPos, newDir, turns)
#         if newPos == [-1, -1]:
#             # if printing == True:
#             #     print("False")
#             return False
#         elif placesVisited[tuple(newPos)] == tuple(newDir):
#             return True
#         # elif newPos == loopStart and newDir == startDir:
#         #     # if printing == True:
#         #     #     print("True")
#         #     # print(obstaclePos)
#         #     return True
#         elif turns > 500000:
#             # if printing == True:
#             #     print("turns")
#             return False
#         placesVisited[tuple(newPos)] = tuple(newDir)

def tryObstacle(grid, pos, dir, startpos, y, x):
    # print("here", len(grid), len(grid[0]))

    newgrid = newGrid(grid)
    # print("here", len(newgrid), len(newgrid[0]))

    newPos = [pos[0], pos[1]]
    newDir = [dir[0], dir[1]]

    if newgrid[y][x] == '#' or startpos == [y, x]:
        return False
    newgrid[y][x] = '#'
    # if canPutObstacle(newgrid, pos, dir, startpos) == 0:
    #     return False
    # elif canPutObstacle(newgrid, pos, dir, startpos) == 2:
    #     if newDir == [-1, 0]:
    #         newDir = [0, 1]
    #     elif newDir == [0, 1]:
    #         newDir = [1, 0]
    #     elif newDir == [1, 0]:
    #         newDir = [0, -1]
    #     elif newDir == [0, -1]:
    #         newDir = [-1, 0]
        # return tryObstacle(newgrid, newPos, newDir, startpos)

    # obstaclePos = [pos[0] + dir[0], pos[1] + dir[1]]
    # print(pos, dir, obstaclePos)
    # newgrid[obstaclePos[0]][obstaclePos[1]] = '#'
    # for line in newgrid:
    #     print (line)
    loopStart = [pos[0], pos[1]]
    startDir = [dir[0], dir[1]]
    turns = 0
    newPos = [pos[0], pos[1]]
    newDir = [dir[0], dir[1]]
    # print("newhuh")

    printing = False
    placesVisited = defaultdict(tuple)
    placesVisited[tuple(newPos)] = tuple(newDir)
    # if newPos == startpos:
    #     printing = True
    while True:
        # print(newPos, newDir)
        newgrid, newPos, newDir, turns = tryWalk(newgrid, newPos, newDir, startpos, turns)
        # if printing == True:
        #     print(newPos, newDir, turns)
        if newPos == [-1, -1]:
            # if printing == True:
            #     print("False")
            return False
        elif placesVisited[tuple(newPos)] == tuple(newDir):
            return True
        # elif newPos == loopStart and newDir == startDir:
        #     # if printing == True:
        #     #     print("True")
        #     # print(obstaclePos)
        #     return True
        elif turns > 500000:
            # if printing == True:
            #     print("turns")
            return False
        placesVisited[tuple(newPos)] = tuple(newDir)

# 1853

def main():
    with open("input") as file:
        lines = file.read().split("\n")

    part1 = 0
    part2 = 0

    grid = list()
    for y, line in enumerate(lines):
        grid.append(list())
        for x, char in enumerate(line):
            grid[y].append(char)
            if char == '^':
                pos = [y, x]
    dir = [-1, 0]
    startpos = [pos[0], pos[1]]
    turns = 0
    # print("here", len(grid), len(grid[0]))

    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            obstacle = tryObstacle(grid, pos, dir, startpos, y, x)
            if obstacle is True:
                print("YESSSSSS", part2)
                part2 += 1
            # print(x, y, part2)

    # while True:
    #     obstacle = tryObstacle(grid, pos, dir, startpos)
    #     if obstacle is True:
    #
    #         print("YESSSSSS", pos)
    #         part2 += 1
    #     grid, pos, dir, turns = tryWalk(grid, pos, dir, startpos, turns)
    #     if pos == [-1, -1]:
    #         break

    print(f"The answer to part 1 is: {part1}")
    print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
    main()
