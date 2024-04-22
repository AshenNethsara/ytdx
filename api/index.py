from flask import Flask, jsonify

app = Flask(YTBox)


@app.route("/")
def home():
    return "YTBox - Hello World", 200


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404
