from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def homepage():
    title = 'My homepage'
    intro = 'Text'

    scrambled_words = ['act', 'god']

    groceries = ['apples', 'bannanas', 'carrots']
    
    return render_template('app.html', title=title, text=intro, groceries=groceries, scrambled_words=scrambled_words)

@app.route("/second")
def second():

    picture_url = url_for('static', filename='water.png')

    return render_template('app2.html', picture_url=picture_url)

@app.route("/count/<int:count_to>")
def count(count_to):
    
    l= list(range(1,count_to+1))

    return render_template('count.html', last_number=count_to, numbers=l)

@app.route("/words/<string:word>")
def words(word):
    f = open('words.txt')
    word_list = f.read().splitlines()
    is_real = word in word_list

    return render_template('words.html', word=word, is_real=is_real)