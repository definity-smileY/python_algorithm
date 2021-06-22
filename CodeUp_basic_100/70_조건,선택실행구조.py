"""
본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
------

월이 입력될 때 계절 이름이 출력되도록 해보자.

월 : 계절 이름
12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9, 10, 11 : fall

예시
...
if n//3==1 :
  print("spring")
...

참고
때때로 수들의 특징을 관찰하고 이용하면 매우 간단히 해결할 수도 있다.

입력:
월을 의미하는 1개의 정수가 입력된다.(1 ~ 12)
12

출력:
계절 이름을 출력한다.
winter
"""
# 너무 별로인듯하다.
a = int(input())
if a in (12, 1, 2):
    print("winter")
elif a in (3, 4, 5):
    print("spring")
elif a in (6, 7, 8):
    print("summer")
else:
    print("fall")

