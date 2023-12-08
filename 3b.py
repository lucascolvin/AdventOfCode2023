import re

def checkNeighborLineForNumbers(line: str, gearIdx: int):
    gearNeighbors = []
    num = ""
    if (gearIdx - 1) >= 0 and line[gearIdx - 1].isnumeric():
        num = line[gearIdx - 1]
        nextIdx = gearIdx - 2
        while nextIdx >= 0 and line[nextIdx].isnumeric():
            num = line[nextIdx] + num
            nextIdx -= 1
    if num and not(line[gearIdx].isnumeric()):
        gearNeighbors.append(int(num))
        num = ""
    if line[gearIdx].isnumeric():
        num += line[gearIdx]
    if (gearIdx + 1) < len(line):
        if num and not(line[gearIdx + 1].isnumeric()):
            gearNeighbors.append(int(num))
            num = ""
        elif line[gearIdx + 1].isnumeric():
            num += line[gearIdx + 1]
            nextIdx = gearIdx + 2
            while nextIdx < len(line) and line[nextIdx].isnumeric():
                num += line[nextIdx]
                nextIdx += 1
            gearNeighbors.append(int(num))
    return gearNeighbors

def checkGearForNeighbors(previousLine: str, currentLine: str, nextLine: str, gearIdx: int):
    gearNeighbors = []
    if (gearIdx - 1) >= 0 and currentLine[gearIdx - 1].isnumeric():
        num = currentLine[gearIdx - 1]
        nextIdx = gearIdx - 2
        while nextIdx >= 0 and currentLine[nextIdx].isnumeric():
            num = currentLine[nextIdx] + num
            nextIdx -= 1
        gearNeighbors.append(int(num))
    if (gearIdx + 1) < len(currentLine) and currentLine[gearIdx + 1].isnumeric():
        num = currentLine[gearIdx + 1]
        nextIdx = gearIdx + 2
        while nextIdx < len(currentLine) and currentLine[nextIdx].isnumeric():
            num += currentLine[nextIdx]
            nextIdx += 1
        gearNeighbors.append(int(num))

    gearNeighbors.extend(checkNeighborLineForNumbers(previousLine, gearIdx))
    gearNeighbors.extend(checkNeighborLineForNumbers(nextLine, gearIdx))
    return gearNeighbors


def checkLine(previousLine: str, currentLine: str, nextLine: str):
    lineSum = 0
    pieces = re.split(r"\*", currentLine)
    gearIdx = 0
    for idx, piece in enumerate(pieces):
        if idx < len(pieces)-1:
            gearIdx += len(piece) + int(idx != 0)
            gearNeighbors = checkGearForNeighbors(previousLine, currentLine, nextLine, gearIdx)
            if len(gearNeighbors) == 2:
                lineSum += gearNeighbors[0] * gearNeighbors[1]
    return lineSum

input_file_path = '3-in.txt'

if __name__ == "__main__":
    gearSum = 0
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
                gearSum += checkLine('.' * lineLength, prevLine, currentLine)
            else:
                #all others except last
                gearSum += checkLine(prevLine, currentLine, line)
                prevLine = currentLine
                currentLine = line.strip()
        gearSum += checkLine(prevLine, currentLine, '.' * lineLength)

    print("Part two: ", gearSum)
