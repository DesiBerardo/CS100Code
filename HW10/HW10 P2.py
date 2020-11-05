'''
Desimir Berardo
CS100 113
11/5/2020
'''

def initialLetterCount(wordList):
    dict = {}
    for word in wordList:
        if word[0] not in dict:
            dict[word[0]] = [word]
    return dict



horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']

print(initialLetterCount(horton))