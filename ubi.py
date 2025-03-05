sentence = 'milk kamau'
new_str = ''
for char in sentence:
    if char in 'aeiou':
       new_str += 'ub' + char
    else:
        new_str += char
print(new_str)