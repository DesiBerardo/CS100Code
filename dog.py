'''
Desimir Berardo
CS100 113
11/17/2020
'''

class Dog:
    '''Creates a Dog with many features of said Dog.'''

    species = 'canis familiaris'

    def __init__(self, dog_name, dog_breed):
        self.name = dog_name
        self.breed = dog_breed
        self.tricks = []

    def teach(self, trick):
        self.tricks.append(trick)
        print(self.name + " knows " + trick)

    def knows(self, trick):
        if trick in self.tricks:
            print('Yes, ' + self.name + ' knows ' + trick)
            return True
        else:
            print('No, ' + self.name + ' does not know ' + trick)
            return False
