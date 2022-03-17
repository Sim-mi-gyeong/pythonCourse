# 동적 페이지 : 스크롤을 넘길 때 마다 로딩되어 아래에 데이터가 나타남
# 현재, 구글 무비에서는 화살표 버튼 클릭을 통해 다른 영화 정보 확인 가능하도록

from selenium import  webdriver
browser = webdriver.Chrome('./chromedriver')
browser.maximize_window()

# 페이지 이동
url = 'https://play.google.com/store/movies'
browser.get(url)

# 지정한 위치로 스크롤 내리기 -> 넘기기
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 2080)")

# 화면 가장 아래로 스크롤 내리기 -> 현재 문서의 총 높이만큼
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 높이가 변하지 않을 때까지
import time
interval = 2   # 2초에 한 번씩 스크롤 내림

# 현재 문서 높이를 가져와 저장
prevHeight = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내리기
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")    

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    currnetHeight = browser.execute_script("return document.body.scrollHeight")

    if currnetHeight == prevHeight:
        break

    prevHeight = currnetHeight

print('스크롤 완료')


import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, 'lxml')

movies = soup.find_all('div', attrs = {'class' : 'ULeU3b neq64b'})
# print(len(movies))

for movie in movies:
    title = movie.find('div', attrs= {'class' : 'Epkrse'})
    if title != None:
        title = title.get_text()
    else:
        continue

    # 할인 전 가격
    originPrice = movie.find('span', attrs={'class': 'SUZt4c P8AFK'})
    if originPrice:
        originPrice = originPrice.get_text()
    else:
        # print(title, ' < 할인되지 않은 영화 제외 > ')
        continue

    # 할인된 가격
    price = movie.find('span', attrs={'class': 'VfPpfd VixbEe'}).get_text()

    # 링크
    link = movie.find('a', attrs={'class':'Si6A0c ZD8Cqc'})['href']
    # 올바른 링크 : 'https://play.google.com + link
    print(f'제목 : {title}')
    print(f'할인 전 가격 : {originPrice}')
    print(f'할인 후 가격 : {price}')
    print('링크 : ', 'https://play.google.com' + link)
    print('-' * 100)

browser.quit()
# 다른 로직에 의해 페이지 로딩하는 경우 존재 class 다른 경우 존재
# movies = soup.find_all('div', attrs={'class' : [ 'ImZGtf mpg5gc', 'Vpfmgd' ]})