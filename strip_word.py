num =123.4567
word = str(num)
int_part,decimal_part = word.split('.')

before =2
after = 3

print(f'word :{int_part[-2:]}.{decimal_part[:3]}')