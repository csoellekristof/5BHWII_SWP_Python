import random

lottodict = {}
for i in range(1,46):
    lottodict[i] = 0


for i in range(1000):
    lottolist = [1,45]

    for i in range(1,46):
        lottolist.append(i)


    for i in range (6):
        rand_num = random.choice(lottolist)
        lottodict[rand_num] = lottodict[rand_num] + 1
        lottolist.remove(rand_num)

print (lottodict)


