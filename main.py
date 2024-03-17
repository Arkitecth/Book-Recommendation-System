import requests
from bs4 import BeautifulSoup
import urllib.parse
trending_books_url = "https://www.goodreads.com/shelf/show/trending"

r = requests.get(trending_books_url)

soup = BeautifulSoup(r.content, 'html.parser')
trending_books = soup.select(".leftContainer .left .bookTitle")
for book in trending_books:
    print(book.text)

urllib.parse.quote_plus("foo://bar_baz")
