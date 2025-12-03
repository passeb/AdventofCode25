def readInput():
    with open("3rdTask/Input1.txt") as file:
        instructions = []
        for line in file:
            list = [int(digit) for digit in line if digit != '\n']
            instructions.append(list)
    return instructions


def calculateMaxJoltage2Digits(instructions):
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


def calculateMaxJoltage12Digits(instructions):
    maxJoltages = []
    for list in instructions:
        maxJoltage = 0
        maxDigits = []
        remainingList = list[:]
        for i in range(11, -1, -1):
            newlist = remainingList[:]
            print(newlist)
            for j in range(i):
                newlist.pop()
            print(newlist)
            indexMaxWithoutLastDigits = newlist.index(max(newlist))
            maxDigits.append(newlist[indexMaxWithoutLastDigits])
            indexMaxWithoutLastDigits += 1
            remainingList = remainingList[indexMaxWithoutLastDigits:]
            print(remainingList)
        strMaxJoltage = ''.join([str(digit) for digit in maxDigits])
        maxJoltage = int(strMaxJoltage)
        maxJoltages.append(maxJoltage)
        print(maxJoltage)
    return sum(maxJoltages)


def main():
    instructions = readInput()
    code = calculateMaxJoltage12Digits(instructions)
    print("The final code is:")
    print(code)


if __name__ == "__main__":
    main()
