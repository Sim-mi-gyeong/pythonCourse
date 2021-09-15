# Chapter05-04
# 일급 함수(일급 객체)
# 클로저 기초
# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(액세스) 가능

# 데코레이터(Decorator)
# 장점
# 1. 중복 제거, 코드 간결, 공통 함수 작성
# 2. 로깅, 프레임워크, 유효성 체크 -> 공통 기능
# 3. 조합해서 사용 용이

# 단점
# 1. 가독성 감소
# 2. 특정 기능에 한정된 함수는 -> 단일 함수로 작성하는 것이 유리
# 3. 디버깅 불편

# 데코레이터 실습
import time

# 서로 다른 함수가 여러 개 있어도, 데코레이터를 하나만 정의하면 모든 함수를 실행시간 뽑아낼 수 있음.
def perf_clock(func):
    def perf_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()
        # 함수 실행
        # 부모에서 넘어온 func이 아래에서 실행 -> 실행되는 함수가 바뀌더라도 자유변수로 가질 수 있음
        # *args는 내부에서 packing해서 받고
        result = func(*args)

        # 함수 종료 시간
        et = time.perf_counter() - st
        # 실행 함수명
        name = func.__name__
        # 함수 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결과 출력
        print('[%0.5fs] %s(%s) -> %r ' % (et, name, arg_str, result))
        return result
    return perf_clocked

@perf_clock
# 데코레이터 사용시 time_func() 함수가 호출되기 전 perf_clock() 함수가 실행되면서
# 바깥에서 내부 함수를 받아 -> 내부 함수에서 인자로 받아 -> 데코레이터 실행되는 과정 
def time_func(seconds):
    time.sleep(seconds)

@perf_clock
def sum_func(*numbers):
    return sum(numbers)

# 데코레이터 미사용
# 외부(바깥)의 함수를 실행해야 안의 함수 리턴 가능
none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)

print('none_deco1 : ', none_deco1, none_deco1.__code__.co_freevars)
print('none_deco2 : ', none_deco2, none_deco2.__code__.co_freevars)

print('-' * 40, 'Called None Decorator -> time_finc')
print()
none_deco1(1.5)
print('-' * 40, 'Called None Decorator -> sum_finc')
print()
none_deco2(100, 200, 300, 400, 500)

print('\n\n')
print('--- 데코레이터 사용 ---')
# 데코레이터 사용
print('-' * 40, 'Called Decorator -> time_finc')
print()
time_func(1.5)
print('-' * 40, 'Called Decorator -> sum_finc')
print()
sum_func(100, 200, 300, 400, 500)
