import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs = {"class" : re.compile("^search-product")})
# print(items[1].find("div", attrs = {"class" : "name"}).get_text())
for item in items:

    # 광고 제품은 제외
    ad_badge = item.find("span", attrs={"class" : "ad-badge-text"})
    if ad_badge:
        print(" < 광고 상품은 제외합니다. > ")
        continue  

    name = item.find("div", attrs={"class" : "name"}).get_text()   # 제품명

    # 애플 제품 제외
    if "Apple" in name:
        print(" < Apple 제품은 제외합니다. > ")
        continue

    price = item.find("strong", attrs={"class" : "price-value"}).get_text()   # 가격 

    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find("em", attrs={"class" : "rating"})  # 평점
    # 평점이 없는 상품에 대해 아래의 오류 발생 
    # AttributeError: 'NoneType' object has no attribute 'get_text'
    if rate:
        rate = rate.get_text()
    else:
        # rate = "평점 없음"
        print(" < 평점 없는 상품은 제외합니다. > ")
        continue

    rateCount = item.find("span", attrs={"class" : "rating-total-count"})   # 평점 수
    if rateCount:
        rateCount = rateCount.get_text()   # output : (26)
        rateCount = rateCount[1:-1]
        # print("리뷰 수 : ", rateCount)
    else:
        # rateCount = "평점 수 없음"
        print(" < 평점 수가 없는 상품은 제외합니다. > ")
        continue

    # 평점/평점 수 존재하는 경우의 처리
    if float(rate) >= 4.5 and int(rateCount) >= 100:
        print(name, price, rate, rateCount)
    