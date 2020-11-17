def countVowels(text):
    wordList = text.split()
    vowels = 'aeiou'
    d = {}
    for word in wordList:
        if word not in d:
            d[word] = 0
        for letter in word:
            if letter in vowels:
                d[word] += 1
    return d






abe = "government of the people by the people for the people shall not perish"
print(countVowels(abe))