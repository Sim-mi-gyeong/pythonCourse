# for selenium -> chrome 버전에 일치하는 web driver 설치
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome("./chromedriver")   # "./chromedriver"   # 같은 경로에 있으면 webdriver.Chrom() 만으로 처리 가능
# chrome driver 객체를 생성하고 -> 해당 url로 이동
browser.get("http://naver.com")

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element(By.CLASS_NAME, "link_login")
elem.click()

# 3. id, pw 입력
browser.find_element(By.ID, "id").send_keys("naver_id")
browser.find_element(By.ID, "pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element(By.ID, "log.login").click()

time.sleep(3)

# 5. id 를 새로 입력
# browser.find_element(By.ID, "id").send_keys("my_id")
browser.find_element(By.ID, "id").clear()
browser.find_element(By.ID, "id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close()   # 현재 탭만 종료
browser.quit()   # 전체 브라우저 종료