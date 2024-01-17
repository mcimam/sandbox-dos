from concurrent.futures import ThreadPoolExecutor
import requests
from flask import Flask, jsonify

app = Flask(__name__)

pool = ThreadPoolExecutor(max_workers=10)


def fetch(url):
    page = requests.get(url)
    return page.text
    # Catch HTTP errors/exceptions here


@app.route("/attack/0", methods=["GET"])
def say_att0():
    urls = ["http://defender0"] * 10
    result = []
    for page in pool.map(fetch, urls):
        result += page

    return jsonify({"msg": "Attack Done", "result": result})


@app.route("/attack/1", methods=["GET"])
def say_att1():
    urls = ["http://defender1"] * 10
    result = []
    for page in pool.map(fetch, urls):
        result += page

    return jsonify({"msg": "Attack Done", "result": result})


@app.route("/")
def test_main():
    return jsonify({"msg": "GO ATTACK"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
