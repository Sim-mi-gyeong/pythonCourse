import asyncio
import aiohttp

from app.config import get_secret

# from config import get_secret


class NaverBookScraper:

    NAVER_API_BOOK = "https://openapi.naver.com/v1/search/book"
    NAVER_API_ID = get_secret("NAVER_API_ID")
    NAVER_API_SECRET = get_secret("NAVER_API_SECRET")

    # Data 요청 함수 - apis에 있는 api 각각의 url에 동시성을 적용해 요청 전송
    @staticmethod
    async def fetch(session, url, headers):
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                result = await response.json()
                return result["items"]

    def unit_url(self, keyword, start):
        return {
            "url": f"{self.NAVER_API_BOOK}?query={keyword}&display=10&start={start}",
            "headers": {
                "X-NAVER-Client-Id": self.NAVER_API_ID,
                "X-NAVER-Client-Secret": self.NAVER_API_SECRET,
            },
        }

    # apis : 해당하는 api url 이 들어가 있음
    async def search(self, keyword, total_page):
        apis = [
            self.unit_url(keyword, 1 + i * 10) for i in range(total_page)
        ]  # pagenation :  1 + i * 10(한 페이지 당 보여주는 수 10)

        async with aiohttp.ClientSession() as session:
            all_data = await asyncio.gather(
                *[NaverBookScraper.fetch(session, api["url"], api["headers"]) for api in apis]
            )
            print(all_data)
            result = []
            for data in all_data:
                if data is not None:
                    for book in data:
                        result.append(book)

            return result

    # asyncio.run()는 awiatable 객체가 아닌, 실행을 하는 것 -> 코루틴 함수를 실행하는 것이므로 run() 함수는, async def 필요 X
    def run(self, keyword, total_page):
        return asyncio.run(self.search(keyword, total_page))


if __name__ == "__main__":
    scraper = NaverBookScraper()
    print(scraper.run("파이썬", 3))  # 각 페이지들은 하나의 리스트로 담김
    print("len(scraper.run('파이썬', 3)) : ", len(scraper.run("파이썬", 3)))


# [ [한 페이지에 데이터들 10개], [한 페이지에 데이터 10개], [한 페이지에 데이터 10개] ]

# [ 데이터 30개 ]
