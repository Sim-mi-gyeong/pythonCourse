import requests
# res = requests.get("http://naver.com")
# # res = requests.get("http://nadocoding.tistory.com")   # 403 인 경우 접근 불가(스크래핑 불가)
# print('응답 코드 : ', res.status_code)   # 200 이면 정상


# if res.status_code == requests.codes.ok:
#     print('정상입니다.')
# else:
#     print('문제가 생겼습니다. [에러코드 ', res.status_code, "]")

# res.raise_for_status()   # 문제가 생긴 경우, 즉 에러코드가 403인 경우 오류를 출력하고 바로 종료
# print("웹 스크래핑을 진행합니다.")

# 정리 - 2줄로 끝내기
res = requests.get("http://google.com")
res.raise_for_status()

print(len(res.text))
print(res.text)

with open("webScraping/webScraping_basic/mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)