import string

letters = list(string.ascii_uppercase)

#print(letters)

input = "XRPCTCRGNEI"

cipher_shift = 0

for shift_num in range(25):
    shift_num = shift_num + 1
    output = ""
    for letter in input:
        #print(letter)
        letter_index = letters.index(letter)
        new_letter_index = (letter_index + shift_num) % 26
        output = output + letters[new_letter_index]
    print(output)


