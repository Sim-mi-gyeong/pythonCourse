from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

# from motor.motor_asyncio import AsyncIOMotorClient
# from odmantic import AIOEngine

# from config import MONGO_DB_NAME, MONGO_URL
from app.models import mongodb
from app.models.book import BookModel

BASE_DIR = Path(__file__).resolve().parent  # Path(__file__).resolve() : 현재 경로

app = FastAPI()  # 싱클톤 패턴의 app 생성

# app.mount("/static", StaticFiles(directory="static"), name="static")   # mount : 미들웨어, Staticfiles : CSS(웹 상에서 이미지 처리, 스타일 등 처리), js 파일 등

templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    book = BookModel(keyword="파이썬", publisher="BJPublic", price=1200, image="me.png", hhh="abcdefg")
    print(
        await mongodb.engine.save(book)
    )  # save() 함수는 async(코루틴) 함수 = book : 비동기적으로 동작 -> DB 저장(새로고침을 하면,)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "콜렉터 북북이"},
    )


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    print("q : ", q)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "콜렉터 북북이", "keyword": q},
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
