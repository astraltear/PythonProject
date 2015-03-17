from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return "home!";

@app.route("/")
def root():
    return "index page!!!!"

@app.route("/login/<login_id>")
def login(login_id):
    return "user login id is %s" % login_id

@app.route("/view/<int:idx>")
def view(idx):
    return "use choose index of %d" % idx

@app.route("/login_form")
def login_form():
    return render_template('login_form.html', name='test',age=35)

if __name__ == '__main__':
    app.debug = True
    app.run()
