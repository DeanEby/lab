list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

target = 'd'

def binarySearch(targ, list):
    list_length = len(list) -1
    guess_index = round(list_length / 2)
    #print(f"guess {list[start_index]}")
    if list[guess_index] == targ:
        output = list[guess_index]
        return output
    else:
        lista = list[:guess_index + 1]
        listb = list[guess_index:]
        #print(f"lista {lista} listb {listb}")
        if lista[-1] > targ:
            return binarySearch(targ, lista)
        else:
            return binarySearch(targ, listb)
    

x = binarySearch(target, list)
print(x)