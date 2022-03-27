# uvicorn app.main:app --reload

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="localhost", port=8000, reload=True)
    # 실제 Product 환경에서 reload=True X
    # uvicorn.run("app.main:app", host="localhost", port=8000)
