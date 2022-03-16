# 주민등록번호
# 901201-1111111

# 이메일 주소
# nadocoding@gmail.com

# 차량번호
# 11가 1234
# 123가 1234

# IP 주소
# 192.168.0.1

import re
# abcd, book, desk
# ca?e
# -> 예측 : care, cafe, case, cave
# 정규식 사용

# p = re.compile("어떤 정규식을 컴파일할지 적어줌.")
p = re.compile("ca.e")   
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe(X)
# ^ (^de) : 문자열의 시작 > desk, destination (O) | fade(X)
# $ (se$) : 문자열의 끝 > case, base (O) | face (X)

# pattern 과 매칭되는지 확인
def print_match(m):
    # print(m.group())   # 매치되지 않으면 에러 발생   # AttributeError: 'NoneType' object has no attribute 'group'
    if m:
        print("m.group() : ", m.group())   # 일치하는 문자열 반환
        print("m.string() : ", m.string)   # 입력받은 문자열 -> 변수(함수 X)
        print("m.start() : ", m.start())   # 일치하는 문자열의 시작 index
        print("m.end() : ", m.end())   # 일치하는 문자열의 끝 index
        print("m.span() : ", m.span())   # 일치하는 문자열의 시작 / 끝 index
        print()
    else:
        print("매칭되지 않음")

m = p.match("careless")   # match : 주어진 문자열의 '처음부터' 일치하는지 확인
print_match(m)

m2 = p.search("good care")   # search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m2)

lst = p.findall("good care cafe")   # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)

# 1. p = re.complie("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인 
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는 것이 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 '리스트' 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe(X)
# ^ (^de) : 문자열의 시작 > desk, destination (O) | fade(X)
# $ (se$) : 문자열의 끝 > case, base (O) | face (X)