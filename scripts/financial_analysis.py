import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import matplotlib.pyplot as plt
from gensim import corpora
from gensim.models import LdaModel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def perform_sentiment_analysis(df):
    # Initialize VADER SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()
    
    # Apply sentiment analysis on the 'headline' column
    df['sentiment'] = df['headline'].apply(lambda x: sia.polarity_scores(x)['compound'])

    # Categorize the sentiment into positive, negative, or neutral
    df['sentiment_label'] = df['sentiment'].apply(lambda score: 'positive' if score > 0.05 else ('negative' if score < -0.05 else 'neutral'))

    print("Sentiment analysis complete. Here are some samples:")
    print(df[['headline', 'sentiment', 'sentiment_label']].head())

    return df
