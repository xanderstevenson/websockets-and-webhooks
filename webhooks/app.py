from flask import Flask, render_template, request, jsonify
from webhook_processor import process_webhook

app = Flask(__name__)
app.config.from_pyfile("config.py")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json  # Assuming webhook data is JSON
    response = process_webhook(data)
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(debug=True)
