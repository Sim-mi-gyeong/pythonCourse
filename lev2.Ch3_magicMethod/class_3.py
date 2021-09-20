# Chapter03-03
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드

# 객체 -> 파이썬의 데이터를 추상화
# (모든 객체 -> id), (type -> value)로 확인 가능

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

# 인덱스로 접근 가능
l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_leng1)

# 네임드 튜플 사용 -> 데이터 모델링
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')

# Point()라는 클래스인가? -> 알고보니, Point라는 namedtuple을 사용
# 튜플 성질도 보유 - 인덱스로 접근 가능, 딕셔너리 - 키('x', 'y')로 접근 가능
# 튜플 형태의 데이터가 어떤 것을 의미하고 있는지 한 눈에 볼 수 있음.
# 성능도 향상
pt3 = Point(1.0, 5.0)  
pt4 = Point(2.5, 1.5)

print(pt3, pt4)   # 튜플 형태로, 레이블된 상태
print(pt3[0])   # 인덱스로도 접근 가능
print(pt3.x)   # key로도 접근 가능

# 인덱스로 접근하는 것은 좋지 않음. -> key로도 접근 가능!
l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(l_leng2)


# 네임드 튜플 선언 방법
# typename = collections.namedtuple('typename', 'fidle_names')
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
# x: 중복, class: 예약어
Point4 = namedtuple('Point', 'x y x class', rename=True)  # Defalut = False

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}

# 출력
print(Point1, Point2, Point3, Point4)

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point(20, 40)
p3 = Point3(45, y=20)
# rename 테스트
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)  # namedtuple로 unpacking하여 x, y 찾아감

print('\n\n')
print(p1)
print(p2)
print(p3)
print(p4)   # x 키 값이 중복 -> _2라는 난수로 변수 생성(rename=True가 되었기때문)
print(p5)

# 사용
print(p1[0] + p2[1])
print(p1.x + p2.y)

# Unpacking
x, y = p2   # 묶여있던 것을 풀어 각각 x, y에 할당
print(x, y)
print(p2)
print('\n')

# 네임드 튜플 메소드
temp = [52, 38]
# _make() : 새로운 객체 생성(리스트를 네임드 튜플로 변환(캐스팅))
p4 = Point1._make(temp)
print(p4)

# _fields: 필드 네임 확인 -> 객체 안에 key가 어떤 것이 있는지를 나타냄
print(p1._fields, p2._fields, p3._fields, p4._fields)

# _asdict(): OrderedDict(정렬된 딕셔너리) 반환 (네임드 튜플을 -> 정렬된 딕셔너리로)
print(p1._asdict())   # OrderdDict([('x', 10), ('y', 35)])
print(p4._asdict())   # OrderdDict([('x', 52), ('y', 38)])


# 실 사용 실습
# 한 반에 20명, 4개의 반(A, B, C, D)

# 'rack': A, B, C, D / 'number': 1~20
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()
print(numbers)
print(ranks)

# list Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print("전체 학생 수 : ", len(students))
print("학급 별 학생 : ", students)   # 체계적으로 관리 가능

# 추천
students2 = [Classes(rank, number)   # A 나오고 20번 반복 -> B 나오고 20번 반복 ..
                for rank in 'A B C D'.split()
                    for number in [str(n)
                        for n in range(1,21)]] 

print("전체 학생 수 : ", len(students))
print("학급 별 학생 : ", students)

# 출력
for s in students:
    print(s)
