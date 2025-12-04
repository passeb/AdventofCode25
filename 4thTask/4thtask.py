import copy


def readInput():
    with open("4thTask/Input1.txt") as file:
        instructions = []
        for line in file:
            list = [literal for literal in line if literal != '\n']
            instructions.append(list)
    return instructions


def calculateAccessablePaperRolls(instructions):
    numberOfColumns = len(instructions[0])
    numberofRows = len(instructions)
    instructionsCopy = copy.deepcopy(instructions)
    print(f"Rows: {numberOfColumns}, Lines: {numberofRows}")
    for row in range(numberofRows):
        for column in range(numberOfColumns):
            if instructions[row][column] == '@':
                if row == 0:
                    counter = 0
                    if column == 0:
                        # print("Start at top-left corner")
                        if instructions[row+1][column] == '@': counter += 1
                        if instructions[row][column+1] == '@': counter += 1
                        if instructions[row+1][column+1] == '@': counter += 1
                        print(f"Accessible rolls from (0,0): {counter}")
                    elif column == numberOfColumns - 1:
                        if instructions[row][column-1] == '@': counter += 1
                        if instructions[row+1][column-1] == '@': counter += 1
                        if instructions[row+1][column] == '@': counter += 1
                        print(f"Accessible rolls from (0,{column}): {counter}")
                    else:
                        if instructions[row][column-1] == '@': counter += 1
                        if instructions[row+1][column-1] == '@': counter += 1
                        if instructions[row+1][column] == '@': counter += 1
                        if instructions[row][column+1] == '@': counter += 1
                        if instructions[row+1][column+1] == '@': counter += 1
                        print(f"Accessible rolls from (0,{column}): {counter}")
                    if counter < 4: instructionsCopy[row][column] = 'x'
                elif row == numberofRows - 1:
                    counter = 0
                    if column == 0:
                        if instructions[row-1][column] == '@': counter += 1
                        if instructions[row-1][column+1] == '@': counter += 1
                        if instructions[row][column+1] == '@': counter += 1
                        # print(f"Accessible rolls from ({row},0): {counter}")
                    elif column == numberOfColumns - 1:
                        if instructions[row-1][column-1] == '@': counter += 1
                        if instructions[row-1][column] == '@': counter += 1
                        if instructions[row][column-1] == '@': counter += 1
                        # print(f"Accessible rolls from ({row},{column}): {counter}")
                    else:
                        if instructions[row][column-1] == '@': counter += 1
                        if instructions[row-1][column-1] == '@': counter += 1
                        if instructions[row-1][column] == '@': counter += 1
                        if instructions[row-1][column+1] == '@': counter += 1
                        if instructions[row][column+1] == '@': counter += 1
                        # print(f"Accessible rolls from ({row},{column}): {counter}")
                    if counter < 4: instructionsCopy[row][column] = 'x'
                else:
                    counter = 0
                    if column == 0:
                        if instructions[row-1][column] == '@': counter += 1
                        if instructions[row-1][column+1] == '@': counter += 1
                        if instructions[row][column+1] == '@': counter += 1
                        if instructions[row+1][column] == '@': counter += 1
                        if instructions[row+1][column+1] == '@': counter += 1
                        # print(f"Accessible rolls from ({row},0): {counter}")
                    elif column == numberOfColumns - 1:
                        if instructions[row-1][column-1] == '@': counter += 1
                        if instructions[row-1][column] == '@': counter += 1
                        if instructions[row][column-1] == '@': counter += 1
                        if instructions[row+1][column-1] == '@': counter += 1
                        if instructions[row+1][column] == '@': counter += 1
                        # print(f"Accessible rolls from ({row},{column}): {counter}")
                    else:
                        if instructions[row-1][column-1] == '@': counter += 1
                        if instructions[row-1][column] == '@': counter += 1
                        if instructions[row-1][column+1] == '@': counter += 1
                        if instructions[row][column-1] == '@': counter += 1
                        if instructions[row][column+1] == '@': counter += 1
                        if instructions[row+1][column-1] == '@': counter += 1
                        if instructions[row+1][column] == '@': counter += 1
                        if instructions[row+1][column+1] == '@': counter += 1
                        # print(f"Accessible rolls from ({row},{column}): {counter}")
                    if counter < 4: instructionsCopy[row][column] = 'x'
        # print()
    # print(instructions)
    return instructionsCopy


def countRemainingPaperRolls(instructions):
    counter = 0
    for row in instructions:
        for literal in row:
            if literal == 'x':
                counter += 1
    return counter


def removeAsMuchAsPossiblePaperRolls(instructions):
    previousInstructions = []
    currentInstructions = instructions
    while previousInstructions != currentInstructions:
        previousInstructions = currentInstructions
        currentInstructions = calculateAccessablePaperRolls(currentInstructions)
    counter = countRemainingPaperRolls(currentInstructions)
    return counter


def main():
    instructions = readInput()
    code = removeAsMuchAsPossiblePaperRolls(instructions)
    print("The final code is:")
    print(code)


if __name__ == "__main__":
    main()
