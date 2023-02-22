from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(1, 9)

@app.route("/")
def guess():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src=https://media3.giphy.com/media/l41YtZOb9EUABnuqA/200.webp?cid=ecf05e47gtq2hjetnjd5e3thppaqmd0b95zp61xhquf5nktq&rid=200.webp&ct=g>"


@app.route("/<int:number>")
def choice(number):
    if number > random_number:
        return f"<h1 style='color:green';>{number} is too high :(</h1>" \
               "<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"
    elif number < random_number:
        return f"<h1 style='color:red';>{number} is too low :(</h1>" \
               "<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"
    else:
        return f"<h1 style='color:black';>You found me! :D</h1>" \
               "<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>"


if __name__ == "__main__":
    # run app in debug mode - auto-reload
    app.run(debug=True)
