'''


How many times doeas a word appear in a sentence?
'''
sentence = input("enter a word")

words = sentence.split(" ")

wordsCount = {} # dictionary

for words in sentence:
    if (words in wordsCount):
        wordsCount[words] += 1
    else:
        wordsCount[words] = 1
print(wordsCount)
