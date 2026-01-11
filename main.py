from src.rss_fetcher import fetch_rss
from src.scraper import get_article_text
from src.cleaner import clean_text
from src.summarizer import ai_summary
from src.database import init_db, save_news

def run_pipeline():
    # initialize database
    init_db()

    # fetch news from RSS
    articles = fetch_rss()

    # process limited articles (for safety)
    for entry in articles[:5]:
        try:
            # extract article content
            raw_text = get_article_text(entry.link)

            # clean the article text
            clean_article = clean_text(raw_text)

            # generate normal summary (no AI)
            summary = ai_summary(clean_article)

            # save to database
            save_news(entry.title, entry.link, summary)

            print("Saved:", entry.title)

        except Exception as e:
            print("Skipped article due to error")

if __name__ == "__main__":
    run_pipeline()
