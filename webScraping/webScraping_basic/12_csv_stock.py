# https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=4
import csv
import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "webScraping/webScraping_basic/시가총액1-200.csv"
f = open(filename, "w", encoding="utf8", newline="")
# f = open(filename, "w", encoding="utf-8-sig", newline="")   # 한글 깨질 경우
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    data_rows = soup.find("table", attrs = {"class" : "type_2"}).find("tbody").find_all("tr")

    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:   # 의미 없는 데이터(Ex) 줄바꿈) Skip
            continue
        data = [column.get_text().strip() for column in columns]   # .strip() : 불필요한 공백(\n\n\t\t\t\t) 제거
        # print(data)
        writer.writerow(data)