import pandas as pd
import json
import streamlit as st
from textblob import TextBlob

# Function to analyze sentiment using TextBlob
def analyze_sentiment(text):
    analysis = TextBlob(text)
    # Classify as positive, negative, or neutral based on polarity
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Streamlit app title
st.title("Sentiment Analysis Tool")

# File uploader for JSON
uploaded_file = st.file_uploader("Choose a JSON file", type=["json"])
if uploaded_file is not None:
    try:
        # Read the JSON data
        data = pd.read_json(uploaded_file)
        if 'Text' in data.columns:
            data['Sentiment'] = data['Text'].apply(analyze_sentiment)
            st.write(data)  # Display the data
        else:
            st.error("The uploaded JSON file must contain a 'Text' column.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
        

