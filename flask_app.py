import os

from flask import Flask

from persons import db

env = os.environ["FLASK_ENV"]
fixtures_file = f"fixtures/{env}.json"

db.setup(fixtures_file)

app = Flask(__name__)


# We will delete this in the end
@app.route("/")
def hello() -> str:
    return "Hello, World!"
