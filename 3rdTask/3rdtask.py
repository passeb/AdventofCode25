def readInput():
    with open("3rdTask/Input1.txt") as file:
        instructions = []
        for line in file:
            list = [int(digit) for digit in line if digit != '\n']
            instructions.append(list)
    return instructions


def calculateMaxJoltage(instructions):
    maxJoltages = []
    for list in instructions:
        maxJoltage = 0
        newlist = list[:]
        newlist.pop()
        indexMaxWithoutLastDigit = newlist.index(max(newlist))
        MaxWithoutLastOne = newlist[indexMaxWithoutLastDigit]
        indexMaxWithoutLastDigit += 1
        newlist = list[indexMaxWithoutLastDigit:]
        MaxOfRemainingList = max(newlist)
        maxJoltage = (MaxWithoutLastOne * 10) + MaxOfRemainingList
        maxJoltages.append(maxJoltage)
    return sum(maxJoltages)


def main():
    instructions = readInput()
    code = calculateMaxJoltage(instructions)
    print("The final code is:")
    print(code)


if __name__ == "__main__":
    main()
