# Advent of code Day 2 Part 2

# A list containing lists for all the numbers of each line.
fileList = []
# a text file with the input numbers "reports" with "labs"
file = open("2024/2-1input.txt", "r")
# read in lines from file and break into fileList
for line in file:
    lineList = line.split()
    fileList.append(lineList)
#print(fileList)

# Total number of safe reports
total = 0
# iterate through lines from file as list of numbers.
for i in fileList:
    # the location of the lab to remove
    n = 0
    # additional loop for removing labs
    while n < len(i):
        # this templist needed to be a copy of i so popping would not effect it
        tempList = list(i)
        # remove the lab we want
        tempList.pop(n)
        # while loop counter
        count = 0
        # will turn false if a report is deemed unsafe
        safe = True
        # stores if we are increasing or decreasing
        dir = 0
        # increment n
        n = n + 1
        # loop through each line
        while count < (len(tempList) - 1):
            # our two values to compare
            valueA = int(tempList[count])
            valueB = int(tempList[count + 1])
            # the two values should not match
            if valueA == valueB:
                safe = False
            elif valueA < valueB:
                if dir == 0 or dir == 1:
                    dir = 1
                else:
                    safe = False
                     # make sure the distance is at least one but not more than three
                if valueB - valueA >= 1 and valueB - valueA <=3:
                    pass
                else:
                    safe = False
            elif valueA > valueB:
                if dir == 0 or dir == -1:
                    dir = -1
                else:
                    safe = False
                     # make sure the distance is at least one but not more than three
                if valueA - valueB >= 1 and valueA - valueB <= 3:
                    pass
                else:
                    safe = False
                    


            
            count = count + 1
            #print(safe)
            
            # we don't need to keep testing if a pair is unsafe
            if not safe:
                #print(tempList, "not safe")

                break
        # if a line made it though safe we add to total and break out
        # because we dont need to keep testing removing diff labs
        if safe:
            #print(i, "safe")
            total = total + 1
            break
print("total: " + str(total))