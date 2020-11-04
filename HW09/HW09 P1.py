'''
Desimir Berardo
CS100 113
11/4/2020
'''

def file_copy(in_file, out_file):
    r = open(in_file, 'r')
    w = open(out_file, 'w')
    w.write(r.read())
    r.close()
    w.close()



file_copy('created_equal.txt', 'copy.txt')
copy_f = open('copy.txt', 'r')
print(copy_f.read())

copy_f.close()