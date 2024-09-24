import feedparser

def print_feed_entries(feed_url):
    feed = feedparser.parse(feed_url)

    for entry in feed.entries:
        title = entry.title if 'title' in entry else 'No title'
        link = entry.link if 'link' in entry else 'No link'
        summary = entry.summary if 'summary' in entry else 'No summary'

        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Summary: {summary}")
        print()

# Yahoo Finance RSS feed URL
rss_url = 'https://finance.yahoo.com/rss/'
print_feed_entries(rss_url)
