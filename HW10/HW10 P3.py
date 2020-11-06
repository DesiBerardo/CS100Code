'''
Desimir Berardo
CS100 113
11/5/2020
'''

def ShareOneLetter(wordList):
    dict = {}
    for word in wordList:
        dict[word] = [word]
        for word2 in wordList:
            for letter in word2:
                if letter in word2 and word2 not in dict[word]:
                    dict[word].append(word2)
    return dict

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']

print(ShareOneLetter(horton))
