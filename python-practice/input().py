# -*- coding: utf-8 -*-

# ---- 기본 입출력 함수 ---- 

# input() # 콘솔창을 통해 사용자에게 입력을 받아오는 함수 / 입력 데이터를 문자열 형식으로 가지고 있다

# 사칙연산 계산기
a = input().split(' ')
# a = ['2', '5']
x = int(a[0]) # 연산을 위해 문자열을 정수형으로 형 변환
y = int(a[1])
print("x + y = ", x + y)
print("x - y = ", x - y)
print("x * y = ", x * y)
print("x / y = ", x / y)