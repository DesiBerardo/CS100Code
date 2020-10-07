'''
Desimir Berardo
CS100 113
10/7/2020
'''

def space():
    print('-' * 50)

def hasFinalLetter(strList, letters):
    finalList = []
    for i in strList:
        if i[-1] in letters:
            finalList.append(i)
    return finalList


def isDivisible(maxInt, twoInts):
    finalList = []
    for i in range(1, maxInt):
        if i % twoInts[0] == 0 and i % twoInts[1] == 0:
            finalList.append(i)
    return finalList



strList1 = ["borN","announceD","cast","stood","steady","camera"]
finalLetter1 = "larfDHesyN"

print(hasFinalLetter(strList1, finalLetter1))

strList2 = ["spell","cave","outline","grounD","instrument","statement"]
finalLetter2 = "djkwor"

print(hasFinalLetter(strList2, finalLetter2))

strList3 = ["tall","contain","by","whistlE","contain","Mine"]
finalLetter3 = "lnyEne"

print(hasFinalLetter(strList3, finalLetter3))

space()

maxInt1 = 55
twoInts1 = (2, 5)

print(isDivisible(maxInt1, twoInts1))

maxInt2 = 77
twoInts2 = (2, 4)

print(isDivisible(maxInt2, twoInts2))

maxInt3 = 15
twoInts3 = (17, 36)

print(isDivisible(maxInt3, twoInts3))

