from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


import requests
from bs4 import BeautifulSoup

import time
import pyperclip
import pymongo

from openpyxl import Workbook
import datetime
import numpy as np
import pandas as pd


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )
    return browser


browser = set_chrome_driver()
# browser = webdriver.Chrome("./chromedriver")
browser.maximize_window()

url = "https://cafe.naver.com/joonggonara.cafe?iframe_url=/ArticleList.nhn%3Fsearch.clubid=10050146%26search.boardtype=L%26viewType=pc"
browser.get(url)
time.sleep(1)

# 로그인 페이지 이동
loginBtn = browser.find_element(By.ID, "gnb_login_button")
loginBtn.click()
time.sleep(1)

# 일회용 번호 클릭
loginOneBtn = browser.find_element(By.ID, "ones")
loginOneBtn.click()

oneNum = 19348438
inputNum = browser.find_element(By.ID, "disposable")
inputNum.click()
inputNum.send_keys(oneNum)
loginBtn = browser.find_element(By.ID, "otnlog.login")
loginBtn.click()
# browser.switch_to.frame("cafe_main")

# # ID, Password 입력할 곳을 찾고 입력(copy)

# inputId = browser.find_element(By.ID, "id")
# inputPw = browser.find_element(By.ID, "pw")
# # inputId = browser.find_element(By.ID, 'id_line')
# # inputPw = browser.find_element(By.ID, 'pw_line')

# # 입력된 값이 없는 상태로
# inputId.clear()
# inputPw.clear()

# myId = "alruddlwl"
# myPw = "seung1217!"

# # ID 입력
# inputId.click()
# inputId.send_keys(myId)
# # id, pw 값 secrets.json 으로 따로 빼기
# # pyperclip.copy(myId)
# # inputId.send_keys(Keys.CONTROL, 'v')
# time.sleep(1)

# # PW 입력
# inputPw.click()
# inputPw.send_keys(myPw)
# # pyperclip.copy('seung1217!')
# # inputPw.send_keys(Keys.CONTROL, 'v')
# time.sleep(1)

# # 로그인 버튼 클릭
# loginBtn = browser.find_element(By.ID, "log.login")
# loginBtn.click()

baseUrl = "https://cafe.naver.com/joonggonara"
junggonaraId = 10050146

# 카테고리 ID
mobilePhoneId = 339  # 휴대폰
tabletId = 749  # 태블릿
sideDeviceId = 427  # 주변기기/악세사리
laptopId = 334  # 노트북
desktopId = 382  # 데스크탑
monitorId = 383  # 모니터

menu = ["휴대폰", "태블릿", "주변기기/악세사리", "노트북", "데스크탑", "모니터"]
menuIds = [mobilePhoneId, tabletId, sideDeviceId, laptopId, desktopId, monitorId]

# 필요한 카테고리 열기
categoryListUrl = f"{baseUrl}?iframe_url=/ArticleList.nhn%3Fsearch.clubid={junggonaraId}%26search.menuid={mobilePhoneId}%26search.boardtype=L"

total_page = 1000

# 페이지 개수 나누기
total_next = total_page // 10
last_page = total_page - total_next * 10

# datetime
now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

# 엑셀 작성
wb = Workbook(write_only=True)
ws = wb.create_sheet(today)
ws.append(["사이트", "카테고리", "제목", "가격", "상품 상태", "작성 날짜", "상품 설명", "url", "거래 상태"])


def iframe():
    try:
        browser.switch_to.frame("cafe_main")
    except:
        pass


browser.get(categoryListUrl)
time.sleep(2)

browser.switch_to.frame("cafe_main")
# 카테고리 내 첫번째 게시물 클릭
articles = browser.find_elements(By.CSS_SELECTOR, "a.article")
articles[10].click()
# midUrl = "https://cafe.naver.com/joonggonara/907902283"
# browser.get(midUrl)
time.sleep(5)

# 다음글 표시가 없을 때까지 반복 - 50번마다 저장
i = 0
while True:
    # for _ in range(5):
    i += 1

    # soup = BeautifulSoup(browser.page_source, "lxml")
    # scraping()
    # 정보 추출
    # 공지 게시물과도 동일한 제공 정보
    # try:
    #     WebDriverWait(browser, 10).until(
    #         EC.presence_of_element_located(By.CSS_SELECTOR, "h3.title_text")
    #     )
    # except:
    #     break

    try:
        date = browser.find_element(By.CSS_SELECTOR, ".date").text
    except:
        date = None

    try:
        title = browser.find_element(By.CSS_SELECTOR, "h3.title_text").text.strip(" ")
    except:
        title = None

    try:
        url = browser.find_element(By.CSS_SELECTOR, ".button_url").get_attribute("href")
    except:
        url = None

    print("date : ", date)
    print("title : ", title)
    print("url : ", url)

    try:
        # 거래 상태
        tradeStatus = browser.find_element(By.CSS_SELECTOR, ".ProductName").find_element(
            By.TAG_NAME, "em"
        )
        # tradeStatus = soup.find_all(
        #     "em", attrs={"class": ["SaleLabel safety", "SaleLabel sold", "SaleLabel selling"]}
        # )
        if tradeStatus:
            # tradeStatus = tradeStatus[0].text
            tradeStatus = tradeStatus.text
        else:
            tradeStatus = None
    except:
        tradeStatus = None
        pass

    print("tradeStatus : ", tradeStatus)

    try:
        # 상품 가격
        priceStr = browser.find_element(By.CSS_SELECTOR, ".ProductPrice")
        #         if priceStr != None:
        if priceStr:
            priceStr = priceStr.text
            if priceStr:
                priceNumStr = priceStr[:-1]
                price = priceNumStr.replace(",", "")
                price = int(price)
                print("price : ", price)
            # else:
            #     # 제목에서 가격 문자열 추출 시도 한 번 더
            #     price = ""
        else:
            price = ""
    except:
        price = None
        pass

    print("price : ", price)

    try:
        # 상품 상태
        status = browser.find_element(By.CSS_SELECTOR, ".detail_list")
        if status:
            statusTitle = status.find_element(By.CSS_SELECTOR, ".list_title").text
            if statusTitle == "상품 상태":
                statusContent = status.find_element(By.CSS_SELECTOR, ".list_detail").text
                print("status : ", status)
                print("statusTitle : ", statusTitle)
                print("statusContent : ", statusContent)
            else:
                statusContent = ""

        else:
            statusContent = ""
    except:
        statusContent = None
        pass

    try:
        # 상품 설명
        explanation = browser.find_element(By.CSS_SELECTOR, ".se-main-container")
        if explanation:
            explanation = explanation.text
        else:
            explanation = ""
    except:
        explanation = None
        pass

    print("explanation : ", explanation)

    # 엑셀에 작성
    # ws.append(["사이트", "카테고리", "제목", "가격", "상품 상태", "작성 날짜", "상품 설명", "url", "거래 상태"])
    ws.append(["중고나라", "휴대폰", title, price, statusContent, date, explanation, url, tradeStatus])

    try:
        browser.find_element(By.LINK_TEXT, "다음글").click()
        # 기다리기
        time.sleep(5)

    except NoSuchElementException:  # 다음글 표시가 없는 경우 종료
        break
    except Exception as error:
        print(error)
        pass

    # if i % 50 == 0:
    #     wb.save(f"중고나라_{menu[0]}_2_{today}_게시물.xlsx")

# selenium 끝내고 엑셀 파일 저장
# browser.quit()
# wb.save(f"중고나라_{menu[0]}_2_{today}_게시물.xlsx")
wb.save(f"중고나라_{menu[0]}_9_{today}_게시물.xlsx")

# 7-8-(9) 합치기
