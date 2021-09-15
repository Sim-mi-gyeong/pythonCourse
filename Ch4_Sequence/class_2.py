# Chapter04-02
# 시퀀스형(순서가 있고, 번호가 나열)
# 컨테이너(Container : 서로 다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한 개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque) : 한 번 선언 후 변경 가능
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking

# b, a = a, b

# divmod(a, b): a를 b로 나눈 몫과 나머지 반환
print(divmod(100, 9))
# divmod((100,9))를 입력하면 인자가 (100, 9) 하나가 입력되어 오류
print(divmod(*(100,9)))   # *를 통해 풀어서(Unpacking)
# 결과 값을 Unpacking
print(*(divmod(100, 9)))

# x, y, rest = range(10)  # range(10)을 할당하기에 적은 수의 인자
x, y, *rest = range(10)   # x와 y에 하나씩 할당 -> 나머지 rest에 Packing이 되어 리스트로! 묶임
print(x, y, rest)   
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)
x, y, z, i, *rest = 1, 2, 3, 4, 5
print(x, y, rest)
print('\n')

# Mutable(가변) vs Immutable(불변)

l = (15, 20, 25)
m = [15, 20, 25]
print(l, id(i))
print(m, id(m))

# id 값이 달라짐
l = l * 2
m = m * 2
print(l, id(l))
print(m, id(m))

l *= 2
m *= 2
print(l, id(l))   # 튜플은 id 값이 계속 변함
print(m, id(m))   # 연산자의 할당에 따라 리스트는 다시 자기 자신에 id 할당 -> 변경이 심한 값은 리스트에 넣어놓고 연산

# sort vs sorted
# reverse, key=len, key=str.Lower, key=func...

# sorted : 정렬 후 새로운 객체 반환 -> 원본 수정 X
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print('sorted - ', sorted(f_list))
print('sorted - ', sorted(f_list, reverse=True))  # reverse=True : 역순 허용 -> 알파벳 뒤에서 부터
print('sorted - ', sorted(f_list, key=len))   # key=len : 글자 수, 길이 수 기준 정렬
print('sorted - ', sorted(f_list, key=lambda x: x[-1]))   # 끝에 한 글자를 기준으로 정렬
print('sorted - ', sorted(f_list, key=lambda x: x[-1], reverse=True)) 
print('sorted - ', f_list)

# sort : 정렬 후 객체 직접 변경 -> 원본 수정 O 
# -> 반환 값 확인(None) = 원본이 수정됨.
print('sorted - ', f_list.sort(), f_list)
print('sorted - ', f_list)
print('sorted - ', f_list.sort(reverse=True), f_list)
print('sorted - ', f_list.sort(key=len), f_list)
print('sorted - ', f_list.sort(key=lambda x: x[-1]), f_list)
print('sorted - ', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)


# List Vs Array 적합한 사용법 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트와 거의 호환 가능)
