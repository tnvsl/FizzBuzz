from operator import is_
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def start():
    title = "What word should I check?"

    return render_template('main.html', title=title)

@app.route("/dictionary/<string:letter>")
@app.route("/dictionary")
def dictionary(letter=''):
    f = open('words.txt')
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    word_list = f.read().splitlines()
    words = []
    for w in alphabet:
        words.append(letter+w)

    letter = letter.upper()

    a = 0
    for word in word_list:
        if word.startswith(letter):
            a+=1


    if letter in word_list:
        is_word = True
    else:
        is_word = False


    return render_template('dictionary.html', alphabet=alphabet, words=words, wordlen=a, is_word=is_word, letter=letter)