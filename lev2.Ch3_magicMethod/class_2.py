# Chapter03-02
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드

# 클래스 예제 2
# 벡터(x,y)
# (5,2) + (4,3) = (9,5)
# (10,3) * 5 = (50,15)
# Max((5,10)) = 10

class Vector(object):
    # def __init__(self, x, y):
    def __init__(self, *args):  # unpacking
        """
        Create a vector, example : v = Vector(5, 10)
        """
        if len(args) == 0:  # 오류 방지
            self._x, self._y = 0, 0  # unpacking
        else:
            self._x, self._y = args

    def __repr__(self):
        ''' Return the vector informations.'''
        return 'Vector(%r, %r)'%(self._x, self._y)

    def __add__(self, other):
        ''' Return the vector addition of self and other '''
        # 새로운 클래스 인스턴스를 만들어서 반환하는 방법
        return Vector(self._x + other._x, self._y + other._y)

    # def __add__(self, other):
    #     return (self._x + other._x , self._y + other._y)

    def __mul__(self, y):
        # 여기서 y는 스칼라
        return Vector(self._x * y, self._y * y)

    # def __mul__(self, y):
    #     return (self._x * y , self._y * y) 

    def __bool__(self):
        return bool(max(self._x, self._y))  # max인 값이 0보다 크면 True를 반환
                                            # 좌표 평면 상에서 원점에 있는지를 확인하는 메서드 ex) (0,0)일 때 False

# print(Vector.__doc__)
print(Vector.__init__.__doc__)

# Vector 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()  # 생성자에 의해 (0,0)으로 초기화

# 매직메소드 출력
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

print(v1, v2, v3)
print("v1 + v2 = " , v1 + v2)
print("v1 * 3 = ", v1 * 3)
print("v2 * 10 = ", v2 * 10)
print(bool(v1) , bool(v2)) 
print(v1.__bool__(), v2.__bool__())
# print(v1.bool(), v2.bool())   # AttributeError: 'Vector' object has no attribute 'bool'
print(bool(v3))
