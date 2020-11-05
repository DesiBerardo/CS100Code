'''
Desimir Berardo
CS100 113
11/5/2020
'''

def initialLetterCount(wordList):
    dict = {}
    for word in wordList:
        if word not in dict:
            dict[word] = [word]
    for word in wordList:
        for letter in word:
            if letter in dict[word]:
                print('test')
                dict[word].append(word)


    return dict



horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']

print(initialLetterCount(horton))