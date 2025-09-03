from textblob import TextBlob


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
        return "Got It Tell me more about this"
    else:
        return "Thanks for sharing. Tell me more."


print(" ChatBot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print(" ChatBot: Goodbye! Take care! All the best for the future! ")
        break
    response = chatbot_reply(user_input)
    print(" ChatBot:", response)
