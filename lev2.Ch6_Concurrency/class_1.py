# Chapter06-01
# 병행성(Concurrency)
# 이터레이터, 제너레이터
# Iterator(반복 가능한 객체), Generator(Iterator를 리턴하는 함수)

# 파이썬 반복 가능한 타입
# collections, text file, list, Dict, Set, Tuple, unpacking, *args... : iterable

# 반복 가능한 이유? -> iter(x) 함수 호출
t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('dir(t) : ', dir(t))   # __iter__ : 반복 가능
for c in t:   # 내부적으로는, t가 __iter__() 함수를 호출해서 next를 통해 하나하나 나온 것
    print('>> ', c)

# while
w = iter(t)
# print('dir(w) : ', dir(w))

# print('next(w) 1 : ', next(w))   # 다음에 나올 순서를 기억
# print('next(w) 2 : ', next(w))
# print('next(w) 3 : ', next(w))
# print('next(w) 4 : ', next(w))
# print('next(w) 5 : ', next(w))
# print('\n\n')

while True:
    try:
        print(next(w))
    except StopIteration:
        break

print()

# 반복형 확인
from collections import abc   # abstractmethod

# print(dir(t))
print(hasattr(t, '__iter__'))   # true를 반환하면 __iter__를 가지고 있음.
print(isinstance(t, abc.Iterable))   # 상속을 받았는지 확인 : t가 abc 클래스의 Iterable 인스턴스와 같은지 ? 
print('\n\n')

# next 패턴
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')   # text를 받아 공백을 기준으로 initializing

    def __next__(self):   # 매직메소드로 next() 함수 구현
        # print('Called __next__')
        try:
            word = self._text[self._idx]   # text의 현재 인덱스 값을 반환
        except IndexError:
            raise StopIteration('Stopped Iteration.')

        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wi = WordSplitter('Do today what you could do tommorow')
print("WordSplitter('Do today what you could do tommorow') : ", wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))

print('\n\n') 

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 후 메모리 사용량 증가 -> 제너레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(Coroutine), 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            # 제너레이터 -> 인덱스를 사용하지 않아도 내부적으로 다음에 반환할 위치 정보의 값을 기억함.
            yield word   

    def __repr__(self):
        return 'WordSplitGenerator(%s)' % (self._text)

wg = WordSplitGenerator('Do today what you could do tommorow')
wt = iter(wg)
print('wt : ', wt, '\n', 'wg : ', wg)

print('next(wt) 1 : ', next(wt))
print('next(wt) 2 : ', next(wt))
print('next(wt) 3 : ', next(wt))
print('next(wt) 4 : ', next(wt))
print('next(wt) 5 : ', next(wt))
print('next(wt) 6 : ', next(wt))
print('next(wt) 7 : ', next(wt))
# print('next(wt) 8 : ', next(wt))
