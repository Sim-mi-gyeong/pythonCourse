from typing import Optional

from fastapi import FastAPI  # fastapi 라이브러이의 FastAPI 클래스 가져오기

app = FastAPI()  # 싱글톤 패턴 app 인스턴스


@app.get("/")
def read_root():
    print("hello world")
    return {"message": "Hello World"}


@app.get("/hello")
def read_fastapi_hello():
    print("hello world")
    return {"Hello": "Fastapi"}  # get 프로토콜을 서버로 보내면 -> 서버는 요청에 대한 응답을 return 으로


# http://127.0.0.1:8000/items/12345/abcdefg?q=hello
@app.get("/items/{item_id}/{xyz}")
def read_item(item_id: int, xyz: str, q: Optional[str] = None):
    return {"item_id": item_id, "q": q, "xyz": xyz}


# {item_id}, {xyz} : 동적 라우팅

# uvicorn 은 ASGI 구현체
# -> python 으로 작성된 코드를 ASGI 위에서 실행 가능하도록
