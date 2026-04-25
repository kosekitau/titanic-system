from flask import Flask, request, render_template

from .database import db_session
from .models import Person


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"


@app.route("/hello")
def hello_jinja():
    return render_template("hello.html", title="HELLO JINJA2")


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        person = Person(**request.form.to_dict())
        db_session.add(person)
        db_session.commit()
        return f"Registration Successful"
    return render_template("registration.html")


if __name__ == "__main__":
    app.run(debug=True)
