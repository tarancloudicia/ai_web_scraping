# AI-Powered Web Scraping

This project demonstrates an AI-powered web scraping solution for extracting, analyzing, and storing product data and customer reviews from e-commerce websites.

## Features
- Data extraction using BeautifulSoup and Requests
- Sentiment analysis using NLTK
- Data storage in MongoDB
- Scalable and modular architecture
- Unit tests for all components

## Installation

1. Clone the repository
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Configure your MongoDB connection in `config.py`.

## Usage

To run the scraper:
```bash
python main.py
```

## Project Structure

- `scraper/`: Contains the web scraping code
- `sentiment/`: Contains the sentiment analysis code
- `database/`: Contains the database interaction code
- `tests/`: Contains the unit tests
- `utils/`: Contains utility functions like logging

## Running Tests

To run the unit tests:
```bash
pytest
```