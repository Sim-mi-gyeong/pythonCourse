# 하나의 document - python 에서 model

from odmantic import AIOEngine, Model


class BookModel(Model):
    keyword: str
    publisher: str
    price: int
    gaimageme: str

    class Config:
        collection = "books"  # collection Name 을 지정 가능


# MonboDB 는, DB > collection > document
# fastapi-pj > books > {keyword: ~, publisher: ~ }
