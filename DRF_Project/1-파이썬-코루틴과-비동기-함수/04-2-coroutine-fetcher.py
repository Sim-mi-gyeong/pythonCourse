# https://docs.aiohttp.org/en/stable/
# pip install aiohttp~=3.7.3

import aiohttp
import time
import asyncio


async def fetcher(session, url):  # (열려있는 세션, url)
    async with session.get(url) as response:  # with 앞에 async 를 쓰려면, 해당하는 context 에서도 async 를 적용해야 함
        return await response.text()


async def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"]

    async with aiohttp.ClientSession() as session:
        # result = [fetcher(session, url) for url in urls] * 10
        # print(result)
        # result = await fetcher(session, urls[0])  # fetcher() 는 코루틴 함수이므로 await 객체
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print("걸린 시간 : ", end - start)  # 0.59초
