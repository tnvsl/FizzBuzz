from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def homepage():
    title = 'My homepage'
    intro = 'Text'

    groceries = ['apples', 'bannanas', 'carrots']
    
    return render_template('app.html', title=title, text=intro, groceries=groceries)

@app.route("/second")
def second():

    picture_url = url_for('static', filename='water.png')

    return render_template('app2.html', picture_url=picture_url)