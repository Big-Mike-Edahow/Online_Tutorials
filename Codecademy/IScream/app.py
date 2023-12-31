# app.py

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    flavor = 'chocolate'
    return render_template('index.html', flavor=flavor)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)


