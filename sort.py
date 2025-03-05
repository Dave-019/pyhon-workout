words = ['kam','wnaajau','roma']



def num_vowels(word):
    count = 0
    for i in word:
        if i in 'aeiou':
            count +=1
    return count

sorted_words = sorted(words, key=num_vowels)
print(sorted_words)
