from flask import Flask, render_template, request, jsonify
from chatbot import get_response  # Import our response function

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_bot_response():
    user_input = request.json["message"]
    bot_response = get_response(user_input)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
