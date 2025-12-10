def readInput():
    with open("7thTask/test.txt") as file:
        instructions = []
        for line in file:
            instructions.append(line.strip())
    return instructions


def calculatesth(instructions):
    
    return instructions


def main():
    instructions = readInput()
    code = calculatesth(instructions)
    print("The final code is:")
    print(code)


if __name__ == "__main__":
    main()
