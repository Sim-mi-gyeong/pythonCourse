# Chapter02-1
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리 

# 일반적인 코딩

# 차량 1
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color' : 'White'},
    {'forsepower' : 400 },
    {'price' : 8000}
]
# 차량 2
car_company_2 = 'BMW'
car_detail_2 = [
    {'color' : 'Black'},
    {'forsepower' : 270 },
    {'price' : 5000}
]
# 차량 3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color' : 'Silver'},
    {'forsepower' : 300 },
    {'price' : 6000}
]

# 리스트 구조
# 관리하기가 불편
# 인덱스 접근 시 실수 가능성, 삭제 불편(인덱 번를 알아야함.)

car_company_list = ['Ferrari', 'BMW', 'Audi']
car_detail_list = [
    {'color' : 'White', 'forsepower' : 400, 'price' : 8000},
    {'color' : 'Black', 'forsepower' : 270, 'price' : 5000},
    {'color' : 'Silver', 'forsepower' : 300, 'price' : 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print('\n\n')

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키: 중복 허용 X, 유일), 키 조회 예외 처리 주의
car_dicts = [ 
    {'car_company' : 'Ferrari', 'car_detail' : {'color' : 'White', 'forsepower' : 400, 'price' : 8000}},
    {'car_company' : 'BMW', 'car_detail' : {'color' : 'Black', 'forsepower' : 270, 'price' : 5000}},
    {'car_company' : 'Audi', 'car_detail' : {'color' : 'Silver', 'forsepower' : 300, 'price' : 6000}}
]
# pop(key, 'default')
del car_dicts[1]
print(car_dicts)

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

# class Car(object): object 객체 상속 -> object 생략 가능
class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):  # 문자열로 사용자 입장의 출력을 할 때
                        # 사용자 레벨
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):  # 자료형의 타입에 따른 객체를 그대로 표시할 때 -> 위의 __str__() 메소드가 없을 때 repr 메소드 출력 
                         # 개발자 레벨
        return 'repr : {} - {}'.format(self._company, self._details)

    def __reduce__(self):
        pass

car1 = Car('Ferrari', {'color' : 'White', 'forsepower' : 400, 'price' : 8000})
car2 = Car('BMW', {'color' : 'Black', 'forsepower' : 270, 'price' : 5000})
car3 = Car('Audi', {'color' : 'Silver', 'forsepower' : 300, 'price' : 6000})

print(car1)  # 매핑된 정보(Object 주소)가 나옴
print(car2)
print(car3)

print(car1.__dict__) # 클래스 안에 있는 속성 정보를 볼 수 있음

print(dir(car1)) # 안에 있는(사용 가능한) 모든 메타 정보

print('\n\n')

# 리스트 선언
car_list = []
car_list.append(car1)  # 리스트 안에서 객체에 대한 정보를 보여주므로 repr 형태로!
car_list.append(car2)
car_list.append(car3)

# 반복(__str__) -> 명시적으로 호출할 때 repr 가능
for x in car_list:
    # print(repr(x))
    print(x)
