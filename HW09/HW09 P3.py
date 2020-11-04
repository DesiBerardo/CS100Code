'''
Desimir Berardo
CS100 113
11/4/2020
'''
import string

def repeat_words(in_file, out_file):
    file1 = open(in_file, 'r')
    file2 = open(out_file, 'w')

    text_strip = file1.read()
    text_strip = text_strip.lower()
    text_strip_list = text_strip.split()

    text_list = []
    for word in text_strip_list:
        text_list.append(word.strip(string.punctuation))
    print(text_list)

    for word in text_list:
        file2.write(word)

    print(text_strip)



inF = 'catInTheHat.txt'
outF = 'catout.txt'
repeat_words(inF, outF)