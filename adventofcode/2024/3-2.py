# advent of code day 3 part 2 https://adventofcode.com/2024/day/3/answer

import re


sum = 0
file = open("2024/3-1.txt", "r")
# used to control do() don't() state
active = True

for line in file:
    # finds all valid instructions
    valid = re.findall(r"(?:mul\(\d+,\d+\)|do\(\)|don't\(\))", line)
    #print(valid)
    for i in valid:
        # set active state to True
        if i == "do()":
            active = True
        # set active state to False
        elif i == "don't()":
            active = False
        else:
            # if last do()/don't() command was was do()
            # run this code
            if active == True:
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

#for i in fileList:

print(sum)