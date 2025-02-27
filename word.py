def len_word(*words):
    word_len = []
    for word in words:
        word_len .append(len(word))
    avg_len = sum(word_len)/len(word_len)
    return (max(word_len) ,avg_len, min(word_len))
    
print(len_word('kama','wanja','roma'))