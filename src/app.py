from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"


@app.route("/hello")
def hello_jinja():
    return render_template("hello.html", title="HELLO JINJA2")


if __name__ == "__main__":
    app.run(debug=True)
