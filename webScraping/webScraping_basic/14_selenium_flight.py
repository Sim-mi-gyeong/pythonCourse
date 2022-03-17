from typing import final
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

s = Service('./chromedriver')
browser = webdriver.Chrome(service=s)
browser.maximize_window()   # 창 최대화

url = 'https://m-flight.naver.com/'
browser.get(url)   # url 로 이동

# 가는 날 클릭
# 아래와 같이 class name 으로 가는 날을 선택하려는 경우, 오는 날의 버튼 class name 과 동일해 실행 X
# browser.find_element(By.CLASS_NAME,'tabContent_option__2y4c6 select_Date__1aF7Y').click()
# XPAHT 사용
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()

# Click button by text
# 방법 1) text()
# browser.find_element(By.XPATH, "//button[text()='가는 날']").click()
# 방법 2) contains()
# browser.find_element(By.XPATH, "//button[contains(., '가는 날')]").click()

# 이번 달(3월) 27일, 28일 선택
time.sleep(1)
# browser.find_elements(By.XPATH, "//button[contains(., '27')]")[0].send_keys(Keys.ENTER)   # [0] -> 이번 달 달력에서 선택
# # browser.find_elements(By.XPATH, "//button[text() = '27']")[0].send_keys(Keys.ENTER)   # IndexError: list index out of range -> elements 리스트가 빈 것으로 출력
# browser.find_elements(By.XPATH, "//button[contains(., '28')]")[0].send_keys(Keys.ENTER)   # [0] -> 이번 달 달력에서 선택

browser.find_elements(By.XPATH, "//button[contains(., '27')]")[0].send_keys(Keys.ENTER)   # [1] -> 다음 달 달력에서 선택
browser.find_elements(By.XPATH, "//button[contains(., '29')]")[1].send_keys(Keys.ENTER)   # [1] -> 다음 달 달력에서 선택

time.sleep(1)

# 목적지 선택
browser.find_element(By.XPATH, "//button[contains(., '도착')]").send_keys(Keys.ENTER)
# 국내 클릭
browser.find_element(By.XPATH, "//button[contains(., '국내')]").send_keys(Keys.ENTER)
# 서울, 대한민국 클릭
browser.find_element(By.XPATH, "//button[contains(., '서울')]").send_keys(Keys.ENTER)

time.sleep(1)

# 항공권 검색 선택 - 도착지 선택하지 않고 아래 실행 시 '출발지와 도착지를 모두 입력해 주세요'
browser.find_element(By.XPATH, "//button[contains(., '항공권 검색')]").send_keys(Keys.ENTER)

# 최대 10초까지를 기다리는데, 해당하는 element가 나올 때까지, 10초 초과 시 Error
# XPATH, ID, CLASS_NAME, LINK_TEXT 등 사용 가능
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div[2]/div[2]')))
    # 성공했을 때 동작 수행
    print(elem.text)   # 첫 번째 결과 출력
    # elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div[2]/div[2]/div/button').send_keys(Keys.ENTER)
finally:
    browser.quit()