def readInput():
    with open("2ndTask/Input1.txt") as file:
        instructions = []
        for line in file:
            list = line.strip().split(",")
            for listEntry in list:
                instructions.append(listEntry)
    return instructions


def divideNumberandCheckSymmetry(number):
    strNumber = str(number)
    amountOfDigits = len(strNumber)
    if amountOfDigits % 2 == 0:
        firstHalf = strNumber[:amountOfDigits // 2]
        secondHalf = strNumber[amountOfDigits // 2:]
        if firstHalf == secondHalf:
            return True
    if amountOfDigits % 3 == 0:
        firstThird = strNumber[:amountOfDigits // 3]
        secondThird = strNumber[amountOfDigits // 3: 2 * (amountOfDigits // 3)]
        lastThird = strNumber[2 * (amountOfDigits // 3):]
        if firstThird == secondThird == lastThird:
            return True
    if amountOfDigits % 4 == 0:
        firstQuarter = strNumber[:amountOfDigits // 4]
        secondQuarter = strNumber[amountOfDigits // 4: amountOfDigits // 2]
        thirdQuarter = strNumber[amountOfDigits // 2: 3 * (amountOfDigits // 4)]
        lastQuarter = strNumber[3 * (amountOfDigits // 4):]
        if firstQuarter == secondQuarter == thirdQuarter == lastQuarter:
            return True
    if amountOfDigits % 5 == 0:
        firstFifth = strNumber[:amountOfDigits // 5]
        secondFifth = strNumber[amountOfDigits // 5: 2 * (amountOfDigits // 5)]
        thirdFifth = strNumber[2 * (amountOfDigits // 5): 3 * (amountOfDigits // 5)]
        fourthFifth = strNumber[3 * (amountOfDigits // 5): 4 * (amountOfDigits // 5)]
        lastFifth = strNumber[4 * (amountOfDigits // 5):]
        if firstFifth == secondFifth == thirdFifth == fourthFifth == lastFifth:
            return True
    if amountOfDigits % 6 == 0:
        firstSixth = strNumber[:amountOfDigits // 6]
        secondSixth = strNumber[amountOfDigits // 6: 2 * (amountOfDigits // 6)]
        thirdSixth = strNumber[2 * (amountOfDigits // 6): 3 * (amountOfDigits // 6)]
        fourthSixth = strNumber[3 * (amountOfDigits // 6): 4 * (amountOfDigits // 6)]
        fifthSixth = strNumber[4 * (amountOfDigits // 6): 5 * (amountOfDigits // 6)]
        lastSixth = strNumber[5 * (amountOfDigits // 6):]
        if firstSixth == secondSixth == thirdSixth == fourthSixth == fifthSixth == lastSixth:
            return True
    if amountOfDigits % 7 == 0:
        firstSeventh = strNumber[:amountOfDigits // 7]
        secondSeventh = strNumber[amountOfDigits // 7: 2 * (amountOfDigits // 7)]
        thirdSeventh = strNumber[2 * (amountOfDigits // 7): 3 * (amountOfDigits // 7)]
        fourthSeventh = strNumber[3 * (amountOfDigits // 7): 4 * (amountOfDigits // 7)]
        fifthSeventh = strNumber[4 * (amountOfDigits // 7): 5 * (amountOfDigits // 7)]
        sixthSeventh = strNumber[5 * (amountOfDigits // 7): 6 * (amountOfDigits // 7)]
        lastSeventh = strNumber[6 * (amountOfDigits // 7):]
        if firstSeventh == secondSeventh == thirdSeventh == fourthSeventh == fifthSeventh == sixthSeventh == lastSeventh:
            return True
    return False


def calculateDoubles(instructions):
    code = 0
    for instruction in instructions:
        start = int(instruction.split("-")[0])
        end = int(instruction.split("-")[1]) + 1
        listOfNumbers = list(range(start, end))
        for number in listOfNumbers:
            solution = divideNumberandCheckSymmetry(number)
            if solution:
                code += number
                # print(instruction)
                # print(number)
                # print(solution)
    return code


def main():
    instructions = readInput()
    code = calculateDoubles(instructions)
    print("The final code is:")
    print(code)


if __name__ == "__main__":
    main()
