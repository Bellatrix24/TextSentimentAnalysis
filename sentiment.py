from textblob import TextBlob

def assess_emotion(input_text):
    # Analyze the emotional tone using TextBlob
    text_blob = TextBlob(input_text)
    emotion_score = text_blob.sentiment.polarity

    # Classify the emotion based on the polarity score
    if emotion_score > 0:
        return "Positive"
    elif emotion_score < 0:
        return "Negative"
    else:
        return "Neutral"

def run_sentiment_analysis():
    # Obtain user input for the text to be analyzed
    user_input = input("Please enter the text you'd like to assess for sentiment: ")

    # Analyze the sentiment of the provided text
    detected_sentiment = assess_emotion(user_input)

    # Print out the detected sentiment
    print(f"The sentiment of the provided text is: {detected_sentiment}")

if __name__ == "__main__":
    run_sentiment_analysis()
