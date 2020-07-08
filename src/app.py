'''
 # @ Author: Hasi6 (hasitha.chandula@gmail.com)
 # @ Create Time: 2020-07-09 05:30:00
 # @ Modified by: Hasi6 (hasitha.chandula@gmail.com)
 # @ Modified time: 2020-07-09 01:01:13
 # @ Description: easyHR 2020
 '''


from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"
