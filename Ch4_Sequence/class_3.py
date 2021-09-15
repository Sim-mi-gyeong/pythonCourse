# Chapter04-03
# 시퀀스형(순서가 있고, 번호가 나열)
# 컨테이너(Container : 서로 다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한 개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque) : 한 번 선언 후 변경 가능
# 불변(tuple, str, bytes)


# 해시테이블
# Key에 vlaue를 저장하는 구조  __dict__, key는 중복될 수 없음.
# 파이썬 dict 해쉬(고유한 숫자의 값) 테이블 예
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# Key 값을 해싱 함수 -> 해쉬 주소 -> Key에 대한 vlaue 참조

# Dict 구조
# print(__builtins__.__dict__)

# Hash 값 확인 (가능하면 -> 고유한 값)

t1 = (10, 20, (30, 40, 50))   # 튜플 : 수정 불가 -> 고유
t2 = (10, 20, [30, 40, 50])   # 리스트 : 값의 수정이 가능한 new table -> 해쉬 값 찾을 수 없음.
print(hash(t1))
# print(hash(t2))   # 예외

print('\n\n')

# Dict Setdefault 예제
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))   # 튜플로 되어있는 값을 리스트로 통합하고자 함.
new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    # 이미 key가 있으면
    if k in new_dict1:   
        new_dict1[k].append(v)
    # 새로운 key
    else:
        new_dict1[k] = [v]
print('new_dict1 : ', new_dict1)

# Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)
print('new_dict2 : ', new_dict2)

# 주의
new_dict3 = {k: v for k, v in source}
print('new_dict3 : ', new_dict3)   # key가 중복일 때 vlaue 값을 덮어씀.
