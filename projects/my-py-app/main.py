from flask import Flask
from random import randint

from projects.calculator.calculator import Calculator

app = Flask(__name__)
my_calc = Calculator()

@app.route("/")
def hello():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    message = "{} + {} = {}".format(num1, num2, mycalc.add(num1, num2))

if __name__ == "__main__":
    app.run()
