import re

def findAndLastDigits(str):
    first = re.search(r"\d|one|two|three|four|five|six|seven|eight|nine", str).group()
    match first:
        case "one":
            first = "1"
        case "two":
            first = "2"
        case "three":
            first = "3"
        case "four":
            first = "4"
        case "five":
            first = "5"
        case "six":
            first = "6"
        case "seven":
            first = "7"
        case "eight":
            first = "8"
        case "nine":
            first = "9"

    last = re.search(r"\d|enin|thgie|neves|xis|evif|ruof|eerht|owt|eno", str[::-1]).group()
    match last:
        case "eno":
            last = "1"
        case "owt":
            last = "2"
        case "eerht":
            last = "3"
        case "ruof":
            last = "4"
        case "evif":
            last = "5"
        case "xis":
            last = "6"
        case "neves":
            last = "7"
        case "thgie":
            last = "8"
        case "enin":
            last = "9"
    return first+last

input_file_path = '1-in.txt'  # Replace with your file path

if __name__ == "__main__":
    # Print something to the console
    sum = 0
    with open(input_file_path, 'r') as file:
        for line in file:
            sum += int(findAndLastDigits(line))
            # Do something with the result
            print(sum)
            # print(findAndLastDigits(line))

    print(sum)
