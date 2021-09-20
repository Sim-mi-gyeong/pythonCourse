# Chapter04-01
# 시퀀스형(순서가 있고, 번호가 나열)
# 컨테이너(Container : 서로 다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한 개의 자료형[str, bytes, bytearray, array.array, memoryview])

# 가변(list, bytearray, array.array, memoryview, deque) : 한 번 선언 후 변경 가능
# 불변(tuple, str, bytes)

# 리스트 및 튜플 고급


# 지능형 리스트(Comprehending lists)
chars = '+_)(*&^%$#@!'
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))   # ord(s): s에 해당하는 유니코드 반환
print(code_list1)
print([chr(s) for s in code_list1])

# Comprehending lists -> 속도가 조금 더 향상
code_list2 = [ord(s) for s in chars]
print(code_list2)
print([chr(s) for s in code_list2])

# Comprehending lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
print(code_list3)
print([chr(s) for s in code_list3])

code_list4 = list(filter(lambda x: x > 40, map(ord, chars)))
print(code_list4)
print([chr(s) for s in code_list4])
print('\n')

# Generator 생성
# Generator : 시퀀스를 만들어내고, 작동 시 로컬 상태를 유지해 다음 번에 반환할 값의 위치를 정확히 가지고 있음
# -> 일종의 iterator

import array
# Generator: 한 번에 한 개의 항목을 생성(메모리 유지 X)

# tuple_g = [ord(s) for s in chars]
# print("리스트 : ", tuple_g)

tuple_g = (ord(s) for s in chars)
print("제너레이터 : ", tuple_g)  # 아직 값들을 생성하지 않은 상태, 반환할 준비만 된 상태
print(type(tuple_g))
print(next(tuple_g))   # next()를 반복할수록 첫 번째 요소부터 하나씩 반환됨.

array_g = array.array('I', (ord(s) for s in chars))
print(array_g)
print(type(array_g))
# array를 리스트로 반환
print(array_g.tolist())

print('\n\n')

# 제너레이터 예제
print(( '%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))

# 하나 출력하고 하나 생성하고
for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s)

print('\n\n')
# 리스트 주의(깊은 복사 / 얖은 복사)
marks1 = [['~'] * 3 for _ in range(4)]   # 사용하지는 않지만 반복하는 원소는 _로 처리
marks2 = [['~'] * 3] * 4

print(marks1)
print(marks2)

print()

# 수정
marks1[0][1] = 'x'   # 각 리스트의 아이디 값이 모두 다름
print("marks1 : ", marks1)

marks2[0][1] = 'x'   # 하나의 주소값(객체)이 4개로 복사가 되어 같음 -> 원본 수정 시 복사 값도 변경됨.
print("marks2 : ", marks1)   # 모든 인덱스가 다 변함 -> 의도하지 않은 값이 변경됨.

# 증명
print([id(i) for i in marks1])
print([id(i) for i in marks2])
