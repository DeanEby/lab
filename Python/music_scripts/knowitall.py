import random
import string
import time
song_words = ['knowitall', 'strangers', 'hiddenmoves', 'ursodramatic', 'wecantalkaboutit', 'uknoweverything', 'nothingleavesthehome', 'headdown', 'itfallsapartaroundyou', 'itwouldbethesamewithoutyou', 'willimakeitoutalive', 'idontwannamakeitreal']
def createRandomString():
    wordLengths = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    output = ''
    for i in range(random.choice(wordLengths)):
        output = output + random.choice(string.ascii_letters + string.punctuation)
    return output

for i in range(50000):
    
    dice = random.randint(0, 8)
    if dice <= 1:
        songword = random.choice(song_words)
        print(f"\033[31m{songword}\033[0m", end='')
    else:
        if dice == 5:
            print(createRandomString(), end='', flush=True)
        else:
            print(createRandomString(), end='')
    if dice == 3:
        print(' ' * random.randint(1, 10), end='')
    time.sleep(0.005)

