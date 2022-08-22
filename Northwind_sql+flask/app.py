from flask import Flask, render_template
import database2

app = Flask(__name__)

@app.route('/')
def hello_world():
    facts = database2.get_all_facts()
    return render_template('index.html', facts=facts)


if __name__ == '__main__':
    app.run()