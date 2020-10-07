


list = [1, 5, 2, 4, 6]

def oddCount(numlist):
    tally = 0
    for i in numlist:
        if i % 2 == 1:
            tally += 1
    return tally

print(oddCount(list))