# -*- coding: utf-8 -*-

# ---- 문자열 기본 함수 ---- 



a = "왜그러는데대체"

# 해당되는 문자 개수 반환
b = a.count
print(b)

# 해당되는 문자의 (인덱스) 위치 반환 / 존재하지 않는 문자의 경우 -1 반환
c = a.find("는")
print(c)

# 문자열의 특정 부분을 잘라냄 
d = a.strip("대체")
print(d)

# 해당되는 문자 부분을 대체
e = d.replace("왜그러는데", "what is wrong with you!")
print(e)

# 문자열을 1. 공백을 기준으로 2. 여러 개로 나누고 3. 배열의 형태로 반환
f = e.split(" ")
print(f)

#자리수 만큼 나머지를 0으로 채움 (로렘입숨과 같은 작동 방식) / 금액을 다룰 때 유용 (0으로 단위 맞추기)
g = ("13").zfill(6)
print(g)

# 문자열을 숫자로 변환
h = "3412"
i = int(h)
print(i + 500)