# from bs4 import BeautifulSoup
import aiohttp
import asyncio
from config import get_secret

# fetch 함수는 url에 있는 html 정보를 가져옴 - 동시에, 각 페이지에 대해 수행


async def fetch(session, url):
    headers = {
        "X-Naver-Client-Id": get_secret("NAVER_API_ID"),
        "X-Naver-Client-Secret": get_secret("NAVER_API_SECRET"),
    }
    async with session.get(url, headers=headers) as response:
        result = await response.json()
        items = result["items"]
        images = [item["link"] for item in items]
        print(images)
        # print(result)


async def main():
    BASE_URL = "https://openapi.naver.com/v1/search/image"
    keyword = "cat"
    urls = [f"{BASE_URL}?query={keyword}&display=20&start={1 + i*20}" for i in range(10)]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url) for url in urls])


if __name__ == "__main__":
    asyncio.run(main())
