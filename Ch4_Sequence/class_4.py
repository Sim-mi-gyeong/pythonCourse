# Chapter04-04
# 시퀀스형(순서가 있고, 번호가 나열)
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, set -> 중복 하용 X
# Dict 및 Set 심화

# immutable Dict(읽기 전용 - 쓰기, 수정 불가능한 테이블)

from types import MappingProxyType

d = {'key1' : 'value1'}

# Read Only
d_frozen = MappingProxyType(d)

print('d : ', d, id(d))   # print(hash(d))
print('d_frozen : ', d_frozen, id(d_frozen))   # hash값 지원 X

# 수정 불가 -> 재할당 불가
# d_frozen['key2'] = 'value2'  

# 수정 가능
d['key2'] = 'value2'
print('d : ', d)


# set - 중복 가능
s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
# 원소가 하나도 없을 때에는 딕셔너리 X -> set()으로 지정해야함.
s4 = set()
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

s1.add('Melon')
# 추가 불가
# s5.add('Melon')

print('s1 : ', s1, type(s1))
print('s2 : ', s2, type(s2))
print('s3 : ', s3, type(s3))
print('s4 : ', s4, type(s4))
print('s5 : ', s5, type(s5))

# 선언 최적화
# 파이썬은 실행할 때 바이트 코드 실행 -> 파이썬 인터프리터 실행
# dif : 바이트 코드가 어떻게 실행되는지 순서를 볼 수 있음.
from dis import dis

print('------')
print(dis('{10}'))   # set을 선언할 때에는 {}의 형태로 선언하는 것이 더 좋다.
print('------')
print(dis('set([10])'))


# 지능형 집합(Comprehending Set)
print('------')

from unicodedata import name

print({name(chr(i), '') for i in range(0, 256)})
