from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful friendly chatbot."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response.choices[0].message["content"]
    return jsonify({"reply": reply})

@app.route("/")
def home():
    return "Chatbot API is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
