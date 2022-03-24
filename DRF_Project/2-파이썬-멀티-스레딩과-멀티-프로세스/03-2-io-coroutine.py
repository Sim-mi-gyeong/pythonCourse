import time
import os
import threading
import asyncio
import aiohttp


async def fetcher(session, url):
    print(
        f"{os.getpid()} process | {threading.get_ident()} url : {url}"
    )  # getpid() : 현재 프로세스 id , get_ident() :
    async with session.get(url) as response:
        return await response.text()


async def main():
    # urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 50
    urls = ["https://google.com", "https://apple.com"] * 50

    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print("걸린 시간 : ", end - start)  # 20.22초 -> 2.56초
