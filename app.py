import random

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', )
def page_index():
    return "It works"


@app.route("/python")
def page_python():
    return "<strong>это язык который мы учим</strong>"


@app.route("/java")
def page_java():
    return "<strong>а это мы не учим</strong>"


@app.route("/php")
def page_php():
    return "<strong>а это что такое вообще</strong>"


@app.route("/random")
def page_random_letter():
    return random.choice(list("ABCDEFGHIKLMNOPQRSTVXYZ"))


@app.route("/detect/<x>")
def page_detect(x: str):
    if x.isdigit():
        return "это число"
    return "это не число"

@app.route("/avg")
def page_avg():
    user_list = [23, 16, 144, 72, 90, 11, 5]
    return f"{sum(user_list)/len(user_list):.2f}"


app.run()
