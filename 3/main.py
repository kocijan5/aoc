import re

def main(file_path):
    with open(file_path) as file:
        lines = file.readlines()

    text = "".join(lines)
    
    expresion = re.compile(r'mul\(\d*,\d*\)')
    occurerces = re.findall(expresion, text)

    sum = 0
    for occurence in occurerces:
        tmp = occurence.replace('mul', '').replace('(', '').replace(')', '').split(',')
        nums = list(map(int, tmp))
        sum += nums[0] * nums[1]
    
    return sum


def main2(file_path):
    with open(file_path) as file:
        lines = file.readlines()

    text = "".join(lines)
    
    expresion = re.compile(r"do\(\)|don\'t\(\)|mul\(\d*,\d*\)")
    occurerces = re.findall(expresion, text)
    print(occurerces)

    sum = 0
    do = True
    for occurence in occurerces:
        if occurence == "do()":
            do = True
            continue
        elif occurence == "don't()":
            do = False
            continue
        
        if not do:
            continue

        tmp = occurence.replace('mul', '').replace('(', '').replace(')', '').split(',')
        nums = list(map(int, tmp))
        sum += nums[0] * nums[1]
    
    return sum

if __name__ == '__main__':
    assert main('test_input.txt') == 161
    print(main('input.txt'))
    assert main2('test_input_2.txt') == 48
    print(main2('input.txt'))