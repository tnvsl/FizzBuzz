from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def start():
    title = "What word should I check?"

    return render_template('main.html', title=title)

@app.route("/words/<string:word>")
def words(word):
    f = open('words.txt')
    l = []
    word_list = f.read().splitlines()
    for w in word_list:
        w = w.lower()
        if sorted(word) == sorted(w):
            l.append(w)

    return render_template('words.html', word=word, l=l)