import unittest
from scraper.scraper import Scraper

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = Scraper()

    def test_scrape_data(self):
        data = self.scraper.scrape_data()
        self.assertTrue(len(data) > 0)
        self.assertIn('name', data[0])
        self.assertIn('price', data[0])
        self.assertIn('review', data[0])

if __name__ == '__main__':
    unittest.main()
