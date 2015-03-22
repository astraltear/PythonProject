# -*- coding: utf-8 -*-
import sys
import traceback
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_flask():
    return 'Hello Flask!'

@app.route("/profile",methods=['POST','GET'])
def profile(username=None):
    try:
        error=None
        if request.method =='POST':
            username = request.form['username']
            email = request.form['email']
        else:
            username = request.args.get['username']
            email = request.args.get['email']
    except:
        traceback.print_exc(file=sys.stdout)
            
    return username,email

if __name__ == '__main__':
    app.run()