# advent of code day 3 part 1 https://adventofcode.com/2024/day/3/answer

import re


sum = 0
#file = open("2024/3-1.txt", "r")

input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


def recover_memory(data):
    sum = 0
    valid = re.findall(r'mul\(\d+,\d+\)', data)
    #print(valid)
    for i in valid:
        # break the numbers out of the formatting
        i = i.split(",")
        # get rid of mul(
        i[0] = i[0][4:]
        # get rid of )
        i[1] = i[1][0:-1]

        #might as well do the arithmetic while we are here
        product = int(i[0]) * int(i[1])
        sum = sum + product
        #fileList.append(i)

    print(sum)


recover_memory(input)