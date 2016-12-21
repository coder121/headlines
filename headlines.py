import feedparser
from flask import Flask

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640',
             'indiatoday':'http://indiatoday.intoday.in/rss/article.jsp?sid=150'}


@app.route("/")
@app.route("/<publication>")
def get_news(publication="indiatoday"):
  return get_news(publication)



def get_news(publication):
  feed = feedparser.parse(RSS_FEEDS[publication])
  articles="""<html>
    <body><h1>Headlines</h1>"""
  first_article = feed['entries'][0]
  all_articles=feed['entries']
  for article in all_articles:
    articles+="""
       <h2>{0}</h2> </ br>
        <i>{1}</i> </ br>
        <p>{2}</p> </ br>
    </br> </br></br>""".encode('utf-8').format(article.get("title"), article.get("published"), article.get("summary"))
  
  articles+="""</body>
            </html>"""
  return articles 

if __name__ == "__main__":
  app.run(port=5000, debug=True)
