def vowel_counter(list):
    vowels = "aeiouAEIOU"
    vowelCount = 0
    endInVowel = 0

    for i in list:
        if i[0] in vowels:
            vowelCount += 1
        if i[-1] in vowels:
            endInVowel += 1
    return [vowelCount, endInVowel]


list = ["selection","are","dust","smoke","favorite","story"]

print(vowel_counter(list))