def readInput():
    with open("Input1.txt") as file:
        instructions = []
        for line in file:
            instructions.append(line.strip())
    return instructions

def main():
    instructions = readInput()
    
    print("The final code is:")
    print(code)


if __name__ == "__main__":
    main()
