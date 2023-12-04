

# 1.1
ex = [
    '1abc2',
    'pqr3stu8vwx',
    'a1b2c3d4e5f',
    'treb7uchet'
]

with open('2023/data/input_01.txt', 'r') as file:
    input_01 = file.read().splitlines()

def solve_1_1(str_list:list) -> int:
    # extract numbers from list
    nums = [[item for item in string if item.isnumeric()] for string in str_list]
    nums = [int(item[0] + item[-1]) for item in nums]
    return sum(nums)

# 1.2
ex2 = [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen'
]

num_map = {
    "one":    1,
    "two":    2,
    "three":  3,
    "four":   4,
    "five":   5,
    "six":    6,
    "seven":  7,
    "eight":  8,
    "nine":   9
}

def solve_1_2(str_list:list):

    nums_list = []
    for string in str_list:
        nums = []
        for i in range(len(string)):
            if string[i].isnumeric():
                nums.append(str(string[i]))
            else:
                for j in range(len(string)):
                    lookup = num_map.get(string[i:j+1])
                    if lookup:
                        nums.append(lookup)
                        break
        
        nums_list.append(int(str(nums[0]) + str(nums[-1])))

    return sum(nums_list)

if __name__ == "__main__":
    print(solve_1_1(input_01))

    print(solve_1_2(input_01))