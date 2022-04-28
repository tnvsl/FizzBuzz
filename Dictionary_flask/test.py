f = open('words.txt')
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word_list = f.read().splitlines()
words = []
for w in word_list:
    w = w.lower()
    if w[0] == 'y':
        words.append(w)

print(words)
