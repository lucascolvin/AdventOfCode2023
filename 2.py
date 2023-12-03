
# Import necessary libraries (if any)
# For example: import math

# Define functions (if needed)
def getGameMaxValues(game: str):
    # Function logic goes here
    colors = {
        "red": 0,
        "blue": 0,
        "green": 0
    }

    gameSets = game.split(": ")[1].split("; ")

    for gameSet in gameSets:
        for colorData in gameSet.split(", "):
            splitColorData = colorData.split()
            colors[splitColorData[1]] = max(int(splitColorData[0]), colors[splitColorData[1]])

    return colors

input_file_path = '2-in.txt'

if __name__ == "__main__":
    games = []
    with open(input_file_path, 'r') as file:
        for line in file:
            games.append(getGameMaxValues(line))
    print(games)
    
    idxSum = 0
    powerSum = 0
    for idx, game in enumerate(games):
        # print(game["red"], game["green"], game["blue"])
        # print(game["red"] <= 12, game["green"] <= 13, game["blue"] <= 14)
        if game["red"] <= 12 and game["green"] <= 13 and game["blue"] <= 14:
            print(idx+1)
            idxSum += idx+1
        power = game["red"] * game["green"] * game["blue"]
        print("power: ", power)
        powerSum += power
    print(idxSum, powerSum)