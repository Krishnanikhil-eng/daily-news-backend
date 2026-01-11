import requests                 # to download the webpage
from bs4 import BeautifulSoup   # to extract text from HTML

def get_article_text(url):
    """
    Takes an article URL and returns the extracted text.
    """

    # download the webpage
    response = requests.get(url, timeout=10)

    # parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # find all paragraph tags
    paragraphs = soup.find_all("p")

    # combine paragraph text into one string
    text = " ".join(p.get_text() for p in paragraphs)

    return text
