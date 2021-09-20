# Chapter05-01
# 일급 함수(일급 객체)
# 파이썬 함수의 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능(return)

# 5! = 5 * 4 * 3 * 2 * 1
# 함수 객체

def factorial(n):
    '''Factorial Function -> n : int'''

    if n == 1:
        return 1
    return n * factorial(n-1)

class A:
    pass

print(factorial(5))
print(factorial.__doc__)
# 함수의 type -> class -> 일급 객체이므로 객체로 취급
print('type of factorial(n) : ', type(factorial))
print('type of A : ', type(A))
# 함수지만 __repr__, __str__ 존재 -> 객체 취급
print(dir(factorial))
# 함수만 가지고 있는 속성 출력
print('클래스와 중복되지 않는 함수의 속성 : ', set(sorted(dir(factorial))) - set(sorted(dir(A))))
print('factorial.__name__ : ', factorial.__name__)
# 파일 위치 , 함수 정의한 위치(line)
print('factorial.__code__ : ', factorial.__code__)

print('\n\n')

# 변수 할당
var_func = factorial
print(var_func)
print('var_func(10) : ', var_func(10))
print('map -> range(1, 11) : ', list(map(var_func, range(1,11))))

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)
# map, filter, reduce

# 홀수인 경우
print(list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))   # 함수를 인수로 전달
print([var_func(i) for i in range(1, 6) if i % 2])

print('\n\n')

# reduce
from functools import reduce
from operator import add
print('reduce : ', reduce(add, [1,2,3,4,5,6,7,8,9,10]))
print(sum(range(1,11)))

# 익명함수(lambda)
# 가급적 주석 작성
# 가급적 함수 작성
# 일반 함수 형태로 리팩토링 권장

print(reduce(lambda x, t: x + t, range(1,11)))
print('\n\n')

# Callable : 호출 연산자 -> 메소드 형태로 호출이 가능한지 확인
# 호출 가능 확인 - __call__ attribution이 있으면 함수로 호출 가능
# str('a') : 가능, 3.14(3.14) : 불가능
print(callable(str), callable(A), callable(list), callable(var_func), callable(factorial), callable(3.14))

# partial 사용법 : 인수 고정 -> 콜백 함수 사용
from operator import mul
from functools import partial

print('mul(a,b) : ', mul(10,10))

# 인수 고정 ex) 5 * ? 상태
five = partial(mul, 5)
# 고정 추가
six = partial(five, 6)
print('pratial : ', five(10))
print(six())   # 호출만
print([five(i) for i in range(1,11)])

print(list(map(five, range(1,11))))
