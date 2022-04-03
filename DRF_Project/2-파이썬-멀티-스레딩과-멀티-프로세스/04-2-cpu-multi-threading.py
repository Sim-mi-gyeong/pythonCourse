import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor


# nums = [50, 63, 32]
nums = [50] * 100


def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total += i * j * k  # cpu 연산만 필요
    return total


def main():
    executor = ThreadPoolExecutor(max_workers=10)
    results = list(executor.map(cpu_bound_func, nums))
    print(results)
    # for num in nums:
    #     cpu_bound_func(num)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("걸린 시간 : ", end - start)  # 0.0567초 -> 0.0328초 / 0.96초
