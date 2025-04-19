text ="""a b c a a a"""

word_count = {}

for I in  text.split():
    
    if I in word_count:
        word_count[I] += 1
    else:
        word_count[I] = 1
print(word_count)