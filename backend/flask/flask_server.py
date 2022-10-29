from flask import Flask
# from core import app

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/getUser")
def getUser():
    return "<p>Hello, World!</p>"

app.run(debug = True, port=3002) 