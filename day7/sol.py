def add(number1: int, number2: int) -> int:
    return number1 + number2


def multiply(number1: int, number2: int) -> int:
    return number1 * number2


def concatenate(number1: int, number2: int) -> int:
    return int(str(number1) + str(number2))


# Tries all three operators (2 for part1), and keeps going until
# the last number is reached, if the result matches the final number
# will return the finalResult and build back the recursion to main
# if it doesn't match, will return -1 and go back a step to try a different operation
# if no operation left goes back again and try another path
# if nothing works returns to main and doesn't count the line
def tryoperator(currentResult: int, numbers: list[int], index: int, finalResult: int, part: int) -> int:
    if index == len(numbers):
        if currentResult == finalResult:
            return currentResult
        return -1
    if tryoperator(add(currentResult, numbers[index]), numbers, index + 1, finalResult, part) == finalResult:
        return finalResult
    if tryoperator(multiply(currentResult, numbers[index]), numbers, index + 1, finalResult, part) == finalResult:
        return finalResult
    if part == 2 and tryoperator(concatenate(currentResult, numbers[index]), numbers, index + 1, finalResult, part) == finalResult:
        return finalResult
    return -1


def main():
    with open("input") as file:
        lines = file.read().split("\n")

    part1 = 0
    part2 = 0
    for line in lines:
        result, numbers = line.split(":")
        numbers = list(map(int, numbers.split()))
        if tryoperator(numbers[0], numbers, 1, int(result), 1) != -1:
            part1 += int(result)
        if tryoperator(numbers[0], numbers, 1, int(result), 2) != -1:
            part2 += int(result)

    print(f"The answer to part 1 is: {part1}")
    print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
    main()
