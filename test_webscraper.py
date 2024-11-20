import unittest
from unittest.mock import patch, MagicMock
import sqlite3
from webscraper import init_db, WebScraper, app
import threading
import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request
import logging
import asyncio
import aiohttp

# FILE: test_webscraper.py

class TestWebScraper(unittest.TestCase):
    # Test case for the init_db function
    @patch('webscraper.sqlite3.connect')
    def test_init_db(self, mock_connect):
        # Create a mock connection object
        mock_conn = MagicMock()
        # Set the return value of the sqlite3.connect mock to the mock connection object
        mock_connect.return_value = mock_conn
        # Call the init_db function
        init_db()
        # Assert that sqlite3.connect was called with 'scraper.db'
        mock_connect.assert_called_with('scraper.db')
        # Assert that the cursor's execute method was called once
        mock_conn.cursor().execute.assert_called_once()
        # Assert that the connection's commit method was called once
        mock_conn.commit.assert_called_once()
        # Assert that the connection's close method was called once
        mock_conn.close.assert_called_once()

    # Test case for the fetch_page method of the WebScraper class
    @patch('webscraper.aiohttp.ClientSession.get')
    def test_fetch_page(self, mock_get):
        # Create a mock response object
        mock_response = MagicMock()
        # Create a future object and set its result to 'Mocked HTML content'
        mock_response.text = asyncio.Future()
        mock_response.text.set_result('Mocked HTML content')
        # Set the return value of the aiohttp.ClientSession.get mock to the mock response object
        mock_get.return_value.__aenter__.return_value = mock_response

        # Create an instance of the WebScraper class
        scraper = WebScraper('https://example.com', ['page1'])
        # Get the event loop
        loop = asyncio.get_event_loop()
        # Run the fetch_page coroutine and get the result
        result = loop.run_until_complete(scraper.fetch_page(mock_get, 'https://example.com/page1'))
        # Assert that the result is 'Mocked HTML content'
        self.assertEqual(result, 'Mocked HTML content')

    # Test case for the scrape method of the WebScraper class
    @patch('webscraper.aiohttp.ClientSession.get')
    @patch('webscraper.BeautifulSoup')
    def test_scrape(self, mock_soup, mock_get):
        # Create a mock response object
        mock_response = MagicMock()
        # Create a future object and set its result to an HTML string with two titles
        mock_response.text = asyncio.Future()
        mock_response.text.set_result('<html><h1>Title 1</h1><h1>Title 2</h1></html>')
        # Set the return value of the aiohttp.ClientSession.get mock to the mock response object
        mock_get.return_value.__aenter__.return_value = mock_response

        # Set the return value of the BeautifulSoup mock to a mock object with a find_all method
        mock_soup.return_value.find_all.return_value = [MagicMock(get_text=lambda: 'Title 1'), MagicMock(get_text=lambda: 'Title 2')]

        # Create an instance of the WebScraper class
        scraper = WebScraper('https://example.com', ['page1'])
        # Get the event loop
        loop = asyncio.get_event_loop()
        # Run the scrape coroutine
        loop.run_until_complete(scraper.scrape('page1'))
        # Assert that the results attribute of the scraper object contains the expected titles and URLs
        self.assertEqual(scraper.results, [('Title 1', 'https://example.com/page1'), ('Title 2', 'https://example.com/page1')])

    # Test case for the save_to_db method of the WebScraper class
    @patch('webscraper.sqlite3.connect')
    def test_save_to_db(self, mock_connect):
        # Create an instance of the WebScraper class
        scraper = WebScraper('https://example.com', ['page1'])
        # Set the results attribute of the scraper object
        scraper.results = [('Title 1', 'https://example.com/page1'), ('Title 2', 'https://example.com/page1')]

        # Create a mock connection object
        mock_conn = MagicMock()
        # Set the return value of the sqlite3.connect mock to the mock connection object
        mock_connect.return_value = mock_conn

        # Call the save_to_db method
        scraper.save_to_db()
        # Assert that sqlite3.connect was called with 'scraper.db'
        mock_connect.assert_called_with('scraper.db')
        # Assert that the cursor's executemany method was called once with the expected SQL query and data
        mock_conn.cursor().executemany.assert_called_once_with('INSERT INTO data (title, url) VALUES (?, ?)', scraper.results)
        # Assert that the connection's commit method was called once
        mock_conn.commit.assert_called_once()
        # Assert that the connection's close method was called once
        mock_conn.close.assert_called_once()

    # Test case for the /data endpoint of the Flask app
    def test_get_data(self):
        # Create a test client for the Flask app
        tester = app.test_client(self)
        # Send a GET request to the /data endpoint
        response = tester.get('/data')
        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

    # Test case for the /data endpoint of the Flask app
    @patch('webscraper.sqlite3.connect')
    def test_add_data(self, mock_connect):
        # Create a test client for the Flask app
        tester = app.test_client(self)
        # Create a mock connection object
        mock_conn = MagicMock()
        # Set the return value of the sqlite3.connect mock to the mock connection object
        mock_connect.return_value = mock_conn

        # Send a POST request to the /data endpoint with JSON data
        response = tester.post('/data', json={'title': 'Test Title', 'url': 'https://example.com'})
        # Assert that the response status code is 201
        self.assertEqual(response.status_code, 201)
        # Assert that sqlite3.connect was called with 'scraper.db'
        mock_connect.assert_called_with('scraper.db')
        # Assert that the cursor's execute method was called once with the expected SQL query and data
        mock_conn.cursor().execute.assert_called_once_with('INSERT INTO data (title, url) VALUES (?, ?)', ('Test Title', 'https://example.com'))
        # Assert that the connection's commit method was called once
        mock_conn.commit.assert_called_once()
        # Assert that the connection's close method was called once
        mock_conn.close.assert_called_once()
        # Configure logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        # Database setup
        DATABASE = 'scraper.db'

        def init_db(database=DATABASE):
            conn = sqlite3.connect(database)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    url TEXT
                )
            ''')
            conn.commit()
            conn.close()

        # Web Scraper
        class WebScraper:
            def __init__(self, base_url, endpoints, database=DATABASE):
                self.base_url = base_url
                self.endpoints = endpoints
                self.lock = threading.Lock()
                self.results = []
                self.database = database

            async def fetch_page(self, session, url):
                async with session.get(url) as response:
                    return await response.text()

            async def scrape(self, endpoint):
                url = f"{self.base_url}/{endpoint}"
                async with aiohttp.ClientSession() as session:
                    content = await self.fetch_page(session, url)
                    soup = BeautifulSoup(content, 'html.parser')
                    titles = [tag.get_text() for tag in soup.find_all('h1')]
                    with self.lock:
                        for title in titles:
                            self.results.append((title, url))

            def run(self):
                loop = asyncio.get_event_loop()
                tasks = [self.scrape(endpoint) for endpoint in self.endpoints]
                loop.run_until_complete(asyncio.gather(*tasks))

            def save_to_db(self):
                conn = sqlite3.connect(self.database)
                cursor = conn.cursor()
                with self.lock:
                    cursor.executemany('INSERT INTO data (title, url) VALUES (?, ?)', self.results)
                conn.commit()
                conn.close()

        # REST API
        app = Flask(__name__)

        @app.route('/data', methods=['GET'])
        def get_data():
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM data')
            rows = cursor.fetchall()
            conn.close()
            return jsonify(rows)

        @app.route('/data', methods=['POST'])
        def add_data():
            title = request.json['title']
            url = request.json['url']
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO data (title, url) VALUES (?, ?)', (title, url))
            conn.commit()
            conn.close()
            return jsonify({'status': 'success'}), 201

        if __name__ == "__main__":
            init_db()
            
            # Example usage of the scraper
            base_url = "https://example.com"
            endpoints = ["page1", "page2", "page3"]
            scraper = WebScraper(base_url, endpoints)
            
            logging.info("Starting web scraping...")
            scraper.run()
            logging.info("Saving data to database...")
            scraper.save_to_db()
            logging.info("Data saved successfully.")
            
            # Start the REST API
            app.run(debug=True)
# Run the test cases
if __name__ == '__main__':
    unittest.main()