import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def perform_sentiment_analysis(data):
    # Initialize VADER SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()
    
    # Apply sentiment analysis on the 'headline' column
    data['sentiment'] = data['headline'].apply(lambda x: sia.polarity_scores(x)['compound'])

    # Categorize the sentiment into positive, negative, or neutral
    data['sentiment_label'] = data['sentiment'].apply(lambda score: 'positive' if score > 0 else ('negative' if score < 0 else 'neutral'))

    print("Sentiment analysis complete. Here are some samples:")
    print(data[['headline', 'sentiment', 'sentiment_label']].head())

    return data