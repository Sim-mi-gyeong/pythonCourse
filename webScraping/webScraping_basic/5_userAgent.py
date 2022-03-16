from email import header
import requests
url = requests.get("http://nadocoding.tistory.com") 
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
res = requests.get(url, headers=headers)
print(len(res.text))
print(res.text)

with open("webScraping/webScraping_basic/nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)