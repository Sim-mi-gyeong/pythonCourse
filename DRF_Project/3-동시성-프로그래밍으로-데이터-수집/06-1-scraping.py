import os
import aiohttp
import asyncio
from config import get_secret
import aiofiles

# pip install aiofiles==0.7.0


async def img_downloader(session, img):
    img_name = img.split("/")[-1]
    # img_name = img.split("/")[-1].split("?")[0]

    try:
        os.mkdir("./images")
    except FileExistsError:
        pass

    # 세션에 대해 img 도 open을 하면 해당 데이터가 들어옴 -> 이 데이터를 로컬에 저장
    async with session.get(img) as response:
        if response.status == 200:
            async with aiofiles.open(
                f"./images/{img_name}", mode="wb"
            ) as file:  # mode = "wb" : byte 를 write
                img_data = await response.read()  # 데이터를 읽고 -> 해당 데이터를 파일 형태로 쓰기
                await file.write(img_data)


async def fetch(session, url, i):
    print(i + 1)
    headers = {
        "X-Naver-Client-Id": get_secret("NAVER_API_ID"),
        "X-Naver-Client-Secret": get_secret("NAVER_API_SECRET"),
    }
    async with session.get(url, headers=headers) as response:
        result = await response.json()
        items = result["items"]
        images = [item["link"] for item in items]
        await asyncio.gather(*[img_downloader(session, img) for img in images])


async def main():
    BASE_URL = "https://openapi.naver.com/v1/search/image"
    keyword = "cat"
    urls = [f"{BASE_URL}?query={keyword}&display=20&start={1 + i*20}" for i in range(10)]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url, i) for i, url in enumerate(urls)])


if __name__ == "__main__":
    asyncio.run(main())
