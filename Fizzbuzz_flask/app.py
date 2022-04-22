from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start():
    title = "What number should I check?"

    return render_template('main.html', title=title)

@app.route("/fizzbuzz/<int:number>")
def fizzbuzz(number):
    l = []
    for n in range(1,number+1):
        if (n%3==0) and (n%5)==0:
            l.append('FizzBuzz')
        elif n%5==0:
            l.append('Buzz')
        elif n%3==0:
            l.append('Fizz')
        else:
            l.append(n)

    return render_template('fizzbuzz.html', l=l, number=number)