import time
import asyncio


async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료 !")
    await asyncio.sleep(mealtime)  # 탈출 및 진입(배달 완료(탈출) -> 식사 완료(진입))
    print(f"{name} 식사 완료, {mealtime} 시간 소요 ... ")
    print(f"{name} 수거 완료")
    return mealtime


async def main():
    result = await asyncio.gather(
        delivery("A", 5),  # 각 결과값 mealtime 이 result의 1, 2, 3번째 인자로 들어감
        delivery("B", 3),
        delivery("C", 4),
        # return (None)
    )

    """
    Sync 코드와 동일(동기적으로 진행, 비동기 함수도 동기적으로 처리)
    await delivery("A", 5)
    await delivery("B", 3)
    await delivery("C", 4)
    """

    """
    위의 코드와 동일 - 태스크(예약) 객체
    task1 = asyncio.create_task(delivery("A", 2))
    task2 = asyncio.create_task(delivery("B", 1))

    await task1
    await task2
    """

    print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    # print(main())   # None
    end = time.time()
    print("걸린 시간 : ", end - start)
