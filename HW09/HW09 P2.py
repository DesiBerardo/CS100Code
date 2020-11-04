'''
Desimir Berardo
CS100 113
11/4/2020
'''

def file_stats(in_file):
    file = open(in_file, 'r')
    countLine = 0
    for line in file:
        countLine += 1
    countCharacter = file.read()


    print('lines:', countLine)
    print('words:', )
    print('characters:', countCharacter)

file_stats('created_equal.txt')