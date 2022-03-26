from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent  # Path(__file__).resolve() : 현재 경로

app = FastAPI()  # 싱클톤 패턴의 app 생성

# app.mount("/static", StaticFiles(directory="static"), name="static")   # mount : 미들웨어, Staticfiles : CSS(웹 상에서 이미지 처리, 스타일 등 처리), js 파일 등

templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)  # "app/templates" 와 같은 경로를 절대 경로로 설정하고자 함


# response_class=HTMLResponse : HTML을 Serving -> templates 안에 TemplateResponse 클래스를 사용해 반환
# {id} : dynamic url - 해당 id 가 함수의 id 로 전달 -> 두번째 인자(Context)에 담아 item.html 의 id 에 들어감
# request: Request, id: str 의 순서는 무관
@app.get("/items/{id}", response_class=HTMLResponse)  # 요청을 받고 -> 해당하는 요청에 따라 응답, items/ 동적 라우트
async def read_item(request: Request, id: str):
    print("request : ", request)
    print("dir(request) : ", dir(request))
    print('request["headers"] : ', request["headers"])  # 요청 주체에 대한 header 종료
    return templates.TemplateResponse(
        "item.html", {"request": request, "id": id, "data": "hello fastapi"}
    )  # item.html 에 데이터를 보내기
