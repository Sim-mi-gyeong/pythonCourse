# Chapter02-02
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리 

class Car():
    """
    Car class
    Author: Sim
    Date: 2021.09.05
    """

    # 클래스 변수: 모든 인스턴스가 공유 -> 하나의 클래스에서 공통적으로 참조하는 변수 할당할 때
    car_count = 0

    def __init__(self, company, details):  # self는 클래스 인스턴스(자기자신, 객체의 인스턴스) - 객체 자기 자신을 참조하는 매개변수
        self._company = company  # 인스턴스 변수
        self.car_count = 10
        self._details = details
        Car.car_count += 1  # __init__() 메소드가 호출될 때마다 1씩 증가

    def __str__(self):  # 문자열로 사용자 입장의 출력을 할 때 인스턴스 메소드
                        # 사용자 레벨
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):  # 자료형의 타입에 따른 객체를 그대로 표시할 때 -> 위의 __str__() 메소드가 없을 때 repr 메소드 출력 
                         # 개발자 레벨
        return 'repr : {} - {}'.format(self._company, self._details)

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

# self 의미
car1 = Car('Ferrari', {'color' : 'White', 'forsepower' : 400, 'price' : 8000})
car2 = Car('BMW', {'color' : 'Black', 'forsepower' : 270, 'price' : 5000})
car3 = Car('Audi', {'color' : 'Silver', 'forsepower' : 300, 'price' : 6000})

# 인스턴스 메소드에서는 self가 첫 번째 매개변수로 넘어옴 

# ID 확인
print(id(car1))  # self가 있어야 자기 자신의 value
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)
print('\n\n')

# dir & __dict__ 확인

print(dir(car1))  # 해당 인스턴스가 가지고 있는 모든 매직 메소드를 리스트 형태로
print(dir(car2))

print('\n\n')

print(car1.__dict__)  # key와 value로 상세하게 값 표시
print(car2.__dict__)

print('\n\n')

# Doctring
print(Car.__doc__)
print('\n\n')

# 실행
car1.detail_info()
print()
car2.detail_info()

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__), id(car3.__class__))  # 메인 class의 id 값 출력

# 에러
# Car.detail_info()  # class 이름으로 접근 -> 인자가 자동으로 전달되지 않아 명시적으로 self 인자 전달
Car.detail_info(car1)
car1.detail_info()  # self를 전달하지 않아도 자동으로 매개변수 전달
print('\n\n')

# 공유 확인
print(car1.car_count)
print(car1.__dict__)  # car_count 값이 나오지 않음
print(dir(car1))  # car_count 값이 나옴
print('\n')

# 접근
print(car1.car_count)
print(Car.car_count)
print('\n')

del car2  # 인스턴스를 메모리에서 지움

# 삭제 확인
print(car1.car_count)
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색 -> # self.car_count = 10가 없으면 클래스 변수 찾음
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수) -> 만약, 그래도 없으면 error)

# 동일한 이름으로 인스턴스 변수를 만들면 접근 방법이 달라짐
# -> 인스턴스 변수(self)는 인스턴스 이름으로, 클래스 변수는 클래스 이름으로 접근
