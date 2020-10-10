def rev_str(sentence):
    words = sentence.split(" ")
    reverse = ' '.join(reversed(words))
    return reverse

sentence = "Hello there mate"
print(rev_str(sentence))