
backwards_sentence = " "
sentence = "The quick brown fox jumpes over the lazy dog"
words = sentence.split(" ")
for x in words:
    backwards = x[::-1]
    backwards_sentence = backwards_sentence + " " + backwards
print(backwards_sentence)
    
