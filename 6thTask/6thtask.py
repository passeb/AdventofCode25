import numpy as np
import re
from collections import defaultdict


def readInput():
    with open("6thTask/Input1.txt") as file:
        numbers = []
        regex = []
        for line in file:
            numbers.append(line)
        regex = numbers.pop()
        muster = r"([\S])(\s*)"
        regex = re.findall(muster, regex)
        operators = []
        for tupel in regex:
            tupel = list(tupel)
            operators.append((tupel[0], len(tupel[1])))
            # print(operators)
    return numbers, operators


def calculateSquidNumbers(numbers, operators):
    stringIndex = 0
    squidnumbers = defaultdict(int)
    squidmultiplyers = defaultdict(lambda: 1)
    numbers.reverse()
    for line in numbers:
        # print(line)
        for _, length in operators:
            for position in reversed(range(length+1)):
                if line[stringIndex + position] == " ":
                    asInt = 0
                elif line[stringIndex + position].isnumeric():
                    asInt = int(line[stringIndex + position])
                else:
                    asInt = 0
                squidnumbers[stringIndex+position] += (asInt * squidmultiplyers[stringIndex+position])
                if asInt != 0:
                    squidmultiplyers[stringIndex+position] *= 10
                # print(line[stringIndex + position])
                # print(squidnumbers[stringIndex+position])
            stringIndex += length + 1
        stringIndex = 0
    return squidnumbers


def addAndMultiply(squidnumbers, operators):
    numbers = []
    listIndex = 0
    print(squidnumbers)
    print(operators)
    for operator, factors in operators:
        if operator == "+":
            operationResult = 0
            for i in range(factors):
                operationResult += squidnumbers[listIndex + i]
        elif operator == "*":
            operationResult = 1
            for i in range(factors):
                operationResult *= squidnumbers[listIndex + i]
        listIndex += factors + 1
        numbers.append(operationResult)
        print(operationResult)
    return sum(numbers)


def calculatesth(numbers, operators):
    array = np.array(numbers, dtype=np.int64).transpose()
    result = []
    for i in range(len(array)):
        if operators[i] == "+":
            lineresult = np.sum(array[i])
        elif operators[i] == "*":
            lineresult = np.prod(array[i])
        result.append(lineresult)
    return sum(result)


def main():
    numbers, operators = readInput()
    squidnuumbers = calculateSquidNumbers(numbers, operators)
    code = addAndMultiply(squidnuumbers, operators)
    print("The final code is:")
    print(code)


if __name__ == "__main__":
    main()
