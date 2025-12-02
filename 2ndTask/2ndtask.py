def readInput():
    with open("test.txt") as file:
        instructions = []
        for line in file:
            instructions.append(line.strip())
    return instructions


def main():
    instructions = readInput()
    code = instructions[0]
    print("The final code is:")
    print(code)


if __name__ == "__main__":
    main()
