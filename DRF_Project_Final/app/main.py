from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.book_scraper import NaverBookScraper

# from motor.motor_asyncio import AsyncIOMotorClient
# from odmantic import AIOEngine

from app.models import mongodb
from app.models.book import BookModel

BASE_DIR = Path(__file__).resolve().parent  # Path(__file__).resolve() : 현재 경로

app = FastAPI()  # 싱클톤 패턴의 app 생성

# app.mount("/static", StaticFiles(directory="static"), name="static")   # mount : 미들웨어, Staticfiles : CSS(웹 상에서 이미지 처리, 스타일 등 처리), js 파일 등

templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    # book = BookModel(keyword="파이썬", publisher="BJPublic", price=1200, image="me.png", hhh="abcdefg")
    # print(
    #     await mongodb.engine.save(book)
    # )  # save() 함수는 async(코루틴) 함수 = book : 비동기적으로 동작 -> DB 저장(새로고침을 하면,)

    return templates.TemplateResponse(
        "./index.html",
        {"request": request, "title": "콜렉터 북북이"},
    )


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    # 1. 쿼리에서 검색어 추출
    keyword = q
    # (예외 처리)
    # - 검색어가 없다면, 사용자에게 검색을 요구 return
    if not keyword:
        context = {"request": request, "title": "콜렉터 북북이"}
        return templates.TemplateResponse(
            "./index.html",
            context,
        )
    # - 해당 검색어에 대해 수집된 데이터가 이미 DB에 존재한다면, 해당 데이터를 사용자에게 보여준다 return
    # await mongodb.engine.find_one(모델, 조건)
    if await mongodb.engine.find_one(BookModel, BookModel.keyword == keyword):
        books = await mongodb.engine.find(BookModel, BookModel.keyword == keyword)
        return templates.TemplateResponse(
            "./index.html",
            {"request": request, "title": "콜렉터 북북이", "books": books},
        )
    # 2. 데이터 수집기로 해당 검색어에 대해 데이터를 수집한다.
    naver_book_scraper = NaverBookScraper()
    # search 가 비동기 함수이므로
    books = await naver_book_scraper.search(keyword, 10)
    book_models = []
    for book in books:
        # book_model = BookModel(keyword=keyword, publisher="BJPublic", price=1200, image="me.png")
        book_model = BookModel(
            keyword=keyword,
            publisher=book["publisher"],
            price=book["price"],
            image=book["image"],
        )
        print(book_model)
        book_models.append(book_model)
        # save : async -> awaitable 객체 => 저장할 때까지 하나 기다리고, 하나 기다리고 하는 방식으로 진행
        # await mongodb.engine.save(
        #     book_model
        # )
    # 각각은 비동기 함수지만, 하나하나 동기적으로 진행
    # await mongodb.engine.save(book_model1)
    # await mongodb.engine.save(book_model2)
    # await mongodb.engine.save(book_model3)
    # asyncio.gather() 로 동시성 프로그래밍으로 진행 가능 => mongodb engine 안에 대신해주는 메서드 save_all() 존재

    # 3. DB에 수집된 데이터를 저장한다.
    await mongodb.engine.save_all(book_models)
    # - 수집된 각각의 데이터에 대해서 DB에 들어갈 모델, 인스턴스를 찍는다.
    # - 각 모델 인스턴스를 DB에 저장한다.

    return templates.TemplateResponse(
        "./index.html",
        # {"request": request, "title": "콜렉터 북북이", "keyword": q},
        {"request": request, "title": "콜렉터 북북이", "books": books},
    )


# Fastapi 에 이벤트 등록 가능 - fastapi server가 처음 구동될 때의 코드 작성 가능
@app.on_event("startup")
def on_app_start():
    print("hello server")
    """before app starts"""
    mongodb.connect()
    # client = AsyncIOMotorClient(MONGO_URL)
    # engine = AIOEngine(motor_client=client, database=MONGO_DB_NAME)


@app.on_event("shutdown")
def on_app_shutdown():
    print("bye server")
    """after app shutdown"""
    mongodb.close()
