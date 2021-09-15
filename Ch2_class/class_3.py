# Chapter02-03
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리 

class Car():
    """
    Car class
    Author: Sim
    Date: 2021.09.05
    Description: Class, static, Instance Method
    """

    # 클래스 변수: 모든 인스턴스가 공유 -> 하나의 클래스에서 공통적으로 참조하는 변수 할당할 때
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company  # 인스턴스 변수
        # self.car_count = 10
        self._details = details
        

    def __str__(self):  # 문자열로 사용자 입장의 출력을 할 때 인스턴스 메소드
                        # 사용자 레벨
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):  # 자료형의 타입에 따른 객체를 그대로 표시할 때 -> 위의 __str__() 메소드가 없을 때 repr 메소드 출력 
                         # 개발자 레벨
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method(self가 들어가 있으면 인스턴스 메소드)
    # self: 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    # Instance Method (어떤 차의 가격을 반환하는지를 써야하기 때문에 인스턴스 메서드)
    # Instance Method의 첫번째 인자는 self를 받음
    def get_price(self):
        return 'Before Car Price -> company : {}, prince : {}'.format(self._company, self._details.get('price'))
    
    # Instance Method
    def get_price_culc(self):
        return 'Before Car Price -> company : {}, prince : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class Method(클래스 변수를 수정하거나 접근)
    # Class Method는 첫번째 인자로 cls(class)를 받음
    @classmethod #(데코레이터)
    def raise_price(cls, per):
        # cls.price_per_raise
        if per <= 1:
            print('Please Enter 1 Or More')
            return
        cls.price_per_raise = per
        print('Succeed! price increased')

    # Static Method
    # class와 관련된 역할 수행하지만 self 인자를 받을 필요가 없을 때 
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'BMW':
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry. This car is not Bmw'

    # def is_bmw(self):
    #     if self._company == 'BMW':
    #         return 'OK! This car is {}'.format(self._company)
    #     return 'Sorry. This car is not Bmw'



# self 의미
car1 = Car('Ferrari', {'color' : 'White', 'forsepower' : 400, 'price' : 8000})
car2 = Car('BMW', {'color' : 'Black', 'forsepower' : 270, 'price' : 5000})

# 전체 정보
car1.detail_info()
car2.detail_info()

# 가격 정보(직접 접근)
# 직접 인스턴스 변수에 접근하는 것은 좋지 않음 -> 메서드를 만들어서 접근
print(car1._details.get('price'))
print(car2._details['price'])

# 가격정보(인스턴스 메서드 - 인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격 인상(클래스 메서드 미사용) -> 직접 접근해서 수정하는 것은 좋지 않음!
Car.price_per_raise = 1.4

# 가격정보(인스턴스 메서드 - 인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 가격 인상(클래스 메서드 사용)
Car.raise_price(1.6)

# 가격정보(인스턴스 메서드 - 인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())
print(Car.get_price_culc(car1))
print('\n\n')

# 인스턴스로 호출(static method)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
# 클래스로 호출(static method)
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))

print(car1.is_bmw())
print(car2.is_bmw())

