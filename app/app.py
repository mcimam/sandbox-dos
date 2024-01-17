import random
import string
from flask import Flask, jsonify

app = Flask(__name__)


def fill_mem():
    """Stupid test function"""
    lst = ""
    for i in range(1024 * 30):
        chr = random.choice(string.ascii_letters)
        x = chr * 1024
        lst = lst + x

    return lst


@app.route("/test", methods=["GET"])
def say_hello():
    return jsonify({"msg": "Hello.Test working"})


@app.route("/")
def test_main():
    res = fill_mem()
    return jsonify({"msg": res})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
