from scraper.scraper import Scraper
from sentiment.analyzer import SentimentAnalyzer
from database.db import Database
from utils.logger import setup_logging

def main():
    setup_logging()
    
    scraper = Scraper()
    data = scraper.scrape_data()

    analyzer = SentimentAnalyzer()
    for item in data:
        item['sentiment'] = analyzer.analyze_sentiment(item['review'])

    db = Database()
    db.insert_data(data)
    
    print("Scraping and analysis complete. Data stored in MongoDB.")

if __name__ == "__main__":
    main()
