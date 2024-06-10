import unittest
from pymongo import MongoClient
from database.db import Database
from config import MONGO_URI, DATABASE_NAME, COLLECTION_NAME

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.client = MongoClient(MONGO_URI)
        self.collection = self.client[DATABASE_NAME][COLLECTION_NAME]

    def test_insert_data(self):
        initial_count = self.collection.count_documents({})
        data = [{'name': 'Test Product', 'price': '$10', 'review': 'Good', 'sentiment': 0.5}]
        self.db.insert_data(data)
        new_count = self.collection.count_documents({})
        self.assertEqual(new_count, initial_count + 1)

    def tearDown(self):
        self.collection.delete_many({'name': 'Test Product'})

if __name__ == '__main__':
    unittest.main()
