from flask import Flask, render_template, request
import sqlite3



app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")



@app.route("/survey")
def survey():
    return render_template("survey_page.html")


app.run()