import requests
from bs4 import BeautifulSoup
quotes = []
for page in range(1,3):
    url = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    page_quotes = soup.find_all("span",class_="text")
    #列表推导式，for循环从page_quotes中取出q将其转化为text格式即q.text，然后extend逐个追加到空列表quotes中
    quotes.extend([q.text for q in page_quotes])

for i,quote in enumerate(quotes,1):
    print(f"引用{i}:{quote}")