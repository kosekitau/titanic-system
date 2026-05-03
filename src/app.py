from flask import Flask, request, render_template

from src.database import db_session
from src.models import Person
from src.ai_interface import ai_pipeline

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
        return "Registration Successful"
    return render_template("registration.html")


@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    result = ""
    if request.method == "POST":
        result = ai_pipeline(request.form.to_dict())
    return f"Prediction Result {result}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8501, debug=True)
