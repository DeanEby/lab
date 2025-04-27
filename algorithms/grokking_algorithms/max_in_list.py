num_list = [4, 5, 7, 8, 3, 5, 1, 8, 2, 11]

def findMax(inlist: list):
    if len(inlist) == 1:
        return inlist[0]
    else:
        findMax(inlist[1:])
        if inlist[0] > findMax(inlist[1:]):
            return inlist[0]
        else:
            return findMax(inlist[1:])
        


print(findMax(num_list))