from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World this is my home page"

@app.route("/about")
def about():
    return "This is the about page!"

@app.route("/periodic-table")
def periodictable():
    return render_template("index.html")