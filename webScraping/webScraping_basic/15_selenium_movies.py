import requests
from bs4 import BeautifulSoup

url = 'https://play.google.com/store/movies'
headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Accept-Language" : "ko-KR,ko"
}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

movies = soup.find_all('div', attrs = {'class' : 'ULeU3b neq64b'})
# print(movies)
print(len(movies))   # 0 출력
# Google movie 에서는 User Agent 에 따라 정보를 다르게 출력(default : 미국 접속)

# with open('webScraping/webScraping_basic/movie.html', 'w', encoding='utf8') as f:
#     # f.write(res.text)
#     f.write(soup.prettify())   # html 문서를 예쁘게 출력

# 동적 페이지 : 스크롤을 넘길 때 마다 로딩되어 아래에 데이터가 나타남
# 현재, 구글 무비에서는 화살표 버튼 클릭을 통해 다른 영화 정보 확인 가능하도록

for movie in movies:
#     title = movie.find('div', attrs= {'class' : 'hP61id'}).get_text()
    title = movie.find('div', attrs= {'class' : 'Epkrse'}).get_text()   # AttributeError: 'NoneType' object has no attribute 'get_text' -> 아마 뒤에 정보들이 끊기거나 null 값인 경우가 있는 것 같음
    print(title)