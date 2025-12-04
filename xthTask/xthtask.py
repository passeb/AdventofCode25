def readInput():
    with open("xthTask/test.txt") as file:
        instructions = []
        for line in file:
            instructions.append(line.strip())
    return instructions


def calculatesth(instructions):
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
    return instructions


def main():
    instructions = readInput()
    code = calculatesth(instructions)
    print("The final code is:")
    print(code)


if __name__ == "__main__":
    main()
