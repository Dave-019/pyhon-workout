def pl_sentence():
    sentence =input("Enter ur sentenc:")
    word = sentence.split(' ')
    pl_sen = ''
    for i in word:
        pl_sen += i + 'way '
    return(pl_sen)
print(pl_sentence())