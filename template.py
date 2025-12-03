def readInput():
    with open("2ndTask/test.txt") as file:
        instructions = []
        for line in file:
            instructions.append(line.strip())
    return instructions


def main():
    instructions = readInput()

    print("The final code is:")
    print(instructions)


if __name__ == "__main__":
    main()
