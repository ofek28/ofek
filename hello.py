from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

def make_bold(function):
    def wrapper_function():
        bold = function()
        return f"<b>{bold}</b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        em = function()
        return f"<em>{em}</em>"
    return wrapper_function


def make_underline(function):
    def wrapper_function():
        u = function()
        return f"<u>{u}</u>"
    return wrapper_function


@app.route('/MaccabiHaifa')
@make_bold
@make_emphasis
@make_underline
def champions():
    return 'Lets celebrate out 15 championship!'

if __name__ == "__main__":
    app.run(debug=True)