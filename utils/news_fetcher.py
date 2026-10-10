import requests
from datetime import datetime

NEWS_API_KEY = "fc99d272b0914239aedec4177f9b84cc"

def get_bangalore_news():
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "Bangalore flood OR traffic OR rain OR protest",
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 10,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params)
    articles = response.json().get("articles", [])

    news_data = []
    for article in articles:
        text = article["title"] + " — " + article["description"] if article["description"] else article["title"]
        
        news_data.append({
            "source": "news",
            "text": text,
            "timestamp": article["publishedAt"],
            "image_url": article.get("urlToImage", ""),
            "article_url": article.get("url", "")
        })

    return news_data
