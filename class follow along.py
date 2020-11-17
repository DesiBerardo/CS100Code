import dog

sugar = dog.Dog('Sugar', 'Border Collie')

print(sugar.tricks)
sugar.teach('frisbee')
print(sugar.tricks)
sugar.knows('frisbee')
sugar.teach('fetch')
sugar.knows('fetch')
sugar.knows('arithmetic')
print(dog.Dog.species)
print(sugar.species)