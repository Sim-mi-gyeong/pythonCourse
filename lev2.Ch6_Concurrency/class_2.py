# Chapter06-02
# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 
# -> 단일 프로그램 안에서 여러 일을 쉽게 수행
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행
# -> 속도, 분업화
 
def generator_ex1():
    print('Start')
    yield 'A Point'   # A Point까지 가서 멈춤 -> 중단점을 지정해 위치 기억
    print('Continue')
    yield 'B Point'   # yield => return의 역할!!(다음 키워드가 나올때까지 출력하고 멈춤) -> B Point 출력하고 멈춰
    print('End')

temp = iter(generator_ex1()) 
# print(temp)
print('A Point : ', next(temp))
print('B Point : ', next(temp))
# print('End : ', next(temp))

for v in generator_ex1():
    pass
    # print(v)   # 알아서 예외처리까지 
print('----------------------')
# Generator Ex2
temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())

# print('temp2 : ', temp2)
# print('temp3 : ', temp3)

# for i in temp2:
#     print(i)
# Start
# Continue
# End
# A PointA PointA Point
# B PointB PointB Point

for i in temp3:
    print(i)   
# Start
# A PointA PointA Point
# Continue
# B PointB PointB Point
# End

print('\n\n')
print('----------------------')

# Gnerator Ex3 (중요 함수)
# count, takewhile, filterfalse, accumulate, chain, product, groupby...

import itertools

gen1 = itertools.count(1, 2.5)

print('Gnerator Ex3 (중요 함수)')
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
# ... 무한
# 무한대로 증가하는 수 생성
# while True:
#     print(next(gen1))

# 조건
gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))

for v in gen2:
    pass
    # print(v)

print('\n\n')

# 필터 반대
print('filter 반대')
gen3 = itertools.filterfalse(lambda n : n < 3, [1, 2, 3, 4, 5])

for v in gen3:
    print(v)

print('\n\n')

# 누적 합계
print('누적 합계')
gen4 = itertools.accumulate([x for x in range(1, 101)])
for v in gen4:
    print(v)
print('\n\n')

# 연결1
# chaining : 앞의 것과 뒤에 것(서로 다른 iterable한 것)을 묶어 하나의 리스트로 만들기
print('연결 1')
gen5 = itertools.chain('ABCDE', range(1, 11, 2))
print('list(gen5) : ', list(gen5))
print('\n')

# 연결2
# 개수만큼 인덱스를 붙여 튜플형 리스트로 반환
print('연결 2')
gen6 = itertools.chain(enumerate('ABCDE'))
print('list(gen6) : ', list(gen6))
# for i in enumerate('ABCDE'):
#     print(i) 
print('\n')

# 개별 1
# 개별로 분리해 튜플로 반환
print('개별 튜플 분리')
gen7 = itertools.product('ABCDE')
print(list(gen7))
print('\n')

# 연산(경우의 수)
# 모든 순서쌍의 경우의 수를 따짐
print('연산(경우의 수)')
gen8 = itertools.product('ABCDE', repeat=2)
print(list(gen8))

# 그룹화
gen9 = itertools.groupby('AAABBCCCCDDEEE')
# print(list(gen9)) 

for chr, group in gen9:
    print(chr, ' : ', list(group))  
