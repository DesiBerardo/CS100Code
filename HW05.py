'''
Desimir Berardo
CS100 113
10/2/2020
'''

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']

char = 'J'
position = 0


def space():
    print('-' * 50)


for i in months:
    if char in i[0]:
        print(months[position])
    position = position + 1

space()

for i in range(99):
    if i % 2 == 0 and i % 5 == 0:
        print(i)

space()

horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for letter in horton:
    if letter in vowels:
        print(letter)
