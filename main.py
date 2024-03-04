def sort_words(wordlist):
    for i in range(len(wordlist)):
        for j in range(i + 1, len(wordlist)):
            word1 = wordlist[i]
            word2 = wordlist[j]
            min_length = min(len(word1), len(word2))

            for k in range(min_length):
                if ord(word1[k]) > ord(word2[k]):
                    wordlist[i], wordlist[j] = wordlist[j], wordlist[i]
                    break
                elif ord(word1[k]) < ord(word2[k]):
                    break
                elif k == min_length - 1 and len(word1) > len(word2):
                    wordlist[i], wordlist[j] = wordlist[j], wordlist[i]
    return wordlist

words = ['password', 'python', 'word', 'wordlist', 'list']
sorted_words = sort_words(words)
print(sorted_words)
