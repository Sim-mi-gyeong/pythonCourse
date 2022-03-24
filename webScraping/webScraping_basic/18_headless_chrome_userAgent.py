from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True
# headlessChrome 을 사용하기 위해 userAgent 를 바꿔줄 필요 있음
options.add_argument(
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
)

browser = webdriver.Chrome(executable_path="chromedriver", options=options)
browser.maximize_window()

# 페이지 이동
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser.get(url)

# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)
# AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/99.0.4844.51 Safari/537.36
detectedValue = browser.find_element(By.ID, "detected_value")
print(
    detectedValue.text
)  # Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/99.0.4844.51 Safari/537.36
browser.quit()
