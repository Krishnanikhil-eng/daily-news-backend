import feedparser  # used to read RSS feeds

def fetch_rss():
    """
    Fetch news articles from RSS feed.
    Returns a list of entries (title, link, date).
    """

    # BBC Technology RSS feed (stable and reliable)
    rss_url = "https://feeds.bbci.co.uk/news/technology/rss.xml"

    # parse the RSS feed
    feed = feedparser.parse(rss_url)

    # return list of news entries
    return feed.entries
