from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
<<<<<<< HEAD
    return '<h1>Hello, Class!</h1>'
=======
    return '<h1>Hello, Julian!</h1>'
>>>>>>> e6a78af (change greeting)


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
