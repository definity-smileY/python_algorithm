"""
본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
------

영문 소문자 'q'가 입력될 때까지
입력한 문자를 계속 출력하는 프로그램을 작성해보자.

입력:
문자들이 1개씩 계속해서 입력된다.
x
b
k
d
l
q
g
a
c

출력:
영문 소문자 'q'가 입력될 때까지 입력한 문자를 계속 출력한다.
x
b
k
d
l
q
"""

while True:
    a = input()
    print(a)
    if a == "q":
        break