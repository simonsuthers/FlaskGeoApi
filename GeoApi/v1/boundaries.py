from .. import app
from flask import jsonify

@app.route("/boundary")
def boundary():
    return jsonify("hello", "user")

