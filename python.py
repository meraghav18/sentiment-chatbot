from flask import Flask, request, jsonify, render_template
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"

def chatbot_reply(user_input):
    user_input_lower = user_input.lower()
    sentiment = get_sentiment(user_input)

    if "hi" in user_input_lower or "hello" in user_input_lower:
        return "Hello there! How can I help you today?"

    if sentiment == "positive":
        return "I'm glad to hear that!"
    elif sentiment == "negative":
        return "I'm sorry to hear that. I'm here for you."
    elif sentiment == "neutral":
        return "Got it! Tell me more about this."
    else:
        return "Thanks for sharing. Tell me more."

# Serve chatbot page
@app.route("/")
def home():
    return render_template("chatbot.html")

# API endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    if user_message.lower() in ["bye", "exit", "quit"]:
        return jsonify({"response": "Goodbye! Take care! All the best for the future!"})
    
    response = chatbot_reply(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
