import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")   # 가져온 html 문서를 lxml parser 를 통해 soup 라는 객채로 만들기
# print(soup.title)
# print(soup.title.get_text())
print(soup.a)   # 첫 번째로 발견되는 a 태그 정보(element) 뿌려주기
print(soup.a.attrs)   # a element의(태그가 가지고 있는) 속성 정보 출력
print(soup.a["href"])   # a elemenet 의 href 속성 정보 출력

# attrs 에 해당하는 정보의 처음 정보 가져오기
# print(soup.find("a", attrs = {"class" : "Nbtn_upload"}))    # class = "Nbtn_upload" 인 a element 를 찾아줘
# print(soup.find(attrs = {"class" : "Nbtn_upload"}))   # class = "Nbtn_upload" 인 어떤 element 를 찾아줘

# rank1 = soup.find("div", attrs = {"class" : "col_inner"})
rank1 = soup.find("li", attrs = {"class" : "rank01"})
print(rank1.a)
print(rank1.a.get_text())
# print(rank1.next_sibling)   # 줄바꿈이 존재할 수 있음
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())
rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())
print(rank1.parent)   # ol 태그

# rank1 항목 기준으로, 다음 항목을 찾을 때 li 인 것만 찾음
rank2 = rank1.find_next_sibling("li")
print(rank2.a.get_text())

rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())

rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())

print(rank1.find_next_siblings("li"))   # rank1 기준으로 다음 형제들 모두 가져옴


webtoon = soup.find("a", text = "독립일기-시즌2 56화 야식 참기")
print(webtoon)