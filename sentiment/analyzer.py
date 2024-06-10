import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer:
    def __init__(self):
        nltk.download('vader_lexicon')
        self.sia = SentimentIntensityAnalyzer()
    
    def analyze_sentiment(self, review):
        score = self.sia.polarity_scores(review)
        return score['compound']
