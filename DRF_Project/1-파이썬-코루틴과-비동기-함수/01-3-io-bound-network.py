import requests


def io_bound_func():
    result = requests.get("https://google.com")
    return result


if __name__ == "__main__":
    for i in range(10):
        result = io_bound_func()  # 각 io_bound_func() 실행이 10번 쌓여 시간이 걸림 - 요청을 보내고 응답까지 기달는 시간 누적
    print(result)
