import threading
import requests
from bs4 import BeautifulSoup
import sqlite3
from flask import Flask, jsonify, request
import logging
import asyncio
import aiohttp

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database setup
DATABASE = 'scraper.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
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
    def __init__(self, base_url, endpoints):
        self.base_url = base_url
        self.endpoints = endpoints
        self.lock = threading.Lock()
        self.results = []

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
        conn = sqlite3.connect(DATABASE)
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
