def readInput():
    with open("5thTask/Input1.txt") as file:
        instructions = []
        ingredient = False
        for line in file:
            if line == '\n':
                ingredient = True
                instructions.append("Ingredients:")
                continue
            if ingredient:
                instructions.append(line.strip())
            else:
                instructions.append(line.strip())
    return instructions


def calculateFreshIngredientIds(instructions):
    freshIngredientIds = []
    for entry in instructions:
        if entry.startswith("Ingredients:"):
            break
        startId, endId = map(int, entry.split('-'))
        freshIngredientIds.append((startId, endId))
    return freshIngredientIds


def countFreshIngredients(freshIngredientIds, instructions):
    beginIndex = instructions.index("Ingredients:")
    ingredients = [int(line) for index, line in enumerate(instructions) if index > beginIndex]
    freshCount = 0
    for ingredient in ingredients:
        for tuple in freshIngredientIds:
            if tuple[0] <= ingredient <= tuple[1]:
                freshCount += 1
                break
    return freshCount


def createCleanIdsSet(freshIngredientIds):
    iDsSet = set()
    for tuple1 in freshIngredientIds:
        for tuple in freshIngredientIds:
            if tuple != tuple1:
                if tuple[0] <= tuple1[0] <= tuple[1]:
                    x = tuple[0]
                else:
                    x = tuple1[0]
                if tuple[0] <= tuple1[1] <= tuple[1]:
                    y = tuple[1]
                else:
                    y = tuple1[1]
                iDsSet.add((x, y))
    for tuple1 in freshIngredientIds:
        for tuple in freshIngredientIds:
            if tuple != tuple1:
                if tuple[0] <= tuple1[0] <= tuple[1] and tuple[0] <= tuple1[1] <= tuple[1]:
                    iDsSet.discard(tuple1)
    return iDsSet


def countFreshIngredientIds(freshIngredientIds):
    iDsCount = 0
    iDsSet = createCleanIdsSet(freshIngredientIds)
    while iDsSet != createCleanIdsSet(iDsSet):
        iDsSet = createCleanIdsSet(iDsSet)
    for tuple in iDsSet:
        iDsCount += tuple[1] - tuple[0] + 1
    return iDsCount


def main():
    instructions = readInput()
    freshIngredientIds = calculateFreshIngredientIds(instructions)
    code = countFreshIngredientIds(freshIngredientIds)
    print("The final code is:")
    print(code)


if __name__ == "__main__":
    main()
