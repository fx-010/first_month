import requests
from bs4 import BeautifulSoup

def fetch_quotes():

    try:
        url = f"http://quotes.toscrape.com/page/1/"
        response = requests.get(url,timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text,"html.parser")
        quotes = [q.text for q in soup.find_all("span",class_="text")]
        return quotes
    except requests.RequestException as e:
        print(f"爬取失败{e}")
        return[]
    
quotes = fetch_quotes()
print(f"抓取了{len(quotes)}条语句",quotes)