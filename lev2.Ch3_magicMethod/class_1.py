# Chapter03-01
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드

# 기본형
print(int)  # 모든 데이터 타입은 클래스
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10

print(type(n), '\n')
print(n + 100)
print(n.__add__(100))
# print(n.__doc__)  Docstring을 출력하는 메소드
print(n.__bool__(), bool(n))  # 0이면 False
print(n * 100, n.__mul__(100))

print('\n\n')

# 클래스 예제 1
class Fruit():
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : {} , {}'.format(self._name, self._price)

    # class 기반 더하기 방식
    def __add__(self, x):
        print('called >> __add__')
        return self._price + x._price

    def __sub__(self, x):
        print('called >> __sub__')
        return self._price - x._price

    # 작거나 같다(<=, little of equal)
    def __le__(self, x): 
        print('called >> __le__')
        if self._price <= x._price:
            return True
        else:
            return False

    # 크거나 같다(>=, greater or equal)
    def __ge__(self, x):
        print('called >> __ge__')
        if self._price >= x._price:
            return True
        else:
            return False
        

# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

# 매직 메소드를 구현해 놓으니 내부적으로 더하기를 할 때 __add__ 메소드 호출
# s2가 x로 넘어감
print(s1 + s2) 
print(s1.__add__(s2))
print()

# 일반적인 계산
# print(s1._price + s2._price)

# 매직 메소드
print(s1 >= s2)
print(s1 <= s2)
print()
print(s1 - s2)
print(s2 - s1)
print()
print(s1)  # __str__ 메소드 출력
print(s2)
