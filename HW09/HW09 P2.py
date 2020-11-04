'''
Desimir Berardo
CS100 113
11/4/2020
'''

def file_stats(in_file):
    file = open(in_file, 'r')
    countLine = 0
    countCharacter = len(file.read())
    file.close()
    file = open(in_file, 'r')
    for line in file:
        countLine += 1
    file.close()
    file = open(in_file, 'r')
    file_text = file.read()
    file_text = file_text.split()
    file.close()

    print('lines:', countLine)
    print('words:', len(file_text))
    print('characters:', countCharacter)

file_stats('created_equal.txt')