artists = [
    ['radiohead', 156],
    ['Kishore Kumar', 141],
    ['The Black Keys', 35],
    ['Neutral Milk Hotel', 94],
    ['Beck', 88],
    ['The Strokes', 61],
    ['WILCO', 111]
    ]

# The first method described, finding the max value in the list repeatedly until the list is sorted.
def method1(in_list: list):
    sorted_list = []
    in_list_og_length = len(in_list)
    while len(sorted_list) < in_list_og_length:
        max = in_list[0]
        max_index = 0
        for index, value in enumerate(in_list):
            if value[1] > max[1]:
                max = value
                max_index = index
        print(max)
        sorted_list.append(max)
        in_list.pop(max_index)


method1(artists)