# 한번 요청을 보내고 응답을 받으면 바로 끊기는 상태
# with 를 사용해 세션 유지 - 서버와 클라이언트 사이에 연결을 유지시켜주는 상태
# 세션을 열어주었으면 닫아야 함

# https://2.python-requests.org/en/master/user/advanced/#id1
# pip install requests

import requests  # 동기적 코드가 있는 패키지
import time


def fetcher(session, url):  # (열려있는 세션, url)
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"]

    """
    session = requests.Session()   # 세션 오픈

    session.get(url)

    session.close()   # 세션 close

    """

    # with requests.Session() as session:
    #     session.get(url)

    with requests.session() as session:
        result = [fetcher(session, url) for url in urls] * 10
        print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("걸린 시간 : ", end - start)
