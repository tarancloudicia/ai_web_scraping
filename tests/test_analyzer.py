import unittest
from sentiment.analyzer import SentimentAnalyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = SentimentAnalyzer()

    def test_analyze_sentiment(self):
        sentiment = self.analyzer.analyze_sentiment("This is a great product!")
        self.assertIsInstance(sentiment, float)
        self.assertGreaterEqual(sentiment, -1)
        self.assertLessEqual(sentiment, 1)

if __name__ == '__main__':
    unittest.main()
