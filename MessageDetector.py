import random
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

responses = {
    "positive" : [
        "Positive"
    ],
    "negative" : [
        "Negative"
    ],
    "neutral" : [
        "Neutral"
    ]
}

def get_sentiment(text):
    "Analyze the sentiment of a message"
    score = sia.polarity_scores(text)
    if score['compound'] >= 0.05:
        return "positive"
    elif score['compound'] <= -0.05:
        return "negative"
    else:
        return "neutral"
    
def chatbot_reply(message):
    "Generate a response based on sentiment"
    sentiment = get_sentiment(message)
    return random.choice(responses[sentiment])

print("Message Detector is running")
while True:
    user_input = input(":")  
    if user_input.lower() == "exit":
        print("Bye Bye")
        break
    response = chatbot_reply(user_input) 
    print(f"Chatbot: {response}")
    