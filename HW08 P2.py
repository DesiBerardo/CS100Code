'''
Desimir Berardo
CS100 113
10/22/2020
'''



def twoWords(length, firstLetter):
    lengthLoop = True
    while lengthLoop == True:
        word_1 = input('Enter a ' + str(length) + ' letter word please: ')
        if len(word_1) == length:
            lengthLoop = False
    letterLoop = True
    while letterLoop == True:
        word_2 = input('Enter a word beginning with ' + firstLetter + ' please: ')
        if word_2[0] == firstLetter.upper() or word_2[0] == firstLetter.lower():
            letterLoop = False
    return [word_1, word_2]



print(twoWords(5, 'H'))