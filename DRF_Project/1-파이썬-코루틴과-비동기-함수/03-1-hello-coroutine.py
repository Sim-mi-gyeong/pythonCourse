# 코루틴 hello world!

import asyncio


async def hello_world():
    # awaitable 객체에만 사용 가능 Ex) 코루틴, 태스크(예약), 퓨처
    # await print("hello world")
    print("hello world")
    return 123


if __name__ == "__main__":
    # await는 async 키워드 안에서 사용되어야 함  ->  SyntaxError: 'await' outside function
    # -> asyncio 패키지로 해결
    # await hello_world()
    asyncio.run(hello_world())
