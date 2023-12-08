import re

def containsSymbol(s: str):
    pattern = r"[^a-zA-Z0-9.]"
    return bool(re.search(pattern, s))

def checkForSymbolNeighbors(previousLine: str, currentLine: str, nextLine: str, startingIdx: int, endingIdx: int):
    if (startingIdx - 1) >= 0 and containsSymbol(currentLine[startingIdx - 1]):
        return True
    if (endingIdx + 1) < len(currentLine) and containsSymbol(currentLine[endingIdx + 1]):
        return True
    if containsSymbol(previousLine[max(0, startingIdx - 1): min(len(currentLine), endingIdx + 2)]):
        return True
    if containsSymbol(nextLine[max(0, startingIdx - 1): min(len(currentLine), endingIdx + 2)]):
        return True
    return False

def checkLine(previousLine: str, currentLine: str, nextLine: str):
    lineSum = 0
    currentNumber = ""
    startingIdx = -1
    # endingIdx = -1
    for idx, character in enumerate(currentLine):
        if character.isnumeric():
            currentNumber += character
            if(startingIdx == -1):
                startingIdx = idx
        elif currentNumber != "":
            # a numb just ended, check it
            if checkForSymbolNeighbors(previousLine, currentLine, nextLine, startingIdx, idx-1):
                print(currentNumber)
                lineSum += int(currentNumber)
            currentNumber = ""
            startingIdx = -1

    if currentNumber != "":
        # a nubmer just ended, check it
        if checkForSymbolNeighbors(previousLine, currentLine, nextLine, startingIdx, idx-1):
            lineSum += int(currentNumber)
        currentNumber = ""
        startingIdx = -1
    return lineSum

input_file_path = '3-in.txt'

if __name__ == "__main__":
    validNumbersSum = 0
    with open(input_file_path, 'r') as file:
        prevLine = ""
        currentLine = ""
        nextLine = ""
        lineLength = 0
        for line in file:
            if prevLine=="":
                #very first line
                prevLine = line.strip()
                lineLength = len(prevLine)
            elif currentLine=="":
                # second line
                currentLine = line.strip()
                # now we have info to do the fist line
                validNumbersSum += checkLine('.' * lineLength, prevLine, currentLine)
            else:
                #all others except last
                validNumbersSum += checkLine(prevLine, currentLine, line)
                prevLine = currentLine
                currentLine = line.strip()
        validNumbersSum += checkLine(prevLine, currentLine, '.' * lineLength)

    print("Part one: ", validNumbersSum)
