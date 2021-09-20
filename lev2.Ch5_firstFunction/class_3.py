# Chapter05-03
# 일급 함수(일급 객체)
# 클로저 기초
# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(액세스) 가능

# Closure 사용
# 여러가지 변수를 담을 때에는 Class 형태가 더 좋음!
def closure_ex1():
    # Free Variance(사용하는 함수 바깥에서 선언)
    # 클로저 영역
    series = []
    # series 변수는 원래, 함수를 호출하면 함수 안에서 소멸됨
    # average 입장에서는 series에 접근 가능
    # 함수가 리턴되면 series 변수의 값을 함수가 계속 기억 변수의 생명 주기
    def average(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))

        return sum(series) / len(series)

    return average

avg_closure1 = closure_ex1()
print('avg_closure1 : ', avg_closure1)  # 함수가 리턴
print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))
print('\n\n')

# function inspection
print('dir(avg_closure1) : ', dir(avg_closure1), '\n')
print('dir(avg_closure1.__code__) : ', dir(avg_closure1.__code__), '\n')
print('자유 변수 : ', avg_closure1.__code__.co_freevars)
print('자유 변수의 값 : ', avg_closure1.__closure__[0].cell_contents)
print((avg_closure1.__closure__[0]))
print('\n\n')
 
# 잘못된 클로저 사용
def closure_ex2():
    # Free variance
    cnt = 0
    total = 0

    def average(v):
        # cnt += 1
        # total += v
        return total / cnt

    return average

avg_clouser2 = closure_ex2()
# local variable 'cnt' referenced before assignment
# average(v) 함수 내에서 closure_ex2() 함수의 cnt를 참조하지 못함. 
# print('avg_clouser2(10) : ', avg_clouser2(10))

def closure_ex3():
    # Free variance
    cnt = 0
    total = 0

    def average(v):
        # cnt와 total이 자유변수로 됨. -> 누적 가능
        # 함수 내에서 global을 쓰는 것은 좋지 못 함.
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt

    return average

avg_clouser3 = closure_ex3()
print('avg_clouser3(15) : ', avg_clouser3(15))
print('avg_clouser3(35) : ', avg_clouser3(35))
print('avg_clouser3(40) : ', avg_clouser3(40))
