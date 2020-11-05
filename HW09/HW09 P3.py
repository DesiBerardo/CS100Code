'''
Desimir Berardo
CS100 113
11/4/2020
'''
import string

def repeat_words(in_file, out_file):
    file1 = open(in_file, 'r')
    file2 = open(out_file, 'w')

    for line in file1:
        allWords = []
        repeatWords = []

        words = line.split()

        for word in words:
            word1 = word.lower()
            word2 = word1.strip(string.punctuation)

            if word2 in allWords and word2 not in repeatWords:
                repeatWords.append(word2)
            else:
                allWords.append(word2)

        for word in repeatWords:
            file2.write(word + ' ')
        file2.write('\n')
    file1.close()
    file2.close()

inF = 'catInTheHat.txt'
outF = 'catout.txt'
repeat_words(inF, outF)
