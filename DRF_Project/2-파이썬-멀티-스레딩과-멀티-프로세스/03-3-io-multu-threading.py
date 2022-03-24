import requests
import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor


def fetcher(params):
    print(params)
    session = params[0]
    url = params[1]
    print(
        f"{os.getpid()} process | {threading.get_ident()} url : {url}"
    )  # getpid() : 현재 프로세스 id , get_ident() :
    with session.get(url) as response:
        return response.text


def main():
    # urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 50
    urls = ["https://google.com", "https://apple.com"] * 50

    executor = ThreadPoolExecutor(max_workers=10)  # max_workers=1 : 스레드를 사용할 개수

    with requests.session() as session:
        # result = [fetcher(session, url) for url in urls]
        # print(result)
        params = [(session, url) for url in urls]
        list(executor.map(fetcher, params))  # (실행하고자 하는 fetch 함수, params) : params는 각 파라미터에 대한 리스트
        # map() 메서드를 통해 session 과 url 이 전달됨 - 제너레이터 객체 -> 리스트 객체로 변환


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("걸린 시간 : ", end - start)  # 스레드 1개 -> 36초 - 스레드를 만드는데에 연산이 추가되어, 같은 싱글 스레드라도 시간이 오래 소요
    # 스레드 10개 -> 4.73초
