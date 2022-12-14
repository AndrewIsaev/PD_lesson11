from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def task1():
    user_dict = {"username": "alexy_001", "email": "alexy@skyeng.ru", "phone": "+1555223311"}
    return render_template("task1.html", user_dict=user_dict)

@app.route("/task2")
def task2():
    user_dict = {1: "Самара", 2: "Краснодар", 3: "Сочи", 4: "Новосибирск", 5: "Вышгород"}
    return render_template("task2.html", cities=user_dict.values())

@app.route("/task3")
def task3():
    user_dict = {1: "Самара", 2: "Краснодар", 3: "Сочи", 4: "Новосибирск", 5: "Вышгород"}
    return render_template("task3.html", user_dict=user_dict)


if __name__ == '__main__':
    app.run()
