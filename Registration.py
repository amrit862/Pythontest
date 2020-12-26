from flask import Flask, jsonify
# from flask_restful import Resource, Api

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify({"about": "Hello World"})


@app.route('/test', methods=['GET', 'POST'])
def helloTest():
    return jsonify({"about": "Hello Test"}), 201


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
