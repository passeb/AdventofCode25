def readInput():
    with open("Input1.txt") as file:
        instructions = []
        for line in file:
            instructions.append(line.strip())
    return instructions


def decipherInstruction(instructions):
    summands = []
    for i in range(len(instructions)):
        string = instructions[i]
        if list(string)[0] == "L":
            summand = int(string[1:])*(-1)
        else:
            summand = int(string[1:])
        summands.append(summand)
    return summands


def calculateFinalPositionandCode(summands):
    position = oldposition = 50
    code = 0

    for summand in summands:
        sum = position + summand
        divisionTuple = divmod(sum, 100)  # Get quotient and remainder
        quotient = divisionTuple[0]  # quotient indicates number of cycles
        position = divisionTuple[1]  # remainder is the new position
        if (summand < 0 and oldposition == 0):
            if (position == 0):
                code += abs(quotient)
            else:
                code += abs(quotient+1)
        elif (summand < 0 and oldposition != 0):
            if (position == 0 and sum != 0):
                code += abs(quotient)+1
            elif (position != 0):
                code += abs(quotient)
        else:
            code += abs(quotient)
        if (sum == 0):
            code += 1
        oldposition = position

    return code


def main():
    instructions = readInput()
    summands = decipherInstruction(instructions)
    code = calculateFinalPositionandCode(summands)
    print("The final code is:")
    print(code)


if __name__ == "__main__":
    main()
