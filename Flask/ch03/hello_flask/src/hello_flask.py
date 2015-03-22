# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/helloFlask2')
@app.route('/helloFlask2/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()
