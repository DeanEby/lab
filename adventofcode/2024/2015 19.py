# Advent of code day 19
# I put the replacement input into a txt file because I was too lazy
# to manually copy the data over.

# each line will be stored as a list in this list
fileList = []
file = open("2024/19.txt", "r")
# read in the data
for line in file:
    #print(line)
    # remove newline character
    line = line.strip()
    # split on this delim.
    lineList = line.split(" => ")
    fileList.append(lineList)

#print(fileList)
# The calibrate molecule
calibrate = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"
# This will store the many replacement possibilities
possibilities = []
# iterate through the calibration molecule
for char in range(len(calibrate)):
    # get the character at the current position
    a = calibrate[char]
    # iterate through our list of lines from the text
    for i in fileList:
        # i[0] is the first column for I which we will be using to match to a
        b = i[0]

        # if current character in molecule matches a replacement character:
        if a == b:
            # turn to list to make it easier to replace the character
            cList = list(calibrate)
            # current character is replaced by the 2nd column of the matched replacement character.
            cList[char] = i[1]
            # turn back to string
            cString = "".join(cList)
            # check for duplicates
            if cString not in possibilities:
                possibilities.append(cString)
            else: 
                print("duplicate:", cString)


            # make sure that we aren't on the last character in calibrate
            # avoids: IndexError: string index out of range 
        if char != len(calibrate) - 1:
            # some of the values in b are 2 characters long
            # we need to check for those
            if calibrate[char] + calibrate[char + 1] == i[0]:
                # same list replacement
                cList = list(calibrate)
                # have to pop off 2nd character before replacing first or else
                # we lose it
                cList.pop(char + 1)
                cList[char] = i[1]
                cString = "".join(cList)
                #print(cString)
                if cString not in possibilities:
                    possibilities.append(cString)
                else: 
                    print("duplicate:", cString)
                #print("match", calibrate[char], i[0])
            

print(len(possibilities))



# # Check to see if there is repeat replacements
# # there are none.
# # this doesn't actually mean we don't need to check for duplicates,
# # as replacements could still hypothetically cause a collision, as shown in 
# # the example.
# for i in fileList:
#     i1 = i[1]
#     for n in fileList:
#         n1 = n[1]

#         if i1 == n1 and i != n:
#             print("Matching 2nd value")
#             print(i)
#             print(n)


