name = 'kamau'
for index ,letter in enumerate(name):
    print(name[:index+1])
#
word = 'computer'
if word[0] in 'aeiou':
    print(f'{word}way')
else:
    print(f'{word[1:]}{word[0]}ay')


print(f'{word[0].upper()}{word[1:]}')

