from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"


@app.route("/hello")
def hello_jinja():
    return render_template("hello.html", title="HELLO JINJA2")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        id = request.form["id"]
        # pclass=1, sex="male", age=20, slibSp=1, parch=1, ticket="113803", fare=7.25, cabin="G6", embarked="S"
        return f"Registration Successful id:{id}"
    return render_template("registration.html")


if __name__ == "__main__":
    app.run(debug=True)
