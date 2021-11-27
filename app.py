import json

from flask import Flask, request, render_template, Response

app = Flask(__name__)


@app.route('/add', methods=["POST"])
def hello_world():
    data = {
        "object": None,
        "msg": "成功",
        "code": 200,
        "result": False
    }
    return Response(json.dumps(data), content_type='application/json')


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
