# Chapter05-02
# 일급 함수(일급 객체)
# 클로저 기초
# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(액세스) 가능

# 파이썬 변수 범위(scope)

# Ex1
def func_v1(a):
    print(a)
    print(b)
# func_v1(10)

# Ex2
b = 20
def func_v2(a):
    print(a)
    print(b)
func_v2(10)

# Ex3
c = 30
def func_v3(a):
    global c
    print(a)
    print(c)  # local variable 'c' referenced before assignment : 안에 같은 변수가 있으면 로컬 변수 실행!
    c = 40   # global c의 값 변경

print('c >> ', c)
func_v3(10)
print('c >> ', c)
print('\n\n')

print('---- Closure ----')
# Closure(클로저) 샤용 이유
# 자유 영역 안에 있는 값(상태)을 기억
# 서버 프로그래밍 -> 동시성(Concurrency) 제어 -> 메모리 공간에 여러 자원이 접근 -> 교착상채(Dead Lock)
# 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 -> Erlang
# 클로저는 공유하되, 변경되지 않는(Immutable, Read Only) 적극
# 클로저는 불변자료구조 및 atom, STM -> 멀티스레드(Coroutine : 단일 스레드 환경에서도 멀티 스레드인 것 처럼) 프로그래밍에 강점

a = 100
print(a + 100)
print(a + 1000)
# 결과 누적(함수 사용)
print(sum(range(1,51)))
print(sum(range(51,101)))

# 클래스 이용
class Averager():
    # 초기화 메서드
    def __init__(self):
        self._series = []

    # Callable() 메서드를 구현하고 있으면 클래스를 함수처럼 호출 가능
    def __call__(self, v):
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

# 인스턴스 생성
average_cls = Averager()

# print('dir(average_cls) : ', dir(average_cls))   # __call__() 함수로서 호출 가능 확인

# 누적
print(average_cls(10))
print(average_cls(30))
print(average_cls(50))
print(average_cls(193))
